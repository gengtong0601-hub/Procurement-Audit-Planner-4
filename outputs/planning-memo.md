# Procurement audit: planning memo

*Generated 2026-10-15 by `build_pack.py` from `audit-plan.json`, `risk-register.md` (revision 1), `auditor-comments.md` by Tony dated 2026-10-15, `rules.json` and `analytics.json`. Status: DRAFT for challenge, QA review and auditor sign-off.*

**Indicators, not findings.** Every test below checks a control against a pattern in public data. Nothing here asserts wrongdoing by the council, a department, an officer or a supplier.

## Purpose

The full spend population shows risk indicators in the aggregation of related purchases, contract coverage of high-value recurring spend, duplicate payments, contract extensions and variations, waivers, and the approval of higher-value awards. This audit tests whether the controls the Contract Procedure Rules require are working where those indicators sit. Indicators are patterns to investigate, not findings; nothing here presumes an outcome.

## Background

The analytics read 10,607 published payment rows dated 2026-05-01 to 2026-07-31 (3 months) and kept 8,534 after setting aside redacted-supplier, pension and inter-authority rows [metric:$.population.rows_after_exclusions]. General procurement accounts for 2,130 payments worth £28,321,138.16 across 519 suppliers [metric:$.population.tags.general_procurement.gbp]; the indicators below count that tag unless stated.
The indicators behind the approved risks: 64 general-procurement payment windows that together cross the three-quote threshold [metric:$.tests.split_purchases.tiers[1].headline.windows]; 191 suppliers whose annualised estimate reaches the notice threshold with no exact match to a published award [metric:$.tests.off_contract.headline.count]; 37 same-supplier, same-amount groups paid at different times within 7 days [metric:$.tests.duplicates.tiers.different_time.by_tag.general_procurement.rows]; 7 suppliers paid after every matching notice had ended [metric:$.tests.expired_notice_spend.count]; and 8 suppliers whose annualised spend is at least 1.25 times the annual rate of their single award [metric:$.tests.spend_vs_award.count].
Waivers, extensions, variations and award decisions are not visible in public data, so R-07 and R-08 rest on the Rules and are tested on council records. Contract letting and Accounts Payable both received Reasonable Assurance in recent internal audits [history:AUD-01] [history:AUD-15]; no repeat finding applies to any in-scope theme.

## Scope

The register lists 9 rated risks. The auditor recorded 9 decisions by Tony dated 2026-10-15: 7 risks are approved and in scope, and 2 are not.

| ID | Risk | Score | Band | Decision | Auditor comment |
|---|---|---|---|---|---|
| R-02 | Related requirements may not have been aggregated before the procurement route was chosen | 9 | Medium - High | approve | Include in scope. |
| R-03 | High-value recurring spend may lack a published or recorded contract award | 12 | Medium - High | approve | Include in scope. |
| R-04 | Duplicate supplier payments may not be prevented or detected | 6 | Moderate | approve | Include in scope. |
| R-05 | Spend may continue after a published contract term without an approved extension | 4 | Moderate | approve | Include in scope. |
| R-06 | Spend may exceed the awarded contract value without an approved variation | 6 | Moderate | approve | Include in scope. |
| R-07 | Waivers and exceptions may not be authorised and documented as the rules require | 6 | Moderate | approve | Include in scope. |
| R-08 | Higher-value awards may not carry the decision and approval the rules require | 4 | Moderate | approve | Include in scope. |

**Not in scope**

- R-01: Payments just below a quotation threshold may not reflect the full requirement value: approve; rated, recommended out of scope; approved as rated
- R-09: Placement purchasing outside competition may lack the recorded justification the rules require: approve; rated, recommended out of scope; approved as rated

## Approach

Python computed every indicator over the full population; the risk-assessor rated each risk on the council's scales, citing a rule, metric or prior audit for every score; the auditor approved the register and its scope. For each approved risk the pack names the control the Rules require, a test step and a targeted sample. Contract-level tests (R-05, R-06, R-03, R-08) come first, then the transaction tests (R-02, R-04) and the records test (R-07).
The builder draws every sample from the flagged lists, largest value first: ten items for risks scored nine or more, five otherwise, all items when fewer exist. Contract coverage is stratified: the largest unmatched suppliers, the rest of those above the Key Decision value, and those from the notice threshold up to it. Aggregation and duplicate samples take one item per supplier. Later samples skip suppliers whose contract file an earlier test examines; that test checks their flagged windows, and T-08.1 checks award decisions for the contracts those tests find.
Waiver, exemption and approval tests select from council records at fieldwork.

