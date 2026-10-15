# Procurement audit risk register

**DRAFT — scope recommendations only; no auditor decisions recorded.**


Band column uses the council's response bands (5.13, Table 4, p.19): Extreme 15 -25; Medium - High 8-12; Moderate 4 - 6; Low Up to 3. Matrix labels are reported separately. Not used for banding: Figure 4. Risk Escalation, p.21 gives a different Corporate Risk Register entry point ("Score 9 or above"). Scoring-method discrepancies recorded in history.json, not resolved here: DIS-01, DIS-02, DIS-03, DIS-04, DIS-05, DIS-06, DIS-07, DIS-08, DIS-09, DIS-10, DIS-11, DIS-12.

Risk indicators to investigate; no finding of wrongdoing is made.

## Summary

| Risk | Title | L | I | Score | Matrix label | Band | Auditor override | Proposed scope |
|---|---|---|---|---|---|---|---|---|
| R-01 | Payments just below a quotation threshold may not reflect the full requirement value | 2 | 2 | 4 | Moderate | Moderate | no | no |
| R-02 | Related requirements may not have been aggregated before the procurement route was chosen | 3 | 3 | 9 | High | Medium - High | no | yes |
| R-03 | High-value recurring spend may lack a published or recorded contract award | 3 | 4 | 12 | High | Medium - High | no | yes |
| R-04 | Duplicate supplier payments may not be prevented or detected | 3 | 2 | 6 | Moderate | Moderate | no | yes |
| R-05 | Spend may continue after a published contract term without an approved extension | 2 | 2 | 4 | Moderate | Moderate | no | yes |
| R-06 | Spend may exceed the awarded contract value without an approved variation | 2 | 3 | 6 | Moderate | Moderate | no | yes |
| R-07 | Waivers and exceptions may not be authorised and documented as the rules require | 2 | 3 | 6 | Moderate | Moderate | no | yes |
| R-08 | Higher-value awards may not carry the decision and approval the rules require | 1 | 4 | 4 | Moderate | Moderate | no | yes |
| R-09 | Placement purchasing outside competition may lack the recorded justification the rules require | 2 | 3 | 6 | Moderate | Moderate | no | no |

## R-01: Payments just below a quotation threshold may not reflect the full requirement value

Payments that sit just below a quotation threshold warrant checking that the procurement route matched the full value of the requirement.

**Likelihood.** At the three-quote threshold of £25,000.00 [rule:CPR-69], 46 payments fall in the band just below it [metric:$.tests.threshold_clustering.tiers[1].count] against 52 at or just above it [metric:$.tests.threshold_clustering.tiers[1].comparator.count], so there is no excess below the line, and only 10 of the band payments are general procurement [metric:$.tests.threshold_clustering.tiers[1].by_tag.general_procurement.rows]. In the one-quote band [rule:CPR-68] more payments sit below the line than above it, but 218 of the 323 are placement-tagged [metric:$.tests.threshold_clustering.tiers[0].by_tag.care_or_education_placement.rows], and individually chosen placements are exempt from competition [rule:CPR-81]. An isolated indicator: rubric two, the council's Unlikely descriptor [history:LIKELIHOOD-2].

**Impact.** Pricing a requirement just under this threshold would avoid three portal quotations [rule:CPR-69] and a contract notice [rule:CPR-70]. At these values the reasonable worst case fits the council's Minor descriptor: low possibility of legal challenge and a financial consequence in the Minor band [history:IMPACT-2]. Payment values are spend, not loss; no consequence data is available.

**Proposed focus.** If brought into scope, review quotation evidence for the general-procurement payments just below the three-quote threshold, alongside aggregation testing of the same suppliers.

**Evidence.**
- [history:IMPACT-2] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.threshold_clustering.tiers[0].by_tag.care_or_education_placement.rows] 218
- [metric:$.tests.threshold_clustering.tiers[1].by_tag.general_procurement.rows] 10
- [metric:$.tests.threshold_clustering.tiers[1].comparator.count] 52
- [metric:$.tests.threshold_clustering.tiers[1].count] 46
- [rule:CPR-68] clause App B row A, p. 12: "At least one quote must be sought from an appropriate source."
- [rule:CPR-69] clause App B row B1, p. 12: "Invitations to quote must be sent via the Procurement Portal to at least three appropriate sources, including at least one SME* or VCSE* organisation and one local supplier ****(where appropriate and possible**)."
- [rule:CPR-70] clause App B row B1, p. 12: "A contract notice must be published on the CDP"
- [rule:CPR-81] clause App C row F, p. 15: "Service Directors must ensure that a record of the reasons for the choice of provider is maintained on the individual’s case notes."

