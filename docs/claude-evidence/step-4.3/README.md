# Guide step 4.3: revise the register

| | |
|---|---|
| Date | 2026-10-15 |
| Run by | Claude Code (desktop app); the `risk-assessor` sub-agent, resumed with the guide's 4.3 instruction |
| Input | `outputs/auditor-comments.md` as recorded in step 4.2 (reviewer Tony, 9 × approve) |

## What the risk-assessor did

All nine decisions are approvals, so nothing could be amended or removed. The only change to
`outputs/risk-ratings.json` is the top-level block `"revision": {"number": 1, "changes": []}`.
The builder then rendered revision 1 and wrote `gate-evidence.json`.

## Checks by the main session

- Compared with a snapshot taken before the run: the `revision` key was added, and `risks` and
  `excluded` are identical. The nine risks are also identical to `risk-baseline.json`.
  `auditor-comments.md` is byte-identical to the file recorded in step 4.2.
- [builder-rerun.txt](builder-rerun.txt): 9 kept, 0 failures, 0 warnings, `gate=closed`. A
  rerun leaves all five outputs byte-identical.
- Register header: *"Revision 1, following auditor comments by Tony dated 2026-10-15."* The
  closing "Auditor decisions" section lists all nine decisions with their comments.
- `gate-evidence.json`: `ready: true`, `revision: 1`. Hash keys are relative paths, so the
  closed gate survives cloning the repository (fix from commit `436c77a`).
- [gate.txt](gate.txt): **gate closed** (exit 0). In scope: R-02 (9), R-03 (12), R-04 (6),
  R-05 (4), R-06 (6), R-07 (6), R-08 (4). Not in scope: R-01, R-09 (approved as rated).
- [pytest.txt](pytest.txt): 47 passed, 1 failed, in the Part B harness test
  `test_actual_prepared_outputs_end_to_end_in_isolated_copy`. Since this step it fails earlier
  than in step 3.7: the harness's prepared mode copies the root `risk-ratings.json`, which now
  carries the revision block, into a fresh run workspace without the auditor's decisions. The
  builder then rightly refuses ("revision supplied but no human decisions are recorded"). Live
  mode already drops the `revision` key; prepared mode must do the same, because a web reviewer
  starts from the pre-decision judgments. The R-04 rule-citation issue from step 3.7 is still
  behind it. Both are Part B harness fixes; the Part A outputs are correct.

## Still open for lesson 5

- The £1,000 vs £25,000 high-value tier question is not settled by the comments. R-02, R-03
  and R-08 cite the £25,000 tier. The planner should state the tier it samples from, and the
  auditor can confirm at sign-off.
- R-04 cites no contract rule, so the planner must choose the rule its control rests on.
