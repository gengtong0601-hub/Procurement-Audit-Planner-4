# Procurement audit risk register

*Revision 1, following auditor comments by tony dated 2026-10-19.*

- R-05: rejected — Out of scope this cycle: covered by the planned 2026/27 audit.

Band column uses the council's response bands (5.13, Table 4, p.19): Extreme 15 -25; Medium - High 8-12; Moderate 4 - 6; Low Up to 3. Matrix labels are reported separately. Not used for banding: 6.3, Figure 4 (Risk Escalation), p.21 gives a different Corporate Risk Register entry point ("Corporate Risk Register includes risks that score 9 or above"). Scoring-method discrepancies recorded in history.json, not resolved here: D-01, D-02, D-03, D-04, D-05, D-07.

Risk indicators to investigate; no finding of wrongdoing is made.

## Summary

| Risk | Title | L | I | Score | Matrix label | Band | Auditor override | Proposed scope |
|---|---|---|---|---|---|---|---|---|
| R-01 | Payment values may cluster just below competition thresholds | 2 | 3 | 6 | Moderate | Moderate | no | yes |
| R-02 | Related requirements may not have been aggregated | 3 | 3 | 9 | High | Medium - High | no | yes |
| R-03 | Significant suppliers may lack a matched published contract notice | 3 | 3 | 9 | High | Medium - High | no | yes |
| R-04 | Payments may have been made more than once for the same supplier and amount | 3 | 3 | 9 | High | Medium - High | no | yes |
| R-06 | Spend may exceed the annual rate implied by the published award value | 2 | 3 | 6 | Moderate | Moderate | no | yes |
| R-07 | Waivers, approvals and contract recording cannot be observed from spend data | 2 | 3 | 6 | Moderate | Moderate | no | yes |
| R-08 | Purchasing of care and personal budgets may have weaker assurance | 3 | 4 | 12 | High | Medium - High | no | yes |

## R-01: Payment values may cluster just below competition thresholds

Payments grouped just under the competition-triggering values in the Contract Rules warrant a check on whether the required quote or tender route was followed. Statutory thresholds are unknown, so only the Appendix B values were tested.

**Likelihood.** The indicator count is 369 payments in the near-threshold bands [metric:$.tests.threshold_clustering.count]. Most of the supplier concentration is in care-type services, where recurring fixed fees are common and competition is exempt for individual placements [rule:CPR-81]. The quote and tender rule is [rule:CPR-68]. Statutory-threshold tiers were skipped because their values are null, so the pattern is treated as isolated pending fieldwork. This follows the council's Unlikely descriptor [history:LIKELIHOOD-2].

**Impact.** A route missed below a threshold would mainly produce compliance and value-for-money criticism, matching the Medium descriptor of external agency criticism [history:IMPACT-3]. The mandatory quote requirement is [rule:CPR-69]. The payment data does not show whether any loss arose.

**Proposed focus.** Sample near-threshold payments outside the care and grant tags and check for the quotes or tenders required by Appendix B.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.threshold_clustering.count] 369
- [rule:CPR-68] clause App B row A, p. 12: "At least one quote must be sought from an appropriate source."
- [rule:CPR-69] clause App B row B1, p. 12: "Invitations to quote must be sent via the Procurement Portal to at least three appropriate sources, including at least one SME* or VCSE* organisation and one local supplier ****(where appropriate and possible**)."
- [rule:CPR-81] clause App C row F, p. 15: "Service Directors must ensure that a record of the reasons for the choice of provider is maintained on the individual’s case notes."

## R-02: Related requirements may not have been aggregated

Repeated payments to the same payee within a short window raise a question about whether requirements were artificially split. Periodic care and education fees can recur legitimately and are tagged separately from general procurement and works.

**Likelihood.** The rule bars artificial splitting [rule:CPR-12]. The test found 176 general-procurement windows across thresholds [metric:$.tests.split_purchases.count]. The windows span several payees and months, which fits a recurring indicator under the council's Likely descriptor [history:LIKELIHOOD-3]. Many windows are likely to be legitimate recurring charges, so this is an indicator to investigate and not a finding.

**Impact.** Undetected disaggregation could bypass quote or tender requirements [rule:CPR-68]. Total window value is 8,871,108.31 pounds. This is a count of window totals across thresholds and not a loss estimate. The Medium descriptor of external agency criticism is the most supportable level [history:IMPACT-3].

**Proposed focus.** For general-procurement windows, compare the related requirements with approvals, quotations and contract records, and confirm whether the placement exemption applies to the care windows.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.split_purchases.count] 176
- [rule:CPR-12] clause 6.16, p. 5: "There shall be no artificial splitting or disaggregation of a contract to avoid the application of the provisions of the Procurement Legislation and/or these Rules."
- [rule:CPR-68] clause App B row A, p. 12: "At least one quote must be sought from an appropriate source."