## R-02: Related requirements may not have been aggregated before the procurement route was chosen

Recurring payments to the same supplier within a short window, each below a threshold but together above it, warrant checking whether one requirement was divided across orders.

**Likelihood.** The no-splitting rule is the control [rule:CPR-12]. At the three-quote threshold, 64 general-procurement windows of 30 days combine payments that are each below the threshold [metric:$.tests.split_purchases.tiers[1].headline.windows], across 42 suppliers [metric:$.tests.split_purchases.tiers[1].by_tag.general_procurement.suppliers]; 3 general-procurement windows also cross the Key Decision value [metric:$.tests.split_purchases.tiers[2].headline.windows] [rule:CPR-04]. A recurring indicator across suppliers: rubric three, the council's Likely descriptor [history:LIKELIHOOD-3]. Invoicing under contracts already let will explain many windows, and the 178 placement windows are reported separately because periodic fees recur [metric:$.tests.split_purchases.tiers[1].placements.windows]. The published data omits smaller payments, so the counts are lower bounds.

**Impact.** Dividing a requirement could bypass three portal quotations [rule:CPR-69] or, at higher values, the report, board and Key Decision route [rule:CPR-66]. The reasonable worst case fits the council's Medium descriptor: reasonable possibility of successful legal challenge or regulatory interest, and external auditor criticism [history:IMPACT-3]. Window totals are spend, not loss; no consequence data is available.

**Proposed focus.** For sampled general-procurement windows, establish whether the payments formed one requirement; if so, check the route followed against the aggregate value (quotations, portal records, notice and approvals). Set aside windows that are instalments under a contract already let once that contract is confirmed.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.split_purchases.tiers[1].by_tag.general_procurement.suppliers] 42
- [metric:$.tests.split_purchases.tiers[1].headline.windows] 64
- [metric:$.tests.split_purchases.tiers[1].placements.windows] 178
- [metric:$.tests.split_purchases.tiers[2].headline.windows] 3
- [rule:CPR-04] clause 4.3, p. 3: "Any contract award with a value over £500,000 is a Key Decision of the Council."
- [rule:CPR-12] clause 6.16, p. 5: "There shall be no artificial splitting or disaggregation of a contract to avoid the application of the provisions of the Procurement Legislation and/or these Rules."
- [rule:CPR-66] clause App A row 3, p. 11: "The award of these contracts shall be a Key Decision delegated to the relevant Service Director in consultation with the relevant Portfolio Holder (following recommendation by the relevant Executive Director, S151 officer and Monitoring Officer) to award the contract provided: a) a written report by the relevant Service Director (or such officers as nominated by them in writing) has been provided and approved by the relevant board; and b) such decision have been made in accordance with Parts [] (Call-In) and [] (Forward Plan)."
- [rule:CPR-69] clause App B row B1, p. 12: "Invitations to quote must be sent via the Procurement Portal to at least three appropriate sources, including at least one SME* or VCSE* organisation and one local supplier ****(where appropriate and possible**)."

## R-03: High-value recurring spend may lack a published or recorded contract award

Suppliers whose annualised spend reaches the contract-notice threshold but who match no published award notice warrant checking against the council's own contract records.

**Likelihood.** Among suppliers whose annualised estimate reaches the notice threshold of £25,000 [rule:CPR-70], 191 general-procurement suppliers have no exact match to a published award [metric:$.tests.off_contract.headline.count], against 40 exact matches across all tags [metric:$.tests.off_contract.by_match_class.exact.count]. The indicator recurs across many suppliers: rubric three, the council's Likely descriptor [history:LIKELIHOOD-3]. It is not raised to four because the notice export is not a contract register, the analysis held no rows from the council's own register [metric:$.contracts.register_rows], some publication years are thin, and older, Find a Tender-only or framework awards will not appear. Recording each award on the Contract Register is a control the data cannot see [rule:CPR-35].

**Impact.** 21 general-procurement suppliers have annualised estimates above £500,000.00 [metric:$.tests.high_value_suppliers.tiers[2].headline.count], and the unmatched top-twenty list includes suppliers in that range, where awards are Key Decisions [rule:CPR-04]. If such spend had no compliant award, the reasonable worst case fits the council's Major descriptor: high possibility of legal challenge and of regulatory intervention [history:IMPACT-4]. Annualised figures are estimates, and spend is not loss.

**Proposed focus.** Request the council's contract register. For sampled unmatched general-procurement suppliers above the notice threshold, obtain the contract, its term and value, and the notice or recorded exemption; confirm near matches before treating them as unmatched. Suppliers below the notice threshold are outside this test and are not to be questioned on it.

