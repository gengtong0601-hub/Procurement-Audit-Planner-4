# Guide steps 3.6 and 3.7: build and run the risk-assessor

| | |
|---|---|
| Date | 2026-10-15 |
| Run by | Claude Code (desktop app), main session Claude Opus 5.5; sub-agent `risk-assessor` launched with the Agent tool from `.claude/agents/risk-assessor.md` |
| Sub-agent run | 36 tool calls, about 9 minutes |
| Inputs | `rules.json` (step 2.2), `analytics.json` (3.2), `history.json` (3.4), builder from step 3.5 |
| Outputs | `outputs/risk-ratings.json`, `risk-register.md`, `auditor-comments.md`, `risk-baseline.json`, `gate-evidence.json` |

## Step 3.6: the agent

`.claude/agents/risk-assessor.md` matches the guide's Option 2 file except for the quoted
`description` (YAML). `CLAUDE.md` already names the risk-assessor in step (3) of the flow,
which is what the guide's Option 1 asks for.

## Before the run

`outputs/auditor-comments.md` held only the eight blank rows of the superseded Codex draft
(no reviewer, date, decision or comment; checked with the builder's own parser). The builder
keeps every existing row, so those stale rows would have stayed in the decision
template. The file was removed with `git rm` so the builder could write a fresh template.
No decision existed to lose.

## Step 3.7: the run

The sub-agent rated afresh from the current inputs. Nothing was copied from the draft.

| Risk | Title | L | I | Score | Matrix | Band | Scope |
|---|---|---|---|---|---|---|---|
| R-01 | Payments just below a quotation threshold may not reflect the full requirement value | 2 | 2 | 4 | Moderate | Moderate | no |
| R-02 | Related requirements may not have been aggregated before the procurement route was chosen | 3 | 3 | 9 | High | Medium - High | yes |
| R-03 | High-value recurring spend may lack a published or recorded contract award | 3 | 4 | 12 | High | Medium - High | yes |
| R-04 | Duplicate supplier payments may not be prevented or detected | 3 | 2 | 6 | Moderate | Moderate | yes |
| R-05 | Spend may continue after a published contract term without an approved extension | 2 | 2 | 4 | Moderate | Moderate | yes |
| R-06 | Spend may exceed the awarded contract value without an approved variation | 2 | 3 | 6 | Moderate | Moderate | yes |
| R-07 | Waivers and exceptions may not be authorised and documented as the rules require | 2 | 3 | 6 | Moderate | Moderate | yes |
| R-08 | Higher-value awards may not carry the decision and approval the rules require | 1 | 4 | 4 | Moderate | Moderate | yes |
| R-09 | Placement purchasing outside competition may lack the recorded justification the rules require | 2 | 3 | 6 | Moderate | Moderate | no |

Eight themes are excluded with reasons, including the statutory-threshold routes, because the
parameters are null. R-01 and R-09 are recommended out of scope, each with a `scope_reason`.

## Checks by the main session (guide's second 3.7 prompt and more)

- [builder-rerun.txt](builder-rerun.txt): rerun gives 9 kept, 0 failures, 0 warnings. All five
  output files are byte-identical after the rerun.
- [supplier-name-check.txt](supplier-name-check.txt): every text field and the register were
  checked against all 1,926 supplier names (printed and normalised, kept and excluded spend and
  notices). No supplier under review is named. The 10 hits are three tokens:
  - "beyond" and "choice": ordinary English that matches a one-word supplier name.
  - "Ofsted", in R-09's impact justification: it quotes the council's own impact descriptor
    (strategy p.14, "External agency criticism – EG Auditor, Ofsted"). It refers to Ofsted as a
    regulator, but Ofsted is also a payee in the spend data (Professional Fees). Rewording it to
    "an inspectorate" would make the check clean. This is left for the auditor to decide.
- [check-quotes.txt](check-quotes.txt): all 22 register rule excerpts match `rules.json`
  (0 failures; the 14 mismatches from the stale draft are gone).
- [gate.txt](gate.txt): the gate correctly blocks planning, because no decisions are recorded.
- [pytest.txt](pytest.txt): 47 passed, 1 failed (see below).

## Compared with the Codex draft

Codex had 8 risks, all recommended in scope, with a maximum score of 9. This run has 9 risks
and 7 in scope. Off-contract spend is rated 3 × 4 = 12 (Major impact), duplicates have lower
impact (2), and there is a new risk for approvals of higher-value awards (R-08). Threshold
clustering (R-01) and placements (R-09) are recommended out of scope with reasons.

## Open items

1. **Auditor method question (from analytics `method_notes`):** the £1,000 one-quote band
   counts as competition-triggering, so the primary high-value list covers all suppliers.
   R-02, R-03 and R-08 cite the £25,000 tier. The auditor should confirm the tier.
2. **Part B harness:** `test_actual_prepared_outputs_end_to_end_in_isolated_copy` fails with
   "R-04: prepared plan needs a cited rule". The harness's prepared demo derives each control
   from a rule the risk cites. R-04 legitimately cites metrics and an audit (AUD-15) but no
   CPR rule, as the skill allows. At Phase 5 the planner must choose a rule for R-04's control.
   The harness assumption needs fixing in the Part B work. The register should not be changed
   just to pass the test.
3. **Builder robustness:** the risk-assessor's memory notes that citations in `scope_reason` or
   `proposed_focus` are rendered but not validated, so an unresolved one there would crash the
   render. No such citation exists now.

## Memory

`.claude/agent-memory/risk-assessor/builder-pitfalls.md` (gitignored) holds six method notes about
the builder (bool and float rendering, the figure-warning regex, uncitable paths, unvalidated
citations outside justifications, never hand-editing the template). It contains no evidence or scores.
