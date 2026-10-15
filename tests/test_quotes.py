"""Quote verifiers give the same verdict whichever PDF extractor is installed."""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFIERS = {
    'rules': [ROOT / '.claude/skills/extract-rules/verify_quotes.py', ROOT / 'outputs/rules.json', ROOT / 'data/contract-rules.pdf'],
    'history': [ROOT / 'scripts/verify_history.py', ROOT / 'outputs/history.json', ROOT / 'data/committee'],
}


@unittest.skipIf(os.name == 'nt', 'fake pdftotext is a shell script')
class ExtractorIndependenceTests(unittest.TestCase):
    def test_pdftotext_on_path_never_fails_verified_quotes(self):
        # A pdftotext whose text matches nothing: the pypdf rendering must still verify every quote.
        with tempfile.TemporaryDirectory() as tmp:
            fake = Path(tmp) / 'pdftotext'
            fake.write_text('#!/bin/sh\nprintf "unrelated text\\f"\n')
            fake.chmod(0o755)
            env = {**os.environ, 'PATH': tmp + os.pathsep + os.environ.get('PATH', '')}
            for name, args in VERIFIERS.items():
                result = subprocess.run([sys.executable, *map(str, args)], env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, f'{name}: {result.stdout[-2000:]}{result.stderr[-2000:]}')
                self.assertIn('ALL CHECKS PASSED', result.stdout, name)
                if name == 'rules':
                    self.assertIn('extractors: pypdf, pdftotext, pdftotext -layout', result.stdout)


if __name__ == '__main__':
    unittest.main()