**Evidence.**
- [history:IMPACT-4] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.contracts.register_rows] 0
- [metric:$.tests.high_value_suppliers.tiers[2].headline.count] 21
- [metric:$.tests.off_contract.by_match_class.exact.count] 40
- [metric:$.tests.off_contract.headline.count] 191
- [rule:CPR-04] clause 4.3, p. 3: "Any contract award with a value over £500,000 is a Key Decision of the Council."
- [rule:CPR-35] clause 10.4, p. 8: "The relevant Service Director must formally notify the Service Lead for Commissioning and Procurement (or nominated officer) of the award of all contracts for the purpose of it being recorded on the Council Contract Register."
- [rule:CPR-70] clause App B row B1, p. 12: "A contract notice must be published on the CDP"

## R-04: Duplicate supplier payments may not be prevented or detected

Payments to the same supplier for exactly the same amount within a short window warrant matching to invoices before any conclusion is drawn.

**Likelihood.** Among general-procurement payments, 37 groups of same-supplier, same-amount payments made at different times within 7 days [metric:$.tests.duplicates.tiers.different_time.by_tag.general_procurement.rows] span 22 suppliers [metric:$.tests.duplicates.tiers.different_time.by_tag.general_procurement.suppliers], with 33 further groups inside single payment runs [metric:$.tests.duplicates.tiers.same_timestamp.by_tag.general_procurement.rows]. A recurring indicator across suppliers: rubric three, the council's Likely descriptor [history:LIKELIHOOD-3]. Most flagged groups overall are placement-tagged, where identical periodic fees are expected, and are not counted here. Accounts Payable received Reasonable Assurance [history:AUD-15], which is not adverse and gives no uplift; no contract rule addresses duplicate payment directly.

**Impact.** Value beyond the first payment in the different-time general-procurement groups is £297,355.44 [metric:$.tests.duplicates.tiers.different_time.by_tag.general_procurement.gbp], an indicator rather than confirmed loss. Genuine duplicates are normally recoverable from suppliers, so the reasonable worst case net loss fits the council's Minor descriptor [history:IMPACT-2].

**Proposed focus.** For sampled general-procurement groups, match each payment to a distinct invoice and order; where a genuine duplicate is found, confirm it was detected and recovered. Review placement-tagged groups only by exception.

**Evidence.**
- [history:AUD-15] audit-completed-work-2025-26-q3.pdf; page 1
- [history:IMPACT-2] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.duplicates.tiers.different_time.by_tag.general_procurement.gbp] 297,355.44
- [metric:$.tests.duplicates.tiers.different_time.by_tag.general_procurement.rows] 37
- [metric:$.tests.duplicates.tiers.different_time.by_tag.general_procurement.suppliers] 22
- [metric:$.tests.duplicates.tiers.same_timestamp.by_tag.general_procurement.rows] 33

## R-05: Spend may continue after a published contract term without an approved extension

Suppliers paid in the period whose every matched notice had ended before the period began warrant checking for an approved extension or a newer contract.

**Likelihood.** 7 suppliers were paid in the period although every matching published notice had ended before it began [metric:$.tests.expired_notice_spend.count]; extending a contract needs S151 approval [rule:CPR-78]. A small set, mostly of low spend: an isolated indicator, rubric two, the council's Unlikely descriptor [history:LIKELIHOOD-2]. A newer contract may exist without a notice in the export.

**Impact.** Spend with these suppliers in the period is £190,366.92 [metric:$.tests.expired_notice_spend.gbp]. An unapproved extension at this scale fits the council's Minor descriptor: low possibility of legal challenge [history:IMPACT-2]. Spend is not loss.

**Proposed focus.** For each flagged supplier, obtain the current contract or the extension and its S151 approval; record where a newer award explains the payments.

**Evidence.**
- [history:IMPACT-2] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.expired_notice_spend.count] 7
- [metric:$.tests.expired_notice_spend.gbp] 190,366.92
- [rule:CPR-78] clause App C row D, p. 14: "Approval of the S151 Officer"

## R-06: Spend may exceed the awarded contract value without an approved variation

Suppliers whose annualised spend runs well above the annual rate of their single published award warrant checking for an approved variation.

**Likelihood.** 8 suppliers have annualised spend at least 1.25 times the annual rate of their single published award [metric:$.tests.spend_vs_award.count]; variations need prior Monitoring Officer and S151 approval [rule:CPR-79], or board approval above the Threshold [rule:CPR-80]. Several flags rest on one or two payments, where annualising one quarter can overstate the run-rate, and award values may be estimates or maxima. An isolated indicator: rubric two, the council's Unlikely descriptor [history:LIKELIHOOD-2]. Most suppliers could not be tested because they lack a unique active notice [metric:$.tests.spend_vs_award.excluded.no_unique_active_notice].

