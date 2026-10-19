# Procurement audit risk register

*Revision 1, following auditor comments by tony dated 2026-10-19.*

- R-05: rejected — Excluded this cycle: lowest-rated risk (4/25); revisit next cycle.

Band column uses the council's response bands (Table 4, p.19): Extreme 15 -25; Medium - High 8-12; Moderate 4 - 6; Low Up to 3. Matrix labels are reported separately. Not used for banding: Figure 4 Risk Escalation, p.21 gives a different Corporate Risk Register entry point ("Score 9 or above"). Scoring-method discrepancies recorded in history.json, not resolved here: DISC-01, DISC-02, DISC-03, DISC-04, DISC-05.

Risk indicators to investigate; no finding of wrongdoing is made.

## Summary

| Risk | Title | L | I | Score | Matrix label | Band | Auditor override | Proposed scope |
|---|---|---|---|---|---|---|---|---|
| R-01 | Payments may cluster just below procurement route boundaries | 3 | 2 | 6 | Moderate | Moderate | no | yes |
| R-02 | Related requirements may not be aggregated for procurement purposes | 3 | 3 | 9 | High | Medium - High | no | yes |
| R-03 | Supplier spend may lack a matching published contract notice | 3 | 3 | 9 | High | Medium - High | no | yes |
| R-04 | Payments may have been made more than once for the same amount and payee | 3 | 3 | 9 | High | Medium - High | no | yes |
| R-06 | Spend may exceed the annual rate of the published award value | 2 | 3 | 6 | Moderate | Moderate | no | yes |
| R-07 | Waivers, exceptions and approvals may not be fully documented | 2 | 3 | 6 | Moderate | Moderate | no | yes |
| R-08 | Provider choice for exempt placements may not be recorded | 2 | 3 | 6 | Moderate | Moderate | no | yes |
| R-09 | A limited-assurance audit of personal budget payments may bear on payment controls | 3 | 3 | 9 | High | Medium - High | no | yes |

## R-01: Payments may cluster just below procurement route boundaries

Payment values observed close to the printed quote and tender boundaries warrant checking that the correct procurement route was followed.

**Likelihood.** Payments flagged near printed value boundaries recur across many payees and every month observed: 369 distinct payments [metric:$.tests.threshold_clustering.count], against the quote requirement [rule:CPR-68]. Most sit at the lowest boundary, where recurring care and grant payments can legitimately repeat. The statutory thresholds are not supplied, so those boundaries are untested. This supports the recurring-indicator level and no higher [history:LIKELIHOOD-3].

**Impact.** A wrong route at the lower value bands would mostly involve modest sums, which fits the minor financial descriptor [history:IMPACT-2]. The route requirement is set by [rule:CPR-68]. Data on actual consequences is not available, and spend is not treated as loss.

**Proposed focus.** Compare flagged payments with the quotation and invitation records for the matching band, and separate recurring placement and grant payments from one-off purchases.

**Evidence.**
- [history:IMPACT-2] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.threshold_clustering.count] 369
- [rule:CPR-68] clause App B row A, p. 12: "At least one quote must be sought from an appropriate source."

## R-02: Related requirements may not be aggregated for procurement purposes

Repeated payments to the same payee within short windows warrant checking whether related requirements were aggregated, as the anti-avoidance rule requires.

**Likelihood.** The test found 176 general-procurement windows [metric:$.tests.split_purchases.count] across several payees and months, which is a recurring indicator [history:LIKELIHOOD-3]. The population covers only payments over the publication floor, so this is a lower bound. Periodic care and education fees can legitimately recur, and these are reported separately. Statutory-threshold windows were not tested because the parameters are null. The governing requirement is [rule:CPR-12].

**Impact.** Disaggregation could mean contracts above a competition boundary were not competed, which fits external agency criticism and a reasonable possibility of legal challenge [history:IMPACT-3] [rule:CPR-12]. No consequence data exists, and the windows are indicators, not proven avoidance.

**Proposed focus.** Sample windows for general-procurement payees and trace each to the underlying requirement, order and approval to see whether one need was bought in parts.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.split_purchases.count] 176
- [rule:CPR-12] clause 6.16, p. 5: "There shall be no artificial splitting or disaggregation of a contract to avoid the application of the provisions of the Procurement Legislation and/or these Rules."

## R-03: Supplier spend may lack a matching published contract notice

Many paid suppliers have no matching published notice, so contract and advertising coverage needs checking against the council's own contract register.

