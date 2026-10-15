# Challenges to the audit planning pack

**Packs reviewed:**

| Version | Controls | Tests | Sampled transactions | Other |
|---|---|---|---|---|
| v1 | 10 | 12 | 139 | |
| v2 | 11 | 14 | 158 | |
| v3 | 11 | 15 | 172 | 36/82 rules cited, 0 warnings, 0 failures; `PLANNER DONE v3` |

**Date:** 2026-10-15

**Rounds:** round one, 8 challenges; round two, 4 challenges. Both rounds are answered and every row is closed: 10 resolved, 0 declined, 2 for the auditor, 0 open.

**Messaging:** relay mode. The lead forwarded each message word for word because SendMessage was not available to teammates in this session. The auditor approved this workaround.

I compared each pack with the approved register (revision 1, with Tony's decisions), `analytics.json`, `history.json` and `rules.json`. I checked three things:
- whether each sample recipe reaches the population the risk's metric describes;
- whether each pass criterion can detect the pattern the risk names;
- whether each "not tested" reason holds up against the pack's own steps.

After each rebuild, I confirmed every accepted change in `audit-plan.json`, the memo and the drawn samples in `audit-program.md`. I also checked for new gaps. #9 came from that check.

On the planner's first-look points:
- Accepted without challenge: point 3 (CPR-68 and CPR-81 counted but not tested, which the memo states) and point 4 (one payment shared by T-04.1 and T-06.1). In v3 a second payment is shared, by T-04.1 and T-08.1. I accept it on the same ground: the tests ask different questions of one invoice.

The cap of four in round two meant some points were considered but not raised:
- The R-04 impact rating. The value beyond the first payment (£297,355.44) sits in the council's Medium band, but the register reasons that duplicates are recoverable.
- The T-03.4 order. It draws largest-first, so it covers the top of its band.

Every challenge concerns the plan. None asserts anything about the council or any supplier.

| # | Type | Risk | Challenge | Evidence | Ask | Response | Status |
|---|---|---|---|---|---|---|---|
| 1 | sample | R-03 | T-03.1 drew only the 10 largest unmatched suppliers. All are above £500,000, so the £25,000 to £500,000 band, where the quotation and notice rules apply, was untested. | T-03.1 recipe; metric:$.tests.off_contract.headline.count (191); metric:$.tests.off_contract.headline.top20[10].annualised_estimate_gbp (645,662.36); metric:$.tests.high_value_suppliers.tiers[2].headline.count (21); $.contracts.caveat; rule:CPR-69, rule:CPR-70, rule:CPR-72 | Add a second stratum of 10 from £25,000 up to £500,000, and run T-03.2 and T-07.3 on both strata. | "accepted. Added T-03.4 under C-03.1 … a second stratum of 10 unmatched suppliers, from the notice threshold up to the Key Decision value." Verified in v2 and v3: T-03.4 draws 10 suppliers (23 transactions). | resolved |
| 2 | test | R-06 | T-06.1 compared the period's payments with a multi-year award, so it could not fail. The top flag's period spend of £314,383.57 is below its £615,540.00 award, although the ratio is 6.13. | T-06.1 step; metric:$.tests.spend_vs_award.top20[0].total_gbp, .awarded_value_gbp, .ratio; rule:CPR-79, rule:CPR-80 | Compare cumulative spend since contract start with the award; add the ledger to the PBC list. | "accepted. T-06.1 now gets the supplier ledger from contract start to the end of the spend period and compares cumulative spend with the award value." Verified: the step, the pass criterion and the PBC list all reflect this. | resolved |
| 3 | coverage | R-03 | CPR-28 and CPR-77 were marked "not tested" although T-03.1 and T-03.2 identify call-offs and accept them as cover, with no pass or fail. | v1 rules_not_tested; T-03.2 step; rule:CPR-28, rule:CPR-77 | Put both rules under a control, give call-offs a pass or fail, and take both off the not-tested list. | "accepted. New control C-03.3 (CPR-28, CPR-77) and new test T-03.5." Verified: C-03.3 and T-03.5 exist with a pass criterion, and coverage is 36/82. | resolved |
| 4 | sample | R-03 | The tag filter dropped the only agency_staff supplier: unmatched, with an annualised estimate of £5,102,208.60, and no stated reason. | metric:$.tests.off_contract.unmatched_by_tag.agency_staff; T-03.1 `where`; rule:CPR-70, rule:CPR-04 | Include agency_staff, or state the reason. | "accepted. T-03.1, T-03.4 and T-08.1 now take dominant_tag general_procurement or agency_staff." Verified: the supplier is drawn in T-03.1, and the memo limitation covers the tags not sampled. | resolved |
| 5 | scope | R-09 | Placement-tagged spend is the largest tag and rests on a service-and-narrative proxy. CPR-81 exempts only individually chosen placements, and AUD-16 has a Limited opinion. The memo states "Placement spend is exempt from competition" as fact. | metric:$.population.tags.care_or_education_placement.gbp (30,571,711.30); metric:$.tests.off_contract.unmatched_by_tag.care_or_education_placement.suppliers (304); metric:$.tests.split_purchases.tiers[1].placements.windows (178); rule:CPR-81; history:AUD-16 | Auditor: decide whether a small R-09 verification sample comes into scope. Memo: use proxy wording. | "for the auditor. You typed this point as scope, so … I have left the plan as it is, including the memo sentence. If the auditor wants your proxy wording, it is a one-line change." | for the auditor |
| 6 | sample | R-03 | The public-body filter removed payees the analytics kept as procurement ("Private Contractors" narrative), so the memo's "consistent with" sentence was wrong. | $.population.exclusion_regexes.inter_authority_unless_narrative; metric:$.tests.off_contract.headline.top20[7], top20[12]; rule:CPR-75 | Remove `where_not_match`, or test public-body payees under T-07.3; correct the memo. | "accepted. Removed where_not_match from T-03.1, T-08.1 and T-02.1 … I deleted the incorrect memo sentence." Verified: public-body payees are now drawn in T-03.1, T-03.4 and T-03.6. | resolved |
| 7 | sample | R-08 | T-08.1 excluded T-06.1 suppliers but did not test their award decisions, and n = 5 from a population of 21. | T-08.1 `exclude_drawn_in` and step; metric:$.tests.spend_vs_award.top20[0].awarded_value_gbp; metric:$.tests.high_value_suppliers.tiers[2].headline.count | Add those T-06.1 suppliers to the step, and draw all remaining suppliers. | "step change accepted; sample-size change declined … n stays at 5 because the skill sets sample size by score." Step verified. I accept the reason for keeping n at 5, and the remaining gap was closed by #9. | resolved |
| 8 | test | R-02 | T-02.1 skipped T-03.1 and T-05.1 suppliers whose windows at the three-quote threshold neither test covered. | T-02.1, T-03.1 and T-05.1 steps; metric:$.tests.split_purchases.tiers[1].headline.windows (64); rule:CPR-12 | Add the window check, or drop the exclusion. | "accepted. T-03.1, T-03.4, T-05.1 and T-06.1 now each confirm that the contract also covers the supplier's windows flagged by the aggregation test." Verified, and T-03.6 does the same. | resolved |
| 9 | sample | R-03 | In v2, unmatched suppliers above the Key Decision value that ranked below T-03.1's top 10 fell between the strata. Three were sampled nowhere, and one appeared only in T-02.1. | metric:$.tests.off_contract.headline.top20[10]–[13], all match_class none; T-03.1 n 10; T-03.4 where_max 500000; rule:CPR-04, rule:CPR-70 | Draw every unmatched supplier above £500,000. | "accepted. … Added T-03.6 under C-03.1 … all 5 available are drawn. With T-03.1 and T-03.6 together, every unmatched supplier in that band is now sampled." Verified in v3: T-03.6 draws all 5 ("only 5 available"); T-03.2, T-03.5, T-07.3 and T-08.1 cover T-03.6; T-08.1 and T-02.1 skip it. | resolved |
| 10 | test | R-06, R-07, R-08 | The pass criteria in T-06.1, T-07.3 and T-08.1 depend on the Threshold, which is null, and no PBC item asked the council for it. | rule:CPR-64, rule:CPR-65, rule:CPR-79, rule:CPR-80, rule:CPR-82; $.skipped[3]; v2 steps and PBC list | Add a PBC item for the Threshold. Conclude level checks only once it is confirmed; otherwise record them as not concluded. Widen the memo limitation. | "accepted. T-02.1, T-03.2, T-06.1, T-07.1, T-07.3 and T-08.1 now conclude a check that depends on the Threshold only once the council confirms the figure it applied." Verified: all six steps carry the clause and a PBC item, and the memo limitation names all six. | resolved |
| 11 | rating | R-08 | R-08 likelihood is 1 (Rare) because "no metric observes approvals". Yet unmatched top-20 entries [0] to [13] are all general-procurement suppliers above £500,000 with no published award notice, against 21 such suppliers in total. | metric:$.tests.off_contract.headline.top20[0]–[13]; metric:$.tests.high_value_suppliers.tiers[2].headline.count (21); rule:CPR-04; history:LIKELIHOOD-1 | Auditor: decide whether R-08 likelihood should reflect this signal. | "for the auditor. This is a rating point, so I have made no plan change. Noted: if the auditor raises R-08 to a score of 9 or more, T-08.1 goes to 10 items under the sizing rule." | for the auditor |
| 12 | coverage | R-06 | The memo did not carry the register's statement that 1,050 suppliers lack a unique active notice and so cannot be tested for spend versus award. | metric:$.tests.spend_vs_award.excluded.no_unique_active_notice (1,050); register R-06 Likelihood | Add that limitation to the memo. | "accepted. A new sentence in the memo limitations says the spend-versus-award test covers only suppliers matched to exactly one active single-supplier notice with a positive award." Verified: the v3 memo renders 1,050 with the metric citation. | resolved |

## For the auditor at sign-off

- **#5 (scope, R-09):** decide whether a small verification sample of placement-tagged suppliers comes into scope. Also decide whether the memo should keep "Placement spend is exempt from competition" or change to the proxy wording, which the planner calls a one-line change.
- **#11 (rating, R-08):** decide whether R-08 likelihood should reflect the signal that most general-procurement suppliers above £500,000 match no published award. A score of 9 or more would raise T-08.1 to 10 items.

**Noted after round two (not sent, because the round cap was reached):** v3 cut the memo limitations to fit the word budget, and two register caveats that v2 carried were dropped:
- "several spend-versus-award flags rest on one or two payments" (register R-06);
- "some publication years are thin" (register R-03; `$.contracts.thin_years`).

The auditor may wish to have them restored.
