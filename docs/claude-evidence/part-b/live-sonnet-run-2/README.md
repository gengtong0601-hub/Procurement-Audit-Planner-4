# Live run 2 (Sonnet 5.5): end to end, signed off

Date: 2026-10-18 PDT (2026-10-19 UTC). Model: `claude-sonnet-5-5` on the Render deployment, harness
commit cf7b4b9. Every judgment in this run came from live Claude API calls; Python built and
checked every output. Copied from the downloaded pack, without `analytics-full/` (6 MB, rebuilt
by `scripts/`).

| Step | Result (from `events.jsonl`) |
|---|---|
| findings-analyst | history.json written; `verify_history.py` rejected attempt 1, passed attempt 2 |
| risk-assessor | 9 risks; `build_register.py` accepted attempt 1. None of the 9 matches the prepared judgments (similarity 15–31%) |
| human gate | Tony approved 8, rejected R-05 ("Excluded this cycle: lowest-rated risk (4/25); revisit next cycle.") |
| planner | PACK READY v1, v2, v3; `build_pack.py` sent each version back once before accepting it |
| challenger | 11 challenges over two rounds and a closing pass: 10 resolved, 1 for the auditor (R-06 likelihood) |
| qa-reviewer | 4/4 checks pass: quotes, numbers (585 figures), trace (8 in scope, 0 open), samples (571 transactions) |
| human sign-off | Tony, 2026-10-19 UTC; `review.md` SHA-256 7b9f9ac2… matches `run-status.json` |

The four checks were re-run locally on this pack against the repository's data and passed
4/4 again.

Earlier live attempts are not hidden:
- A Haiku 5.5 run copied the prepared examples. That led to the structure-only examples in
  commit 9295851.
- The first Sonnet run blocked at the challenge step; see [live-sonnet-run-1-blocked](../live-sonnet-run-1-blocked/README.md).