## R-03: Significant suppliers may lack a matched published contract notice

Many suppliers above the publication threshold have no matching published award notice. The notice export is not a contract register, so this is a pointer to where contract evidence should be requested and not proof of off-contract spend.

**Likelihood.** The test found 634 eligible suppliers without an exact notice match, out of 674 eligible [metric:$.tests.off_contract.count]. Notices are required above the notice threshold [rule:CPR-70] and a register of contracts must be published [rule:CPR-07]. The export holds Contracts Finder notices only, so awards made earlier, through frameworks or on Find a Tender will show as no match. The recurring pattern across suppliers supports the Likely descriptor [history:LIKELIHOOD-3] with a caveat that it may be overstated.

**Impact.** Missing contract coverage could undermine transparency and competition. This is described at Medium level as external agency criticism [history:IMPACT-3]. The register duty is [rule:CPR-35]. The council's contract register was not available, so consequences cannot be measured.

**Proposed focus.** Request the contract register and test the largest unmatched general-procurement suppliers against it. Confirm any near-match candidates by hand.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.off_contract.count] 634
- [rule:CPR-07] clause 5.2.1, p. 3: "A register of contracts, including those in progress and those awarded, with key information such as the contract value, duration and supplier."
- [rule:CPR-35] clause 10.4, p. 8: "The relevant Service Director must formally notify the Service Lead for Commissioning and Procurement (or nominated officer) of the award of all contracts for the purpose of it being recorded on the Council Contract Register."
- [rule:CPR-70] clause App B row B1, p. 12: "A contract notice must be published on the CDP"

## R-04: Payments may have been made more than once for the same supplier and amount

Identical amounts paid to the same payee within a short window may indicate duplicate payment. Batch payments for several service users at the same price can legitimately look identical.

**Likelihood.** The test found 698 groups of same-supplier same-amount payments [metric:$.tests.duplicates.count]. They recur across payees and months. This supports the Likely descriptor for the indicator [history:LIKELIHOOD-3]. Most of the largest groups are in care and education placements, where repeated fees are plausible. Written evidence of purchases is required [rule:CPR-32]. Accounts payable received a Reasonable assurance opinion [history:AUD-15], so no adverse prior assurance applies.

**Impact.** The indicator value beyond the first instance is 5,769,577.08 pounds. This is potential and not a confirmed loss. Matching the Medium financial range would need most of it to be confirmed [history:IMPACT-3]. The invoice payment rule is [rule:CPR-46].

**Proposed focus.** Trace a sample of the same-timestamp and different-time groups to invoices and remittances to separate batch charges from true duplicates.

**Evidence.**
- [history:AUD-15] audit-completed-work-2025-26-q3.pdf; page 1
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.duplicates.count] 698
- [rule:CPR-32] clause 10.1, p. 8: "There should be written evidence of all purchases (which shall include electronic evidence)."
- [rule:CPR-46] clause 10.7.9.1, p. 8: "any payment due from the Council is made no later than 30 days from the date on which the relevant invoice is regarded as valid and undisputed; and"

## R-06: Spend may exceed the annual rate implied by the published award value

For a few uniquely matched contracts, observed spend annualises above the published award value, which could indicate variations or scope growth. Many suppliers could not be tested because they lack a unique active notice.

**Likelihood.** The test found 8 contracts above the ratio limit [metric:$.tests.spend_vs_award.count]. The population is small because only suppliers with a single active notice qualify. This is consistent with an isolated indicator under the Unlikely descriptor [history:LIKELIHOOD-2]. Variation approval rules are [rule:CPR-79] and [rule:CPR-80]. Award values may be estimates or maxima.

**Impact.** Variations above the threshold need board approval [rule:CPR-80]. Spend in flagged contracts was 736,650.97 pounds in the window. Unapproved growth could draw external criticism, matching Medium [history:IMPACT-3]. This is not a loss estimate.

**Proposed focus.** Obtain contract files and variation records for the flagged contracts and compare them with the awarded value and term.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.spend_vs_award.count] 8
- [rule:CPR-79] clause App C row E, p. 14: "For contract value below the Threshold prior written approval from the Monitoring Officer and S151 Officer is required."
- [rule:CPR-80] clause App C row E, p. 14: "For contract value greater than the Threshold, approval of the relevant board, following the submission of an extension report to the relevant board with recommendation from Monitoring Officer and S151 Officer"

## R-07: Waivers, approvals and contract recording cannot be observed from spend data

Mandatory controls over waivers, exception reports, delegated approvals and contract recording have no metric in the spend data. The Rules also state the waiver authority inconsistently.

