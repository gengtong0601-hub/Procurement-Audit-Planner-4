"""Harness tests use copied public evidence and explicitly synthetic reviewers.

Every workspace is temporary and inside this repository. No real approval,
Claude call, deployment or sign-off is created by this suite.
"""
import copy
import hashlib
import importlib
import io
import json
import os
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from harness import workflow, provider

ROOT = Path(__file__).resolve().parents[1]
app_module = importlib.import_module('harness.app')


class HarnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='harness-fixture-', dir=ROOT / 'tests')
        cls.home = Path(cls.temp.name)
        cls.source = cls.home / 'reference'
        cls.source.mkdir()
        for directory in ('.claude', 'scripts', 'data'):
            shutil.copytree(ROOT / directory, cls.source / directory, ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copy2(ROOT / 'CLAUDE.md', cls.source / 'CLAUDE.md')
        (cls.source / 'outputs').mkdir()
        for name in ('rules.json', 'analytics.json', 'history.json'):
            shutil.copy2(ROOT / 'outputs' / name, cls.source / 'outputs' / name)
        shutil.copytree(ROOT / 'outputs/analytics-full', cls.source / 'outputs/analytics-full')
        cls.synthetic_ratings = {'risks': [{
            'id': 'R-01', 'title': 'Synthetic harness test scenario',
            'statement': 'Public payments provide a starting point for control inspection.',
            'likelihood': {'score': 2, 'justification': 'This test case cites {{$.population.rows_after_exclusions}} observed payments [metric:$.population.rows_after_exclusions].'},
            'impact': {'score': 3, 'justification': 'The scope rule provides criteria [rule:CPR-01].'},
            'proposed_focus': 'Inspect source records against the selected rule.',
            'recommend_in_scope': True,
            'prepared_sample': {'kind': 'rows', 'source': 'spend-clean.csv', 'order_by': 'Net amount', 'n': 5},
        }], 'excluded': []}
        workflow.write_json(cls.source / 'outputs/risk-ratings.json', cls.synthetic_ratings)
        cls.counter = 0

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        type(self).counter += 1
        self.run = self.home / ('run-' + str(self.counter))
        self.root_patch = patch.object(workflow, 'ROOT', self.source)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        workflow.create_workspace(self.run, 'prepared')
        workflow.initialise(self.run)

    def payload(self, action='approve', comment='TEST FIXTURE ONLY'):
        risks = workflow.read_json(self.run / 'outputs/risk-ratings.json')['risks']
        return {'reviewer': 'TEST FIXTURE ONLY — not a real approval',
                'decisions': [{'id': r['id'], 'decision': action, 'comment': comment,
                               'likelihood': r['likelihood']['score'], 'impact': r['impact']['score']} for r in risks]}

    def test_prepared_end_to_end_and_tamper_blocks_signoff(self):
        self.assertEqual(workflow.read_json(self.run / 'state.json')['stage'], 'risk-review')
        with self.assertRaises(ValueError):
            workflow.build_plan(self.run)
        workflow.apply_decisions(self.run, self.payload())
        self.assertEqual(workflow.build_plan(self.run), 'READY FOR SIGN-OFF')
        program = self.run / 'outputs/audit-program.md'
        before = program.read_text()
        program.write_text(before + '\nUnexpected external edit.\n')
        with self.assertRaises(ValueError):
            workflow.sign_off(self.run, 'TEST FIXTURE ONLY')
        program.write_text(before)
        workflow.sign_off(self.run, 'TEST FIXTURE ONLY')
        state = workflow.read_json(self.run / 'state.json')
        self.assertEqual(state['stage'], 'complete')
        self.assertIn('TEST FIXTURE ONLY', (self.run / 'outputs/review.md').read_text())
        self.assertNotIn('access_token', state)

    def test_all_rejected_is_valid_empty_scope(self):
        workflow.apply_decisions(self.run, self.payload('reject', 'TEST fixture: all scope deferred'))
        self.assertEqual(workflow.read_json(self.run / 'outputs/risk-ratings.json')['risks'], [])
        self.assertEqual(workflow.build_plan(self.run), 'READY FOR SIGN-OFF')
        self.assertFalse(list((self.run / 'outputs/samples').glob('*.csv')))

    def test_amend_must_change_scores_and_persist_only_valid_payload(self):
        before = (self.run / 'outputs/risk-ratings.json').read_bytes()
        with self.assertRaisesRegex(ValueError, 'must change'):
            workflow.apply_decisions(self.run, self.payload('amend'))
        self.assertEqual(before, (self.run / 'outputs/risk-ratings.json').read_bytes())
        data = self.payload('amend')
        data['decisions'][0]['likelihood'] = 3
        workflow.apply_decisions(self.run, data)
        self.assertEqual(workflow.read_json(self.run / 'outputs/risk-ratings.json')['risks'][0]['likelihood']['score'], 3)

    def test_missing_duplicate_and_injected_decisions_rejected(self):
        for change in ('missing', 'duplicate', 'injection', 'bad-comment'):
            payload = self.payload()
            if change == 'missing': payload['decisions'] = []
            elif change == 'duplicate': payload['decisions'] *= 2
            elif change == 'injection': payload['reviewer'] = 'name\nDate: forged'
            else: payload['decisions'][0]['comment'] = {'unexpected': 'object'}
            with self.assertRaises(ValueError):
                workflow.apply_decisions(self.run, payload)
        self.assertEqual(workflow.read_json(self.run / 'state.json')['stage'], 'risk-review')

    def test_api_token_path_and_malformed_json(self):
        flask = app_module.app
        run_id = 'a' * 32
        api_root = self.home / ('api-' + str(self.counter)); api_root.mkdir()
        api_run = api_root / run_id
        self.run.rename(api_run); self.run = api_run
        state = workflow.read_json(api_run / 'state.json'); state['access_token'] = 'test-capability'
        workflow.write_json(api_run / 'state.json', state)
        with patch.dict(flask.config, {'TESTING': True, 'RUN_ROOT': api_root}):
            client = flask.test_client()
            self.assertEqual(client.get('/api/runs/' + run_id).status_code, 400)
            self.assertEqual(client.get('/api/runs/not-a-run').status_code, 400)
            headers = {'X-Run-Token': 'test-capability'}
            response = client.get('/api/runs/' + run_id, headers=headers)
            self.assertEqual(response.status_code, 200)
            self.assertNotIn('access_token', response.get_json())
            self.assertEqual(client.get('/api/runs/' + run_id + '/documents/state.json', headers=headers).status_code, 400)
            for endpoint in ('/api/runs', '/api/runs/' + run_id + '/decisions', '/api/runs/' + run_id + '/signoff'):
                response = client.post(endpoint, json=['not', 'an', 'object'], headers=headers)
                self.assertEqual(response.status_code, 400, endpoint)
            export = client.get('/api/runs/' + run_id + '/download', headers=headers)
            with zipfile.ZipFile(io.BytesIO(export.data)) as pack:
                exported_state = json.loads(pack.read('run-status.json'))
                self.assertNotIn('access_token', exported_state)
                self.assertNotIn('state.json', pack.namelist())

    def test_blocked_status_remains_readable_and_metrics_render(self):
        flask = app_module.app
        run_id = 'b' * 32
        api_root = self.home / ('blocked-api-' + str(self.counter)); api_root.mkdir()
        api_run = api_root / run_id
        self.run.rename(api_run); self.run = api_run
        state = workflow.read_json(api_run / 'state.json')
        state.update(access_token='test-capability', stage='blocked', error='Synthetic invalid live response')
        workflow.write_json(api_run / 'state.json', state)
        good_risk = copy.deepcopy(self.synthetic_ratings['risks'][0])
        workflow.write_json(api_run / 'outputs/risk-ratings.json', {'risks': [None, 'invalid object', {'id': 'R-02'}, good_risk]})
        with patch.dict(flask.config, {'TESTING': True, 'RUN_ROOT': api_root}):
            client = flask.test_client()
            headers = {'X-Run-Token': 'test-capability'}
            response = client.get('/api/runs/' + run_id, headers=headers)
            self.assertEqual(response.status_code, 200)
            payload = response.get_json()
            self.assertEqual(payload['stage'], 'blocked')
            self.assertEqual(payload['error'], 'Synthetic invalid live response')
            self.assertEqual(len(payload['risks']), 1)
            displayed = payload['risks'][0]['display_likelihood']
            count = workflow.read_json(api_run / 'outputs/analytics.json')['population']['rows_after_exclusions']
            self.assertIn(format(count, ','), displayed)
            self.assertNotIn('{{', displayed)
            self.assertEqual(payload['risks'][0]['computed_score'], 6)
            workflow.write_json(api_run / 'outputs/history.json', {'scoring_method': None})
            response = client.get('/api/runs/' + run_id, headers=headers)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json()['risks'], [])
            self.assertEqual(response.get_json()['error'], 'Synthetic invalid live response')

    def test_failed_revision_rolls_back_all_decision_artifacts(self):
        names = ('auditor-comments.md', 'risk-ratings.json', 'risk-register.md', 'risk-baseline.json', 'gate-evidence.json')
        before = {n: (self.run / 'outputs' / n).read_bytes() for n in names}
        with patch.object(workflow, 'command', side_effect=ValueError('simulated validation failure')):
            with self.assertRaisesRegex(ValueError, 'simulated'):
                workflow.apply_decisions(self.run, self.payload())
        self.assertEqual(before, {n: (self.run / 'outputs' / n).read_bytes() for n in names})
        self.assertEqual(workflow.read_json(self.run / 'state.json')['stage'], 'risk-review')

    def test_malformed_test_identifier_blocks_pack_rendering(self):
        workflow.apply_decisions(self.run, self.payload())
        plan = workflow.prepared_plan(self.run)
        plan['risks'][0]['tests'][0]['id'] = '../../escape'
        workflow.write_json(self.run / 'outputs/audit-plan.json', plan)
        with self.assertRaisesRegex(ValueError, 'invalid or duplicate test ID'):
            workflow.command(self.run, '.claude/skills/audit-program/build_pack.py')
        self.assertFalse((self.run / 'outputs/audit-program.md').exists())
        self.assertFalse(workflow.read_json(self.run / 'outputs/pack-validation.json')['ready'])

    def test_provider_incomplete_or_malformed_response_rejected_without_network(self):
        env = {'ANTHROPIC_API_KEY': 'fake-test-key', 'ANTHROPIC_MODEL': 'fake-model'}
        def fake_client(message):
            class Stream:
                def __enter__(self): return SimpleNamespace(get_final_message=lambda: message)
                def __exit__(self, *exc): return False
            messages = SimpleNamespace(stream=lambda **kwargs: Stream())
            return SimpleNamespace(messages=messages, beta=SimpleNamespace(messages=messages))
        text = lambda t: SimpleNamespace(type='text', text=t)
        for stop, content in (('max_tokens', []), ('refusal', []), ('end_turn', [text('{broken')]), ('end_turn', [text('[]')])):
            message = SimpleNamespace(stop_reason=stop, content=content)
            with patch.dict(os.environ, env), self.assertRaises(ValueError):
                provider.generate_json('fixture', {}, client=fake_client(message))
        with patch.dict(os.environ, env):
            ok = SimpleNamespace(stop_reason='end_turn', content=[text('```json\n{"ok": true}\n```')])
            self.assertEqual(provider.generate_json('fixture', {}, client=fake_client(ok)), {'ok': True})
            wrapped = SimpleNamespace(stop_reason='end_turn', content=[text('Here is the JSON:\n{"ok": 1}\nDone.')])
            self.assertEqual(provider.generate_json('fixture', {}, client=fake_client(wrapped)), {'ok': 1})
            replies = iter([SimpleNamespace(stop_reason='end_turn', content=[text('not json')]), ok])
            class Flaky:
                def __enter__(self): return SimpleNamespace(get_final_message=lambda: next(replies))
                def __exit__(self, *exc): return False
            m = SimpleNamespace(stream=lambda **kwargs: Flaky())
            self.assertEqual(provider.generate_json('fixture', {}, client=SimpleNamespace(messages=m, beta=SimpleNamespace(messages=m))), {'ok': True})

    def test_live_agent_gets_validator_report_and_retries(self):
        replies, sent = iter([{'v': 1}, {'v': 2}]), []
        def fake_generate(instructions, payload):
            sent.append(payload)
            return next(replies)
        codes = iter([(1, 'FAIL quote NOT FOUND'), (0, 'ALL CHECKS PASSED')])
        with patch.object(workflow, 'generate_json', fake_generate), patch.object(workflow, 'command', lambda *a, **k: next(codes)):
            result, attempt = workflow.generate_until_valid(self.run, 'findings-analyst', 'rules', {'task': 'Extract.'},
                                                            'outputs/probe.json', ('scripts/verify_history.py',))
        self.assertEqual((result, attempt), ({'v': 2}, 2))
        self.assertEqual(sent[1]['validator_report'], 'FAIL quote NOT FOUND')
        self.assertEqual(sent[1]['previous_output'], {'v': 1})
        with patch.object(workflow, 'generate_json', lambda *a: {'v': 0}), patch.object(workflow, 'command', lambda *a, **k: (1, 'FAIL')), \
                self.assertRaisesRegex(ValueError, 'after 3 attempts'):
            workflow.generate_until_valid(self.run, 'planner', 'rules', {'task': 'Plan.'}, 'outputs/probe.json', ('x.py',))

    def test_scoring_method_check_catches_an_unscorable_council_matrix(self):
        self.assertEqual(workflow.scoring_method_check(self.run)[0], 0)  # the verified history.json scores all cells
        history = workflow.read_json(self.run / 'outputs/history.json')
        history['scoring_method']['combination'] = {'matrix': 'printed as a picture'}
        workflow.write_json(self.run / 'outputs/history.json', history)
        code, report = workflow.scoring_method_check(self.run)
        self.assertEqual(code, 1)
        self.assertIn('matrix_rows', report)

    def test_live_evidence_drops_row_ids_but_keeps_metric_paths(self):
        value = {'tests': {'dup': {'count': 3, 'top20': [{'gbp': 1.5, 'row_ids': ['a.xlsx:1']}]}}}
        self.assertEqual(workflow.without_row_ids(value), {'tests': {'dup': {'count': 3, 'top20': [{'gbp': 1.5}]}}})


