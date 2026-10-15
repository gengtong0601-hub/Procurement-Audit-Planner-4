# Guide step 2.2: Run the skill (`/extract-rules`)

| | |
|---|---|
| Date | 2026-10-15 |
| Run by | Claude Code (desktop app, Code tab), model Claude Opus 5.5, invoked at the user's request |
| Skill | `.claude/skills/extract-rules/SKILL.md`, invoked natively through Claude Code's skill mechanism |
| Input | `data/contract-rules.pdf`, 15 pages, sha256 `0e87492f…6b276` (matches `data/manifest.json`) |
| Text extraction | `pdftotext` (poppler 26.09.0), plain and `-layout`, as the skill specifies |
| Output | `outputs/rules.json`, sha256 `e7391cad…911d5` |
| Previous version | Codex-prepared `rules.json` kept in git commit `caebffd` |

## Result

`ALL CHECKS PASSED (82 rules, 85 excluded, 0 warning(s))` with pdftotext on PATH **and**
with pypdf only (the Docker/deployment case). Logs:
[verify-with-pdftotext.txt](verify-with-pdftotext.txt), [verify-pypdf-only.txt](verify-pypdf-only.txt).

- Rules by type: 52 required-action, 24 approver, 5 threshold, 1 anti-avoidance.
- Parameters awaiting the auditor (all `null`): goods & services, works & concessions and
  light-touch statutory thresholds, plus a category selector for "the relevant Threshold".
- 16 document notes (VAT basis conflict, `[]` placeholders, £500,000 and Threshold boundary
  gaps, £2.5m inclusivity, 7.2.2 vs 7.3 waiver authority, drafting errors).
- Full rule list: [rules-table.md](rules-table.md).

One fix during the verify loop: CPR-05 first quoted the 5.1 lead-in and the 5.1.1 item together.
pypdf prints the number `5.1.1` between them, so the quote was shortened to the item text
only, as the skill directs for list items.

## Spot-checks against the rendered PDF

| Kind | Rule | Page image | Result |
|---|---|---|---|
| Prose clause | CPR-12 (6.16, no splitting) | [p.5](spot-check-p05-clause-6.16.png) | Quote matches word for word; same page shows VAT in 6.15 |
| Appendix row | CPR-66 (App A row 3) | [p.11](spot-check-p11-appA-row3.png) | Matches; PDF prints "Call-In" across a line break, `[]` placeholders highlighted in the original |
| Threshold | CPR-69 (App B row B1, £25,000 to Threshold) | [p.12](spot-check-p12-appB-rowB1.png) | Matches; header confirms "exclusive of VAT" |

These checks were run by Claude. The guide's human step is for the auditor to repeat at
least these three against the PDF.

## Compared with the Codex version (`caebffd`)

The extraction was done from the PDF text, then compared afterwards. Both versions give the same
publication threshold (£25,000, App B rows B1/B2) and the same App C row D/E mapping that
the spend tests use. Differences in judgment:

- Codex typed the £500 spend-publication (5.1.1) and £5,000 ITT-publication (5.2) duties as
  `threshold`, which creates £500 and £5,000 clustering tiers. This run types them as
  `required-action`, because they are transparency duties, not procurement-route boundaries.
- Testable here, excluded by Codex: 4.1, 6.4, 7.2.1, 10.1, 10.5.
- Excluded here, testable for Codex: 3.2, 4.4, 6.11, 11.6, 11.10, 11.12 (reasons in `excluded`).

## Downstream effect

Rule IDs changed, so the Codex draft register (`outputs/risk-register.md`) now cites the wrong
rules: `scripts/checks/check_quotes.py` reports 14 register-excerpt mismatches. This is
expected until steps 3.2–3.7 regenerate the analytics and the register from this file.