The programme holds 11 expected controls and 15 test steps, with 172 sampled transactions worth £17,279,357.49, each traceable to its row in the council's published workbooks (see `audit-program.md` and `outputs/samples/`).

## Rules coverage

36 of 82 rules in `rules.json` are cited by a risk, a control or a test. The remaining 46 are not tested in this audit, for these reasons:

- Statutory-threshold route: the statutory threshold parameters are null in rules.json and the analytics computed no statutory tier (excluded in the approved register): CPR-10, CPR-13, CPR-74
- Tender process controls (e-tendering, late tenders, opening, evaluation, award criteria): rule-only with no metric, and contract letting received Reasonable Assurance (excluded in the approved register): CPR-14, CPR-15, CPR-16, CPR-17, CPR-18
- Contract documents, standard clauses, sealing, bonds and insurance: rule-only content controls with no metric or history (excluded in the approved register); they can be checked on the contract files pulled for T-03.1 and T-08.1 if the auditor extends scope: CPR-33, CPR-34, CPR-36, CPR-37, CPR-38, CPR-39, CPR-40, CPR-41, CPR-42, CPR-43, CPR-44, CPR-45, CPR-46, CPR-47, CPR-48, CPR-49, CPR-50, CPR-51, CPR-52, CPR-53, CPR-54, CPR-55, CPR-56, CPR-57, CPR-58, CPR-59, CPR-60, CPR-61, CPR-62
- Transparency publication, board reporting and social value: spend publication is evidenced by the published data itself and the others have no metric or history (excluded in the approved register): CPR-01, CPR-05, CPR-06, CPR-08
- Pre-award governance steps (budget provision, supplier suitability checks, approval of notices) outside the spend data and outside every rated risk: CPR-03, CPR-09, CPR-11
- Provider Selection Regime: health-care service contracts cannot be identified in the spend data and no rated risk covers them: CPR-76
- Instruction of Counsel: a legal-services step, not a purchasing control observable in spend data: CPR-63

## Limitations

- Contracts Finder notices are not a contract register, and no council register rows were available [metric:$.contracts.register_rows]; awards published only on Find a Tender, older contracts and framework call-offs will not appear. No exact match is an indicator to check against the council's register, never evidence of off-contract spend.
- Annualised figures scale 3 months of spend by 4 and assume those months are representative; award values may be estimates or maxima. The spend-versus-award test covers only suppliers matched to exactly one active single-supplier notice with a positive award; 1,050 suppliers cannot be tested this way [metric:$.tests.spend_vs_award.excluded.no_unique_active_notice].
- Only payments above the publication limit are in the data, so aggregation and duplicate counts are lower bounds. Dates are payment-run timestamps, not invoice dates. Redacted-supplier rows are excluded from every supplier-level test.
- Statutory threshold values are null in the extracted rules, so the above-threshold route is not tested, and checks in T-02.1, T-03.2, T-06.1, T-07.1, T-07.3 and T-08.1 that depend on the Threshold are concluded only once the council confirms the figure it applied.
- Near matches between spend and notice supplier names remain unmatched until confirmed in T-03.3. Suppliers below the notice threshold are outside the contract-coverage test and are not questioned on it.
- Contract-coverage and award samples take general-procurement and agency-staff suppliers; grant spend has no testable rule (register exclusion) and premises rows are rents, rates and leases.
- Placement spend is exempt from competition and out of scope with R-09; periodic placement fees explain most aggregation and duplicate flags and are not sampled. Rules cited only by the out-of-scope risks R-01 and R-09 (CPR-68, CPR-81) count as traced to a risk but are not tested here.
- Window totals, duplicate values and annualised estimates are spend, not loss.

## Review and sign-off

The challenger's points and their status are in `challenges.md`; points marked *for the auditor* need a decision at sign-off. The QA reviewer's checks and verdict are in `review.md`, which ends with the sign-off block.