**Likelihood.** Of the 674 suppliers large enough to be classed [metric:$.tests.off_contract.eligible_suppliers], 1,031 supplier names across the spend population had no matching active notice [metric:$.matching.none], so the indicator is widespread. The notice file is a Contracts Finder export and not a contract register. Awards made earlier, awards advertised elsewhere and exempt placements will also show no notice, so this is an indicator to check and not evidence of off-contract spend. The relevant requirements are [rule:CPR-70] and [rule:CPR-07]. The rubric level is recurring indicators across suppliers [history:LIKELIHOOD-3].

**Impact.** Missing notices or an incomplete register could expose the council to criticism on transparency and a reasonable possibility of regulatory interest [history:IMPACT-3] [rule:CPR-70]. The consequence is unknown until the register is compared, and spend totals are not treated as loss.

**Proposed focus.** Obtain the council's contract register and match the unmatched high-value payees to it. Confirm that the contract-notice and register-publication duties have been met.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.matching.none] 1,031
- [metric:$.tests.off_contract.eligible_suppliers] 674
- [rule:CPR-07] clause 5.2.1, p. 3: "A register of contracts, including those in progress and those awarded, with key information such as the contract value, duration and supplier."
- [rule:CPR-70] clause App B row B1, p. 12: "A contract notice must be published on the CDP"

## R-04: Payments may have been made more than once for the same amount and payee

Groups of same-payee, same-amount payments within a short window warrant checking against invoices for possible duplicate payment.

**Likelihood.** 698 groups were found [metric:$.tests.duplicates.count] across many payees and all months observed, which is a recurring indicator [history:LIKELIHOOD-3]. Many groups are care and education placement payments, where several service users can share the same fee. Whether any are duplicates needs invoice-level evidence, which this data does not hold. The relevant control is written evidence of purchases [rule:CPR-32]. A recent accounts payable audit reported reasonable assurance and is not adverse [history:AUD-15].

**Impact.** Confirmed duplicates would mean overpayment and possible external criticism of payment controls [history:IMPACT-3] [rule:CPR-32]. The beyond-first-instance value is an indicator, not a loss, and no recovery or consequence data is available.

**Proposed focus.** Select groups across both timestamp tiers and agree each payment to its invoice, order and goods or service receipt. Establish whether duplicate checks run before payment release.

**Evidence.**
- [history:AUD-15] audit-completed-work-2025-26-q3.pdf; page 1
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.duplicates.count] 698
- [rule:CPR-32] clause 10.1, p. 8: "There should be written evidence of all purchases (which shall include electronic evidence)."

## R-06: Spend may exceed the annual rate of the published award value

Payees whose annualised spend is well above the published award's annual rate warrant checking for undocumented variation or scope growth.

**Likelihood.** Only 8 payees met the eligibility rules and exceeded the ratio [metric:$.tests.spend_vs_award.count], an isolated indicator [history:LIKELIHOOD-2]. Most payees could not be tested because they lacked a single active notice, and award values may be estimates or maxima. Variations need approval under [rule:CPR-79] and [rule:CPR-80].

**Impact.** Unapproved variations could be challenged as breaching the approval and competition rules, which fits the reasonable-possibility-of-challenge descriptor [history:IMPACT-3] [rule:CPR-80]. The statutory threshold that sets the approver is not supplied. No consequence data exists, and the excess is not treated as loss.

**Proposed focus.** For each flagged contract, compare payments to the award and any variation or extension records, and confirm the approver required by the variation rules signed off.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [metric:$.tests.spend_vs_award.count] 8
- [rule:CPR-79] clause App C row E, p. 14: "For contract value below the Threshold prior written approval from the Monitoring Officer and S151 Officer is required."
- [rule:CPR-80] clause App C row E, p. 14: "For contract value greater than the Threshold, approval of the relevant board, following the submission of an extension report to the relevant board with recommendation from Monitoring Officer and S151 Officer"

## R-07: Waivers, exceptions and approvals may not be fully documented

Waiver and exception approvals and their documentation cannot be seen in spend data, and the rules give conflicting waiver authority, so they need testing by enquiry and document review.

**Likelihood.** No metric observes waivers, exception reports or approvals, so this rests on the rules and the gap. The rules require documented waivers [rule:CPR-25] and approval by a named officer [rule:CPR-27]. They are inconsistent on who may waive, since [rule:CPR-20] allows executive discretion while [rule:CPR-21] limits waivers to two officers. This is above the rule-only level because the wording conflict is itself an indicator, and no adverse audit evidence was found [history:LIKELIHOOD-2]. A recent contract letting audit gave reasonable assurance [history:AUD-01].

**Impact.** Undocumented or wrongly authorised waivers could draw external agency criticism and a reasonable possibility of legal challenge [history:IMPACT-3] [rule:CPR-21]. The scale of waiver use is unknown because no waiver register data was supplied.