**Likelihood.** These are rule-based controls with no observable data [rule:CPR-21] [rule:CPR-25] [rule:CPR-27]. The baseline would be Rare [history:LIKELIHOOD-1]. I raised it to Unlikely [history:LIKELIHOOD-2] because the Rules name different waiver authorities in clauses [rule:CPR-20] and [rule:CPR-21], which is a design weakness. The data cannot see whether waivers were requested or approved. The prior Contract Letting audit gave Reasonable assurance [history:AUD-01], with no adverse evidence.

**Impact.** Weak waiver or approval control could expose the council to external agency criticism and challenge, matching Medium [history:IMPACT-3]. Approval requirements by value are in [rule:CPR-04] and [rule:CPR-24]. No consequence data is available.

**Proposed focus.** Request the waiver and exception log, the board exception reports and the contract register entries. Test approver, timing and documentation against the Rules.

**Evidence.**
- [history:AUD-01] audit-completed-work-2024-25-annual.pdf; page 1
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-1] risk-management-strategy-2024-27.pdf; page 15
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [rule:CPR-04] clause 4.3, p. 3: "Any contract award with a value over £500,000 is a Key Decision of the Council."
- [rule:CPR-20] clause 7.2.2, p. 6: "at the discretion of the relevant Executive Director and/or the Chief Executive, acting lawfully, who may proceed in a manner most expedient for the efficient management of the Council with reasons recorded in writing."
- [rule:CPR-21] clause 7.3, p. 6: "Only the Monitoring Officer and/or the S.151 Officer may grant a waiver or an exception to these Rules, subject to exception values and delegation thresholds detailed in these Rules and/or elsewhere in the Constitution. An officer who seeks a waiver of these Rules shall do so only in advance and only in exceptional circumstances."
- [rule:CPR-24] clause 7.4.3, p. 6: "for contracts over £500,000 the S.151 Officer and the Monitoring Officer will make a recommendation to the Executive provided an exception report has been prepared and approved by the relevant board and Corporate Board."
- [rule:CPR-25] clause 7.5.1, p. 6: "be fully documented;"
- [rule:CPR-27] clause 7.5.3, p. 7: "be subject to approval by the S.151 Officer who shall record they have considered the reasons for the waiver and that they are satisfied that the circumstances justifying the waiver are genuinely exceptional (applications for waivers which are a result of poor contract planning will rarely be considered genuinely exceptional);"

## R-08: Purchasing of care and personal budgets may have weaker assurance

A recent audit of direct payments gave limited assurance, and care placements make up a large share of the observed spend. Placements are exempt from competition but must record the reason for the provider choice.

**Likelihood.** Personal budgets (direct payments) received Limited assurance [history:AUD-16] and purchase of residential and nursing care received Reasonable assurance [history:AUD-18]. The care and education placement tag covers 353 suppliers [metric:$.tests.high_value_suppliers.by_tag.care_or_education_placement.suppliers]. The record-of-choice duty is [rule:CPR-81]. Adverse assurance in a related area supports Likely [history:LIKELIHOOD-3]. This is not a repeat finding because the same area was not audited twice.

**Impact.** On a reasonable worst case basis, weak control over a large spend area could reach the Major financial and compliance descriptor [history:IMPACT-4]. The tagged spend is 30,559,864.46 pounds in the window. This is not a loss estimate. Actual consequences are unknown.

**Proposed focus.** Check that case notes record the reasons for provider choice and that placement rates and approvals are consistent with the earlier audit recommendations.

**Evidence.**
- [history:AUD-16] audit-completed-work-2025-26-q3.pdf; page 1
- [history:AUD-18] audit-completed-work-2025-26-q3.pdf; page 1
- [history:IMPACT-4] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.high_value_suppliers.by_tag.care_or_education_placement.suppliers] 353
- [rule:CPR-81] clause App C row F, p. 15: "Service Directors must ensure that a record of the reasons for the choice of provider is maintained on the individual’s case notes."

## Excluded

- EX-01: Statutory-threshold route testing: all statutory threshold parameters are null in the rules and no value was supplied, so there is no metric to cite. This is recorded as a data gap for the auditor.
- EX-02: Performance bonds, insurance and sealing controls: the rules exist but there is no spend metric or audit history to support a rating. Cover them in fieldwork as document checks if scope allows.
- EX-03: Transparency publication completeness: the spend file is the publication itself, so no independent evidence exists to rate this.
- R-05: Out of scope this cycle: covered by the planned 2026/27 audit.

## Auditor decisions

Recorded decisions:
- R-01: approve — 
- R-02: approve — 
- R-03: approve — 
- R-04: approve — 
- R-05: reject — Out of scope this cycle: covered by the planned 2026/27 audit.
- R-06: approve — 
- R-07: approve — 
- R-08: approve — 
