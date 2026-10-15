# Guide steps 3.3 and 3.4: build, run and check the findings-analyst

| | |
|---|---|
| Date | 2026-10-15 |
| Run by | Claude Code (desktop app), main session Claude Opus 5.5; sub-agent `findings-analyst` launched with the Agent tool from `.claude/agents/findings-analyst.md` |
| Sub-agent run | 42 tool calls (about 11 minutes), then 5 more for one requested fix |
| Inputs | the four PDFs in `data/committee/` (hashes in `data/manifest.json`) |
| Output | `outputs/history.json` (sha256 `a06e6d19ecd8f5a4…`), written from scratch; the earlier Codex file was not copied |

## Step 3.3: the agent

`.claude/agents/findings-analyst.md` matches the guide's Option 2 file except that the
`description` value is quoted. It contains colons, which is invalid YAML unquoted (recorded
in `docs/IMPLEMENTATION_NOTES.md`). `scripts/verify_history.py` is the guide's verifier,
extended in commit `436c77a` to check every available extractor.

## Step 3.4: the run

The sub-agent extracted plain and layout text with pdftotext, rebuilt garbled tables from
the layout text and recorded:

- 20 audits (16 completed, 3 follow-ups, 1 advisory); 4 directly procurement-related
  (Contract Letting, Accounts Payable, Purchase of Residential and Nursing Care Provision,
  Personal Budgets / Direct Payments).
- No agreed actions and no planned audits in the papers, recorded as gaps (8 gaps in all,
  including the exempt Corporate Risk Register and the missing plan appendices).
- A usable council scoring method: 5-point likelihood and impact scales, 5×5 matrix,
  four RAG bands, appetite by category.
- 15 discrepancies recorded, not resolved, e.g. Figure 4 "Score 9 or above" vs Table 4
  (15–25) for Corporate Risk Register entry; prose "Medium (2)" vs table 3; overlapping
  Medium/Major budget bands; matrix "High" vs Table 4 "Medium - High".

Verifier: **ALL CHECKS PASSED, 172 sourced items, 172 quotes**, with pdftotext on PATH
and with pypdf only ([with pdftotext](verify-with-pdftotext.txt), [pypdf only](verify-pypdf-only.txt)).

### Fix requested by the main session

The first file reused ids DIS-01 to DIS-12 for pointer entries under
`scoring_method.discrepancies`, so every id appeared twice and `build_register.py` refused
the file ("duplicate history id"). The sub-agent was sent the problem, changed the pointer
key to `discrepancy_id`, and re-verified. Now there are 47 ids with 0 duplicates, and all 12
pointers resolve. Its first report also called the Garland row AUD-12. The file had it right
as AUD-11; the report was corrected.

## Spot-checks against rendered pages (guide's second 3.4 prompt)

| Item | history.json | Page image | Result |
|---|---|---|---|
| Audit opinion | AUD-11 Garland (now Burghfield Common Federation): Weak / Unsatisfactory | [annual p.2](spot-check-annual-p02-AUD-11.png) | Matches (red cell) |
| Impact scale | Minor (2): 0.01%–0.1% of budget, £17.5k–£175k | [strategy p.14](spot-check-strategy-p14-impact-minor.png) | Matches; page also shows the "Medium (2)" prose error and the overlapping bands |
| Risk band | Medium - High (Amber) 8–12 | [strategy p.19](spot-check-strategy-p19-band-8-12.png) | Matches |
| Discrepancy | Corporate Risk Register "Score 9 or above" | [strategy p.21](spot-check-strategy-p21-crr-threshold.png) | Matches; conflicts with Table 4 as recorded |

## Compared with the Codex version

Same 20 audits and 12 risk themes; scoring method usable in both. New: 172 sourced items,
all quoted (Codex: 106 items, 81 quotes); 8 gaps (4); 15 discrepancies (6).

## Known downstream issues (for steps 3.5–3.7)

The full test suite has 10 harness failures ([pytest.txt](pytest.txt)), all from
`build_register.py` running on the real outputs:

1. The new `scoring_method` uses `combination.matrix_rows[].cells[]` and band
   `score_low`/`score_high`. `build_register.py` (the step 3.5 implementation) reads only
   `combination.matrix` and `min_score`/`max_score`, so every cell fails with "lacks explicit
   matrix cell/band". The data is complete; the builder must read these field names.
2. The Codex draft `risk-ratings.json` cites old history ids such as `IMPACT-3`. Scale
   entries no longer carry ids, so step 3.5 must define how the impact and likelihood
   descriptors are cited, and the risk-assessor (3.7) must re-rate from the current files.

The web harness's prepared mode depends on these outputs and will not run end to end
until step 3.7 is complete.

## Memory

Four method-only notes in `.claude/agent-memory/findings-analyst/` (gitignored): extraction
quirks, verifier robustness under pypdf, expected absent papers, id uniqueness. They contain no
opinions or figures, only dates.
