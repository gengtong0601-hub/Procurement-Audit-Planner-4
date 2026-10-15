# Guide steps 3.1 and 3.2: build and run the spend-analyst

| | |
|---|---|
| Date | 2026-10-15 |
| Run by | Claude Code (desktop app), main session Claude Opus 5.5; sub-agent `spend-analyst` launched with the Agent tool from `.claude/agents/spend-analyst.md` |
| Sub-agent run | 51 tool calls, about 12.5 minutes, in its own context |
| Inputs | `outputs/rules.json` from step 2.2 (commit `cc4cc35`), `data/spend/*.xlsx` (3 workbooks), `data/contracts.csv` |
| Output | `outputs/analytics.json` (sha256 `cef8d3668cd55040…`) and `outputs/analytics-full/` |

## Step 3.1: the agent

`.claude/agents/spend-analyst.md` is identical to the guide's Option 1 file (checked by
diff against the saved guide text). Claude Code lists it as an available sub-agent type.

## Step 3.2: the run

The sub-agent inspected the existing `clean.py`, `analyse.py`, `selfcheck.py` and tests,
reported the thresholds it derived from `rules.json` before running, then reused the
scripts with these changes (see [script-changes.txt](script-changes.txt) and `git diff`):

- `clean.py`: word boundaries on the premises regex (the spec's `RENT` matched
  "Equipment Rentals"; the spec pattern is kept for reversal); regexes and an
  `exclusion_review` written to `cleaning-log.json`; thin-year check now relative to the
  median notices per year.
- `analyse.py`: supplier matching uses the spec's active-notice set; per-threshold tiers in
  `high_value_suppliers`; `interpretation_rules` (CPR-12, CPR-78, CPR-79/80, CPR-81);
  `method_notes`.
- `selfcheck.py`: each checked item is also opened in its workbook row with openpyxl.
- `tests/test_analytics.py`: four new tests.

Thresholds derived from `rules.json`: £1,000 (CPR-68), £25,000 (CPR-20/68/69/71),
£500,000 (CPR-04/23/24/52/65/66/71/73), £2,500,000 (CPR-66/67). All four statutory
parameters are null, so their tiers are skipped and recorded.

## Headline figures (quoted from analytics.json; indicators to investigate)

| Test | Result |
|---|---|
| Population | 10,607 rows → 8,534 after exclusions (2,015 redacted, 12 pension/statutory, 46 inter-authority); May–Jul 2026 |
| threshold_clustering | 46 payments in the band below £25,000 (52 in the comparator band above) |
| split_purchases (CPR-12) | £25,000: 64 general-procurement windows; £500,000: 3 |
| high_value_suppliers | 228 general-procurement suppliers at £25,000 annualised |
| duplicates | 698 groups; 434 share a payment-run timestamp; 37 general-procurement different-time groups |
| off_contract | of 674 suppliers ≥ £25,000: 40 exact, 7 near (auditor to confirm), 627 none; 191 general-procurement unmatched |
| expired_notice_spend (CPR-78) | 7 suppliers |
| spend_vs_award (CPR-79/80) | 8 suppliers with ratio ≥ 1.25 |

## Independent verification by the main session

- [independent-reconcile.txt](independent-reconcile.txt): [independent_reconcile.py](independent_reconcile.py)
  reads the raw workbooks with openpyxl (none of the project's scripts) and checks the
  population, redacted count, months, every flagged clustering row, all 502 split windows
  and all 698 duplicate groups (re-summed from source rows, counts, amounts and date
  spans), and the council notice count. **0 failures.** A first version failed 7 split
  windows. Each failure was a £1,000.00 payment, which correctly stays under the exclusive
  "above £1,000" trigger, so the check was corrected to use the effective trigger.
- [selfcheck.txt](selfcheck.txt): all 7 project self-checks pass.
- [pytest.txt](pytest.txt): full suite, 46 passed.
- Every figure in the sub-agent's report was compared with `analytics.json` and matches.

## Points for the auditor

- CPR-68 ("at least one quote", £1,000) counts as competition-triggering under the
  agent spec, so the primary high-value list covers all suppliers. The £25,000 tier is
  reported separately (`method_notes`). Confirm which tier the fieldwork list should use.
- The inter-authority exclusion keeps public bodies paid under "Private Contractors" (as the
  spec directs), so some neighbouring councils appear among unmatched general-procurement
  suppliers. Inter-authority arrangements are not normally published as Contracts Finder notices.
- Contracts Finder notices are thin for 2021 and 2026. "No notice found" means checking the
  council's contract register, never evidence of off-contract spend.

## Memory

The sub-agent saved three method-only notes in `.claude/agent-memory/spend-analyst/`
(gitignored): input-format quirks, tagging-regex pitfalls, threshold-tier method. They were
checked for figures and supplier names; none are present.