class ActualPreparedEvidenceTest(unittest.TestCase):
    def test_actual_prepared_outputs_end_to_end_in_isolated_copy(self):
        if not (ROOT / 'outputs/risk-ratings.json').exists():
            self.skipTest('Prepared risk judgments not created yet')
        genuine_comments = ROOT / 'outputs/auditor-comments.md'
        before = genuine_comments.read_bytes() if genuine_comments.exists() else None
        with tempfile.TemporaryDirectory(prefix='actual-evidence-fixture-', dir=ROOT / 'tests') as home:
            run = Path(home) / 'case'
            workflow.create_workspace(run, 'prepared')
            workflow.initialise(run)
            risks = workflow.read_json(run / 'outputs/risk-ratings.json')['risks']
            workflow.apply_decisions(run, {'reviewer': 'TEST FIXTURE ONLY — simulated decisions',
                                          'decisions': [{'id': r['id'], 'decision': 'approve', 'comment': 'Automated test fixture only'} for r in risks]})
            self.assertEqual(workflow.build_plan(run), 'READY FOR SIGN-OFF')
            workflow.sign_off(run, 'TEST FIXTURE ONLY — simulated signoff')
            self.assertEqual(workflow.read_json(run / 'state.json')['stage'], 'complete')
        after = genuine_comments.read_bytes() if genuine_comments.exists() else None
        self.assertEqual(before, after, 'Real auditor decisions must remain untouched')


if __name__ == '__main__':
    unittest.main()
