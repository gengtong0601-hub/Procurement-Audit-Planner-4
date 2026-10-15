# Guide step 3.5: the risk-assessment skill

| | |
|---|---|
| Date | 2026-10-15 |
| Done by | Claude Code (desktop app), main session Claude Opus 5.5, at the user's request |
| Files | `.claude/skills/risk-assessment/SKILL.md`, `.claude/skills/risk-assessment/build_register.py`, `tests/test_gates.py` |

The guide gives only design requirements for this step. The skill and builder were an
original implementation written by Codex against its own `history.json`. After the native
findings-analyst run (step 3.4), the builder could not read the new scoring method: every one of the
25 matrix cells failed with "lacks explicit matrix cell/band", and the impact citations
(`IMPACT-n`) no longer resolved. This step checks the skill against the guide and fixes that.

## Checked against the guide's requirements

| Requirement | Where |
|---|---|
| Judgments in `risk-ratings.json`; `[rule:]`, `[metric:$.path]`, `[history:ID]` citations; `{{$.path}}` placeholders | SKILL.md Steps 3–4; `validate()` |
| Resolve every citation, fill placeholders, compute score, matrix label and band from the council matrix; drop risks without a resolvable citation | `validate()`, `compute_rating()` |
| Repeat-finding uplift needs an adverse audit; warn on typed figures; "Auditor decisions" section | `validate()`; register renderer |
| `auditor-comments.md` template, decisions preserved; revision checks after the gate | `run()`, `check_revision()` |
| Likelihood rubric | SKILL.md Step 2 |
| Conflicting thresholds: use one, mark the other, say so in the header | **fixed in this step** (generated header note) |
| Test on one good and one broken risk | [fixture-build.txt](fixture-build.txt) |

## Changes

1. `matrix_label` reads `scoring_method.combination.matrix_rows[].cells[]` (the
   findings-analyst's format) as well as the older `combination.matrix`. If a printed cell
   score differs from likelihood × impact, it stops.
2. `compute_rating` reads band bounds `score_low`/`score_high` as well as the older names. A null
   bound is open-ended ("Up to 3"). At least one bound must be numeric.
3. `scale_aliases` makes the council scale entries citable as `[history:IMPACT-n]` and
   `[history:LIKELIHOOD-n]` by their score (the entries have no `id`). An alias that collides
   with a real id is an error. A JSON-path form such as `impact_scale[2]` was rejected, because the
   table is printed 5→1 and indices would not match scores.
4. `selection_note` writes the register header from history.json: which response bands set
   the Band column (Table 4, p.19), the Corporate Risk Register entry point it does not use
   (Figure 4, p.21, "Score 9 or above"), and the scoring-method discrepancy IDs. An explicit
   `selection_note` in history.json still takes precedence.
5. SKILL.md is updated to match. Two tests were added: council-format matrix with an open band
   and a scale alias, and a misprinted matrix cell that must block.

## Results

- [council-matrix-grid.txt](council-matrix-grid.txt): all 25 cells of the real
  `outputs/history.json` compute a matrix label and band, and the generated header note is shown.
- [fixture-build.txt](fixture-build.txt): real rules, analytics and history with one good and one
  broken risk. **risks kept: 1, excluded by validation: 1**, with each failure listed. The
  good risk renders as L3 × I3 = 9, High / Medium - High
  ([fixture-risk-register.md](fixture-risk-register.md)).
- [pytest.txt](pytest.txt): full suite, 48 passed. This includes the 10 harness tests that failed
  after step 3.4.

## Still open

The root `outputs/risk-ratings.json` and `risk-register.md` are still the Codex draft. Their
rule IDs now point at different clauses of the step 2.2 `rules.json`, so they are stale
even though they validate. Step 3.7 (risk-assessor) must regenerate them before the
auditor gate.
