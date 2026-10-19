# Procurement audit: planning memo

*Generated 2026-10-19 by `build_pack.py` from `audit-plan.json`, `risk-register.md` (revision 1), `auditor-comments.md` by tony dated 2026-10-19, `rules.json` and `analytics.json`. Status: DRAFT for challenge, QA review and auditor sign-off.*

**Indicators, not findings.** Every test below checks a control against a pattern in public data. Nothing here asserts wrongdoing by the council, a department, an officer or a supplier.

## Purpose

This pack sets out how the auditor-approved risks will be tested against the Contract Rules. Each risk has an expected control, a test step and a targeted sample or enquiry. Every pattern in the spend data is an indicator to investigate, not a finding about any person, team or supplier.

## Background

8,534 payments over the publication floor, across 3 months, were analysed against the Rules [metric:$.population.rows_after_exclusions].
Payments to redacted payees (2,015 rows) were excluded from supplier-level tests because they combine unrelated payees [metric:$.population.excluded.redacted_supplier.rows].
Duplicate-payment indicators were found in 698 groups [metric:$.tests.duplicates.count]. Many are care and education placement payments, which can legitimately repeat. Each tier is therefore sampled separately for general procurement and for placements, and every item is tested by invoice agreement rather than assumed to be an error.
Split-purchase windows also exist at the highest competition-relevant boundary (3 general-procurement windows) [metric:$.tests.split_purchases.tiers[2].headline.windows]. These are tested for aggregation and for the approval route.

## Scope

The register lists 8 rated risks. The auditor recorded 9 decisions by tony dated 2026-10-19: 8 risks are approved and in scope, and 1 is not.

| ID | Risk | Score | Band | Decision | Auditor comment |
|---|---|---|---|---|---|
| R-01 | Payments may cluster just below procurement route boundaries | 6 | Moderate | approve |  |
| R-02 | Related requirements may not be aggregated for procurement purposes | 9 | Medium - High | approve |  |
| R-03 | Supplier spend may lack a matching published contract notice | 9 | Medium - High | approve |  |
| R-04 | Payments may have been made more than once for the same amount and payee | 9 | Medium - High | approve |  |
| R-06 | Spend may exceed the annual rate of the published award value | 6 | Moderate | approve |  |
| R-07 | Waivers, exceptions and approvals may not be fully documented | 6 | Moderate | approve |  |
| R-08 | Provider choice for exempt placements may not be recorded | 6 | Moderate | approve |  |
| R-09 | A limited-assurance audit of personal budget payments may bear on payment controls | 9 | Medium - High | approve |  |

**Not in scope**

- R-05: Payments may continue after the published award has ended: reject; Excluded this cycle: lowest-rated risk (4/25); revisit next cycle.

## Approach

Risks were identified from the analytics, rated on the Council's own likelihood and impact scales, and put to the auditor for decision. One risk was rejected for this cycle and is not planned here.
For each approved risk the plan names the control the Rules require, a test step that cites the Rule, and a sample. Samples are drawn by script from the analytics lists and checked against the cleaned spend file. Where payments are used only to select items, the test first establishes the value of the underlying requirement.
Where the evidence sits outside the spend data (waivers, exception reports, case notes, prior audit actions), the test is an enquiry and document review with no transaction sample.
Placement payments are kept separate from general procurement in samples, because the Rules exempt individually chosen placements from competition on condition that the reasons for the choice are recorded. Agency-staff and grant payees with no matching notice are sampled separately.
The duplicate-indicator samples are stratified by tier and by payment type. The placement stratum carries most of the value beyond the first instance (2,488,376.56 in the same-timestamp tier alone) [metric:$.tests.duplicates.tiers.same_timestamp.by_tag.care_or_education_placement.gbp], so it receives the larger sample, one group per payee. These are targeted samples, and the auditor may extend them if the first results warrant it.
Payees that are other public authorities are left out of the quote and aggregation samples, because a quotation exercise is unlikely to apply to them. The auditor can ask for them to be added.
Two payees that may be direct-payment or prepaid channels are not sampled from the flagged value band. They are tested under the personal budgets follow-up across the payments they received in the period, after the Council says what each one represents.
Where sample order would otherwise depend on tied payment values, items are drawn one per payee in date order, so that no value ranking is implied.

The programme holds 13 expected controls and 20 test steps, with 571 sampled transactions worth £29,905,585.63, each traceable to its row in the council's published workbooks (see `audit-program.md` and `outputs/samples/`).

## Rules coverage

31 of 82 rules in `rules.json` are cited by a risk, a control or a test. The remaining 51 are not tested in this audit, for these reasons:

- statutory threshold parameter is null, so the boundary cannot be tested and no value has been invented: CPR-01, CPR-13, CPR-29, CPR-30, CPR-61, CPR-64, CPR-65, CPR-73, CPR-74
- the spend data is itself the publication of expenditure over the floor; completeness against the ledger is outside this plan: CPR-05
- budget provision, governance reporting, supplier suitability checks, Purchasing Scheme advice and record retention are held in council records, and no approved risk targets them this cycle: CPR-03, CPR-08, CPR-09, CPR-28, CPR-31
- tender procedure steps (tender format, late tenders, opening, evaluation and award basis) are evidenced in procurement files outside the spend data, and no approved risk targets them this cycle: CPR-14, CPR-15, CPR-16, CPR-17, CPR-18
- contract form, sealing, insurance, bond and contract clause content are evidenced in contract files outside the spend data, and no approved risk targets them this cycle: CPR-33, CPR-34, CPR-36, CPR-37, CPR-38, CPR-39, CPR-40, CPR-41, CPR-42, CPR-43, CPR-44, CPR-45, CPR-46, CPR-47, CPR-48, CPR-49, CPR-50, CPR-51, CPR-52, CPR-53, CPR-54, CPR-55, CPR-56, CPR-57, CPR-58, CPR-59, CPR-60, CPR-62, CPR-63
- extension approval is tested by a risk the auditor rejected for this cycle; revisit next cycle: CPR-78
- Provider Selection Regime process records sit outside the spend data, and no approved risk targets them this cycle: CPR-76

## Limitations

- The statutory threshold values are not stated in the Rules and were not supplied, so boundaries that depend on them are untested and no value has been assumed.
- Procurement bands in the Rules apply to the total value of a contract. Payment values in the spend data are not contract values, and the Rules conflict on whether VAT is included in that value. Each route test therefore starts from the value of the full requirement, not the payment.
- The notice file is a Contracts Finder export, not the Council's contract register. A supplier with no matching notice is a prompt to check the register, not evidence of off-contract spend.
- The population holds only payments over the publication floor, so split-purchase and duplicate indicators are lower bounds.
- The payment date is a payment-run timestamp, not an invoice date.
- Near-name matches are candidates for auditor confirmation and are not counted as matches.
- The number of payees above the award-rate ratio reflects how few suppliers could be tested, as 1,050 payees had no single active notice [metric:$.tests.spend_vs_award.excluded.no_unique_active_notice]. It is a test-coverage limit and does not measure how common the pattern is.
- The nature of two payees at the lowest boundary (an e-wallet and a prepaid card provider) is not known from the data. They are tested separately under the personal budgets follow-up and are excluded from the route sample until the Council confirms what they are.
- Two clauses of the Rules conflict on who may grant a waiver. The plan tests both and asks the auditor to clarify which applies.

## Review and sign-off

The challenger's points and their status are in `challenges.md`; points marked *for the auditor* need a decision at sign-off. The QA reviewer's checks and verdict are in `review.md`, which ends with the sign-off block.
