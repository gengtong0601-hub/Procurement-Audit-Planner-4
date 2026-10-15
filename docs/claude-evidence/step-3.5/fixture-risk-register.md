# Procurement audit risk register

**DRAFT — scope recommendations only; no auditor decisions recorded.**


Band column uses the council's response bands (5.13, Table 4, p.19): Extreme 15 -25; Medium - High 8-12; Moderate 4 - 6; Low Up to 3. Matrix labels are reported separately. Not used for banding: Figure 4. Risk Escalation, p.21 gives a different Corporate Risk Register entry point ("Score 9 or above"). Scoring-method discrepancies recorded in history.json, not resolved here: DIS-01, DIS-02, DIS-03, DIS-04, DIS-05, DIS-06, DIS-07, DIS-08, DIS-09, DIS-10, DIS-11, DIS-12.

Risk indicators to investigate; no finding of wrongdoing is made.

## Summary

| Risk | Title | L | I | Score | Matrix label | Band | Auditor override | Proposed scope |
|---|---|---|---|---|---|---|---|---|
| R-01 | Related requirements may not have been aggregated | 3 | 3 | 9 | High | Medium - High | no | yes |

## R-01: Related requirements may not have been aggregated

Recurring payments within a window warrant an aggregation review.

**Likelihood.** 64 general-procurement windows recur under the no-splitting rule [metric:$.tests.split_purchases.tiers[1].by_tag.general_procurement.rows] [rule:CPR-12].

**Impact.** A missed route fits the council's Medium descriptor [history:IMPACT-3] [rule:CPR-69].

**Proposed focus.** Confirm which payments belong to one requirement.

**Evidence.**
- [history:IMPACT-3] risk-management-strategy-2024-27.pdf; page 14
- [metric:$.tests.split_purchases.tiers[1].by_tag.general_procurement.rows] 64
- [rule:CPR-12] clause 6.16, p. 5: "There shall be no artificial splitting or disaggregation of a contract to avoid the application of the provisions of the Procurement Legislation and/or these Rules."
- [rule:CPR-69] clause App B row B1, p. 12: "Invitations to quote must be sent via the Procurement Portal to at least three appropriate sources, including at least one SME* or VCSE* organisation and one local supplier ****(where appropriate and possible**)."

## Excluded

- Validation: R-02: likelihood: requires at least one resolved citation
- Validation: R-02: impact: unresolved citation [history:IMPACT-9]
- Validation: R-02: impact: unresolved citation [rule:CPR-999]
- Validation: R-02: impact: requires at least one resolved citation

## Auditor decisions

No decisions recorded; the auditor must complete auditor-comments.md.

**VALIDATION BLOCKED — not ready for approval or planning.**