**Proposed focus.** Request the waiver and exception register and a sample of exception reports. Test authority, advance timing and recorded reasons, and clarify which officer's approval applies.

**Evidence.**
- [history:AUD-01] audit-completed-work-2024-25-annual.pdf; page 1
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [rule:CPR-20] clause 7.2.2, p. 6: "at the discretion of the relevant Executive Director and/or the Chief Executive, acting lawfully, who may proceed in a manner most expedient for the efficient management of the Council with reasons recorded in writing."
- [rule:CPR-21] clause 7.3, p. 6: "Only the Monitoring Officer and/or the S.151 Officer may grant a waiver or an exception to these Rules, subject to exception values and delegation thresholds detailed in these Rules and/or elsewhere in the Constitution. An officer who seeks a waiver of these Rules shall do so only in advance and only in exceptional circumstances."
- [rule:CPR-25] clause 7.5.1, p. 6: "be fully documented;"
- [rule:CPR-27] clause 7.5.3, p. 7: "be subject to approval by the S.151 Officer who shall record they have considered the reasons for the waiver and that they are satisfied that the circumstances justifying the waiver are genuinely exceptional (applications for waivers which are a result of poor contract planning will rarely be considered genuinely exceptional);"

## R-08: Provider choice for exempt placements may not be recorded

Placement spend is exempt from competition on condition that the reasons for the choice of provider are recorded, and the data cannot show whether this was done.

**Likelihood.** This is a rule-only control with no observable metric: the record of provider choice is required by [rule:CPR-81] and sits in case notes outside the spend data. No adverse evidence was found, so the rating is an isolated-indicator level [history:LIKELIHOOD-2]. A recent audit of residential and nursing care purchasing gave reasonable assurance [history:AUD-18].

**Impact.** Placement spend is the largest tagged group in the population, and weak provider-choice records could attract external agency criticism of value for money [history:IMPACT-3] [rule:CPR-81]. Consequence data is not available.

**Proposed focus.** Sample placement payments and check that case notes record the reasons for provider choice, including recurring payments and any provider paid across several services.

**Evidence.**
- [history:AUD-18] audit-completed-work-2025-26-q3.pdf; page 1
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-2] risk-management-strategy-2024-27.pdf; page 15
- [rule:CPR-81] clause App C row F, p. 15: "Service Directors must ensure that a record of the reasons for the choice of provider is maintained on the individual’s case notes."

## R-09: A limited-assurance audit of personal budget payments may bear on payment controls

A recent audit of direct payments gave an adverse opinion and no agreed actions are published, so the status of improvements is unknown.

**Likelihood.** An adverse overall opinion is current evidence of weak controls over a payment stream [history:AUD-16]. No paper lists agreed actions, owners or due dates, so progress cannot be confirmed. This differs from the supplier-payment population tested here and is not claimed as a repeat finding on any theme above. It is rated at the recurring level because adverse assurance exists and follow-up is unseen [history:LIKELIHOOD-3]. The related payment control is [rule:CPR-32].

**Impact.** Adverse assurance on payments to individuals fits external agency criticism of control weakness [history:IMPACT-3] [history:AUD-16]. The consequence is not quantified in the papers, and the population may fall outside the published spend extract.

**Proposed focus.** Ask for the agreed actions and implementation status from that audit and check whether any of the weaknesses apply to supplier payments in scope.

**Evidence.**
- [history:AUD-16] audit-completed-work-2025-26-q3.pdf; page 1
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [history:LIKELIHOOD-3] risk-management-strategy-2024-27.pdf; page 15
- [rule:CPR-32] clause 10.1, p. 8: "There should be written evidence of all purchases (which shall include electronic evidence)."

## Excluded

- EX-01: Statutory-threshold route and notice testing is not rated as a separate risk. The goods and services, works and light touch threshold parameters are null in the rules and no value was invented, so the analytics skipped those tiers. The auditor must supply the figures and sources before this theme can be rated.
- EX-02: Payments to redacted payees, statutory pension payments and inter-authority payments are excluded from the analytics population, so no supplier-level risk can be rated for them. This is a population limitation for the auditor to note.
- R-05: Excluded this cycle: lowest-rated risk (4/25); revisit next cycle.

## Auditor decisions

Recorded decisions:
- R-01: approve — 
- R-02: approve — 
- R-03: approve — 
- R-04: approve — 
- R-05: reject — Excluded this cycle: lowest-rated risk (4/25); revisit next cycle.
- R-06: approve — 
- R-07: approve — 
- R-08: approve — 
- R-09: approve — 