**Impact.** Spend with flagged suppliers in the period is £736,650.97 [metric:$.tests.spend_vs_award.gbp]. Spend beyond an award without an approved variation fits the council's Medium descriptor: reasonable possibility of successful legal challenge and external audit criticism [history:IMPACT-3]. This is spend, not loss.

**Proposed focus.** For each flagged supplier, compare spend with the award value, term and scope, and obtain any approved variation; confirm whether the published award value is an estimate or a maximum.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.spend_vs_award.count] 8
- [metric:$.tests.spend_vs_award.excluded.no_unique_active_notice] 1,050
- [metric:$.tests.spend_vs_award.gbp] 736,650.97
- [rule:CPR-79] clause App C row E, p. 14: "For contract value below the Threshold prior written approval from the Monitoring Officer and S151 Officer is required."
- [rule:CPR-80] clause App C row E, p. 14: "For contract value greater than the Threshold, approval of the relevant board, following the submission of an extension report to the relevant board with recommendation from Monitoring Officer and S151 Officer"

## R-07: Waivers and exceptions may not be authorised and documented as the rules require

Waivers of competition and exceptions to the rules cannot be seen in spend data; whether they were approved in advance, at the right level and fully documented needs direct testing.

**Likelihood.** Only the Monitoring Officer and/or S151 Officer may grant a waiver, and only in advance [rule:CPR-21], yet another clause lets the relevant Executive Director or the Chief Executive waive competition at discretion [rule:CPR-20]; that conflict in the rules can lead to approval at the wrong level. Every waiver must be fully documented [rule:CPR-25] and approved by the S151 Officer [rule:CPR-27]. No metric observes waivers, so this is rated on the rules and the gap. A rule-only control would be rubric one; the design conflict raises it to two, the council's Unlikely descriptor [history:LIKELIHOOD-2].

**Impact.** A waiver removes competition altogether; for higher-value contracts the reasonable worst case fits the council's Medium descriptor: reasonable possibility of successful legal challenge and external audit criticism [history:IMPACT-3] [rule:CPR-21]. No waiver data is available to size the exposure.

**Proposed focus.** Obtain the waiver and exception register. For a sample, confirm advance approval by the officer the rules require, the documented reasons, the S151 record and, where needed, the board exception report. Check whether unmatched high-value suppliers appear on the register.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [rule:CPR-20] clause 7.2.2, p. 6: "at the discretion of the relevant Executive Director and/or the Chief Executive, acting lawfully, who may proceed in a manner most expedient for the efficient management of the Council with reasons recorded in writing."
- [rule:CPR-21] clause 7.3, p. 6: "Only the Monitoring Officer and/or the S.151 Officer may grant a waiver or an exception to these Rules, subject to exception values and delegation thresholds detailed in these Rules and/or elsewhere in the Constitution. An officer who seeks a waiver of these Rules shall do so only in advance and only in exceptional circumstances."
- [rule:CPR-25] clause 7.5.1, p. 6: "be fully documented;"
- [rule:CPR-27] clause 7.5.3, p. 7: "be subject to approval by the S.151 Officer who shall record they have considered the reasons for the waiver and that they are satisfied that the circumstances justifying the waiver are genuinely exceptional (applications for waivers which are a result of poor contract planning will rarely be considered genuinely exceptional);"

## R-08: Higher-value awards may not carry the decision and approval the rules require

Contracts above the Key Decision value need Key Decision, board and Executive approvals that spend data cannot show; these need direct testing on contract files.

**Likelihood.** Awards over £500,000.00 must be taken as Key Decisions [rule:CPR-04], with board-approved reports in the middle band [rule:CPR-66] and Executive approval at the top band [rule:CPR-67]. No metric observes approvals and no adverse audit history exists; contract letting received Reasonable Assurance [history:AUD-01]. A rule-only control with no adverse evidence: rubric one, the council's Rare descriptor [history:LIKELIHOOD-1].

**Impact.** 21 general-procurement suppliers have annualised estimates above that value [metric:$.tests.high_value_suppliers.tiers[2].headline.count]. An award at that scale without the required decision fits the council's Major descriptor: high possibility of legal challenge and of regulatory intervention [history:IMPACT-4].

**Proposed focus.** For high-value suppliers sampled under the notice-coverage test, check the decision record, board report and Forward Plan or Executive approval against the value band.

**Evidence.**
- [history:AUD-01] audit-completed-work-2024-25-annual.pdf; page 1
- [history:IMPACT-4] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-1] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.high_value_suppliers.tiers[2].headline.count] 21
- [rule:CPR-04] clause 4.3, p. 3: "Any contract award with a value over £500,000 is a Key Decision of the Council."
- [rule:CPR-66] clause App A row 3, p. 11: "The award of these contracts shall be a Key Decision delegated to the relevant Service Director in consultation with the relevant Portfolio Holder (following recommendation by the relevant Executive Director, S151 officer and Monitoring Officer) to award the contract provided: a) a written report by the relevant Service Director (or such officers as nominated by them in writing) has been provided and approved by the relevant board; and b) such decision have been made in accordance with Parts [] (Call-In) and [] (Forward Plan)."
- [rule:CPR-67] clause App A row 4, p. 11: "Contracts with a value in excess of £2.5million shall require Executive approval, which may be given as below. The Executive shall receive quarterly reports detailing contracts being procured and seeking delegated authority from Executive for the relevant Service Director / to award the contract following the procurement process in consultation with the relevant Portfolio Holder, S.151 Officer and the Monitoring Officer."

## R-09: Placement purchasing outside competition may lack the recorded justification the rules require

Individually chosen care and education placements are exempt from competition, but the rules still require recorded reasons for the provider choice, which spend data cannot show.

**Likelihood.** The reasons for the choice of provider must be kept on the case notes [rule:CPR-81]; spend data cannot see case notes, so this is rated on the rule and the gap. Placement-tagged spend is the largest tag in the data [metric:$.population.tags.care_or_education_placement.gbp] and dominates the split and duplicate indicators, which periodic fees largely explain. Personal Budgets (Direct Payments) received Limited Assurance [history:AUD-16]: adjacent adverse evidence, not a repeat finding on this theme, so no uplift applies, but it lifts the rule-only rubric one to two, the council's Unlikely descriptor [history:LIKELIHOOD-2]. Purchase of residential and nursing care received Reasonable Assurance [history:AUD-18].

**Impact.** A poorly justified provider choice affects vulnerable people and value for money; the reasonable worst case fits the council's Medium descriptor: external agency criticism, for example by an inspectorate, and reasonable possibility of regulatory interest [history:IMPACT-3]. No consequence data is available.

**Proposed focus.** If brought into scope, sample placement-tagged payments, prioritising children's and education placements outside the recent care-purchasing audit, and check the recorded reasons for the provider choice.

**Evidence.**
- [history:AUD-16] audit-completed-work-2025-26-q3.pdf; page 1
- [history:AUD-18] audit-completed-work-2025-26-q3.pdf; page 1
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.population.tags.care_or_education_placement.gbp] 30,571,711.30
- [rule:CPR-81] clause App C row F, p. 15: "Service Directors must ensure that a record of the reasons for the choice of provider is maintained on the individual’s case notes."

## Excluded

- Statutory-threshold route: Above-threshold advertising, tender and award routes (CPR-10, CPR-13, CPR-74) cannot be tested: the statutory threshold parameters are null in rules.json and analytics computed no statutory tier. The auditor should supply the figures and their source.
- Tender process controls: E-tendering, late tenders and evaluation (CPR-13 to CPR-18) are rule-only with no metric; contract letting received Reasonable Assurance (AUD-01). Testable on files if the auditor extends scope.
- Contract documents, sealing, bonds and insurance: Minimum clauses, sealing, bonds and insurance (CPR-33 to CPR-62) are rule-only content controls with no metric or history; they can be checked on contract files pulled for in-scope risks.
- Transparency publication and social value: Spend publication (CPR-05) is evidenced by the published data itself; ITT publication, board reporting and social value (CPR-01, CPR-06, CPR-08) have no metric or history. Register completeness (CPR-07, CPR-35) is handled under notice coverage.
- Purchasing schemes and frameworks: Advice before use and approval without further competition (CPR-28, CPR-77) are rule-only; framework call-offs cannot be identified reliably in spend data and are treated as a known reason for missing notices.
- Grant-tagged spend: Clause 1.6.2 treats grants as contracts but rules.json excludes it as a definition, so no testable rule applies; grant spend is reported separately in analytics.
- Fraud risk themes: RT-01, RT-08, RT-09 and RT-12 name fraud generally, not procurement; the Anti-Fraud Work Plan is not in the papers. Fraud-relevant patterns are covered by the indicator risks.
- Repeat-finding uplift: No repeat finding exists on any rated theme: no agreed actions are published and no theme has a prior adverse opinion followed by another. AUD-16 (Limited) is used as adjacent evidence, not an uplift.

## Auditor decisions

No decisions recorded; the auditor must complete auditor-comments.md.
