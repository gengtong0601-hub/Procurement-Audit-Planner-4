# Audit program

*Generated 2026-10-15 by `build_pack.py` from `audit-plan.json`, `risk-register.md` (revision 1), `auditor-comments.md` by Tony dated 2026-10-15, `rules.json` and `analytics.json`. Status: DRAFT for challenge, QA review and auditor sign-off.*

**Indicators, not findings.** Every test below checks a control against a pattern in public data. Nothing here asserts wrongdoing by the council, a department, an officer or a supplier.

7 risks in scope, 11 controls, 15 tests, 172 sampled transactions. Samples are drawn by the builder from `analytics-full/` by the recipe stated under each test, and every transaction is listed with its workbook row.


## R-05: Spend may continue after a published contract term without an approved extension [4 (Moderate; Moderate)]

**Audit objective.** Conclude whether payments to suppliers whose published notices had all ended were made under an approved extension or a newer recorded contract.

**C-05.1. Expected control.** Each extension of an existing contract is approved by the S151 Officer, and any replacement contract is notified for recording on the Council Contract Register. [CPR-78, CPR-35] Owner: S151 Officer (extension); relevant Service Director (register notification).

**T-05.1. Test.** For each sampled supplier, obtain the contract covering the payment dates: the extension and its S151 approval, or the newer award and its register entry. Pass: an approved extension or a recorded newer contract covers the sampled payments and any of the supplier's windows flagged by the aggregation test. [CPR-78, CPR-35, metric:$.tests.expired_notice_spend.count, metric:$.tests.split_purchases.tiers[1].headline.windows]  
**Evidence to inspect:** Extension approval by the S151 Officer, newer contract and register entry, invoices for the sampled payments  
**Sample:** 5 items from `expired-notice-spend.csv`, where dominant_tag = general_procurement, largest total_gbp first, 3 payments per supplier; 9 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P03_-_published.xlsx:704` | 2026-06-16 | Hope & Clay (Construction) Ltd | £91,306.75 | Environment |
| 2 | `Over500_2026_P03_-_published.xlsx:58` | 2026-06-03 | BERKSHIRE MECHANICAL SERVICES | £8,250.00 | Development & Housing |
| 2 | `Over500_2026_P03_-_published.xlsx:42` | 2026-06-03 | BERKSHIRE MECHANICAL SERVICES | £6,250.00 | Development & Housing |
| 2 | `Over500_2026_P03_-_published.xlsx:279` | 2026-06-09 | BERKSHIRE MECHANICAL SERVICES | £5,585.00 | Development & Housing |
| 3 | `Over500_2026_P02_-_published.xlsx:467` | 2026-05-08 | G7 BUSINESS SOLUTIONS LIMITED | £5,469.78 | Finance, Property & Procurement |
| 3 | `Over500_2026_P03_-_published.xlsx:531` | 2026-06-10 | G7 BUSINESS SOLUTIONS LIMITED | £5,469.78 | Finance, Property & Procurement |
| 3 | `Over500_2026_P03_-_published.xlsx:721` | 2026-06-10 | G7 BUSINESS SOLUTIONS LIMITED | £1,365.00 | Finance, Property & Procurement |
| 4 | `Over500_2026_P02_-_published.xlsx:459` | 2026-05-15 | CACI Limited | £12,071.67 | Children's Social Care |
| 5 | `Over500_2026_P03_-_published.xlsx:686` | 2026-06-22 | Morton Pattison Ltd | £1,102.00 | Environment |


## R-06: Spend may exceed the awarded contract value without an approved variation [6 (Moderate; Moderate)]

**Audit objective.** Conclude whether spend running above the annual rate of a supplier's single published award is within the award's value and scope or covered by an approved variation.

**C-06.1. Expected control.** Variations of an existing contract carry the approval the Rules require: prior written approval by the Monitoring Officer and S151 Officer below the Threshold, and relevant board approval on a report with their recommendation above it. [CPR-79, CPR-80] Owner: Monitoring Officer and S151 Officer; relevant board above the Threshold.

**T-06.1. Test.** For each sampled supplier, obtain the supplier ledger from the contract start date to the end of the spend period and compare cumulative spend under the contract with the award value; confirm whether the published award value is an estimate or a maximum and that the payments, including any windows flagged by the aggregation test, fall within the award's scope. Where cumulative spend exceeds the award or falls outside its scope, obtain the variation and its approval. Pass: cumulative spend sits within the award, or within a variation approved at the level its value requires. Where cumulative spend is within the award but the current rate of spend would exhaust it before the term ends, record this for the auditor. Where the check depends on the Threshold, conclude it only once the council confirms the figure applied in the period; otherwise record it as not concluded. [CPR-79, CPR-80, metric:$.tests.spend_vs_award.count, metric:$.tests.spend_vs_award.parameters.ratio_min]  
**Evidence to inspect:** Supplier ledger since contract start, contract and award notice, basis of the award value, variation records and approvals, invoices for the sampled payments  
**Sample:** 5 items from `spend-vs-award.csv`, where dominant_tag = general_procurement, largest total_gbp first, 3 payments per supplier; 10 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:905` | 2026-07-22 | NEC SOFTWARE SOLUTIONS UK LIMITED | £129,125.00 | Finance, Property & Procurement |
| 1 | `Over500_2026_P04_-_published.xlsx:492` | 2026-07-22 | NEC SOFTWARE SOLUTIONS UK LIMITED | £91,629.15 | Finance, Property & Procurement |
| 1 | `Over500_2026_P04_-_published.xlsx:487` | 2026-07-22 | NEC SOFTWARE SOLUTIONS UK LIMITED | £52,054.00 | Finance, Property & Procurement |
| 2 | `Over500_2026_P03_-_published.xlsx:2130` | 2026-06-09 | TWO SAINTS LTD | £38,775.00 | Development & Housing |
| 2 | `Over500_2026_P04_-_published.xlsx:3181` | 2026-07-22 | TWO SAINTS LTD | £38,775.00 | Development & Housing |
| 2 | `Over500_2026_P02_-_published.xlsx:2160` | 2026-05-12 | TWO SAINTS LTD | £27,147.69 | Development & Housing |
| 3 | `Over500_2026_P04_-_published.xlsx:1276` | 2026-07-22 | WCL UK Ltd (Trading as Everything ICT) | £102,882.78 | Education & SEND |
| 4 | `Over500_2026_P03_-_published.xlsx:371` | 2026-06-08 | IDOX SOFTWARE LTD | £48,579.20 | Community Services |
| 4 | `Over500_2026_P02_-_published.xlsx:462` | 2026-05-20 | IDOX SOFTWARE LTD | £2,647.21 | Development & Housing |
| 5 | `Over500_2026_P03_-_published.xlsx:396` | 2026-06-10 | BookingLab Limited | £24,000.00 | Transformation, Customer & ICT |


## R-03: High-value recurring spend may lack a published or recorded contract award [12 (High; Medium - High)]

**Audit objective.** Conclude whether high-value recurring general-procurement spend with suppliers that match no published award is covered by a contract recorded on the Contract Register and let by the route the Rules require.

**C-03.1. Expected control.** Every contract award is notified by the relevant Service Director for recording on the Council Contract Register, and the register of contracts in progress and awarded is published with value, duration and supplier. [CPR-35, CPR-07] Owner: Relevant Service Director (notification); Service Lead for Commissioning and Procurement (register).

**T-03.1. Test.** Request the council's contract register. For each sampled supplier, locate the register entry and the contract, and record its term, value and scope. Pass: a contract on the register covers the sampled payments and their dates. Where the supplier also has payment windows flagged by the aggregation test, at the three-quote threshold or the Key Decision value, confirm the contract covers those payments too. Where no contract is found, record what the council provides instead: a framework call-off goes to T-03.5, a waiver or exemption to T-07.3. [CPR-35, CPR-07, metric:$.tests.off_contract.headline.count, metric:$.tests.split_purchases.tiers[2].headline.windows, metric:$.tests.split_purchases.tiers[1].headline.windows, metric:$.tests.off_contract.unmatched_by_tag.agency_staff.suppliers]  
**Evidence to inspect:** Contract register extract, signed contract or call-off, award notification to Procurement, invoices for the sampled payments  
**Sample:** 10 items from `off-contract-unmatched.csv`, where dominant_tag = ['general_procurement', 'agency_staff'], match_class = none, annualised_estimate_gbp ≥ 25000, largest annualised_estimate_gbp first, 3 payments per supplier, excluding suppliers and rows already drawn in T-05.1, T-06.1; 28 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:793` | 2026-07-13 | VolkerHighways Ltd | £998,987.64 | Environment |
| 1 | `Over500_2026_P04_-_published.xlsx:603` | 2026-07-28 | VolkerHighways Ltd | £855,750.25 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:684` | 2026-06-22 | VolkerHighways Ltd | £366,872.38 | Environment |
| 2 | `Over500_2026_P02_-_published.xlsx:2196` | 2026-05-27 | VEOLIA ES WEST BERKSHIRE LTD (CHAPS ONLY) | £2,201,856.40 | Environment |
| 2 | `Over500_2026_P03_-_published.xlsx:2146` | 2026-06-29 | VEOLIA ES WEST BERKSHIRE LTD (CHAPS ONLY) | £2,180,425.32 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3194` | 2026-07-27 | VEOLIA ES WEST BERKSHIRE LTD (CHAPS ONLY) | £1,803,783.32 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:2144` | 2026-06-25 | Millbrook Healthcare Limited | £1,141,918.00 | Finance, Property & Procurement |
| 3 | `Over500_2026_P03_-_published.xlsx:2216` | 2026-06-03 | Millbrook Healthcare Limited | £1,141,918.00 | Finance, Property & Procurement |
| 3 | `Over500_2026_P04_-_published.xlsx:3789` | 2026-07-29 | Millbrook Healthcare Limited | £1,141,918.00 | Finance, Property & Procurement |
| 4 | `Over500_2026_P03_-_published.xlsx:9` | 2026-06-15 | Comensura Ltd | £107,880.99 | Strategy & Governance |
| 4 | `Over500_2026_P02_-_published.xlsx:5` | 2026-05-12 | Comensura Ltd | £104,728.31 | Strategy & Governance |
| 4 | `Over500_2026_P04_-_published.xlsx:19` | 2026-07-31 | Comensura Ltd | £103,047.79 | Strategy & Governance |
| 5 | `Over500_2026_P02_-_published.xlsx:665` | 2026-05-15 | The Better Group Ltd | £64,500.00 | Adult Social Care |
| 5 | `Over500_2026_P02_-_published.xlsx:666` | 2026-05-15 | The Better Group Ltd | £58,833.00 | Adult Social Care |
| 5 | `Over500_2026_P03_-_published.xlsx:670` | 2026-06-01 | The Better Group Ltd | £48,784.37 | Adult Social Care |
| 6 | `Over500_2026_P02_-_published.xlsx:473` | 2026-05-27 | SoftwareONE UK Ltd | £375,697.68 | Transformation, Customer & ICT |
| 6 | `Over500_2026_P02_-_published.xlsx:474` | 2026-05-27 | SoftwareONE UK Ltd | £85,871.04 | Transformation, Customer & ICT |
| 6 | `Over500_2026_P02_-_published.xlsx:653` | 2026-05-27 | SoftwareONE UK Ltd | £59,650.56 | Transformation, Customer & ICT |
| 7 | `Over500_2026_P02_-_published.xlsx:2200` | 2026-05-13 | Livity Life Ltd | £135,591.03 | Finance, Property & Procurement |
| 7 | `Over500_2026_P03_-_published.xlsx:3087` | 2026-06-17 | Livity Life Ltd | £127,886.78 | Finance, Property & Procurement |
| 7 | `Over500_2026_P04_-_published.xlsx:3310` | 2026-07-13 | Livity Life Ltd | £50,961.45 | Finance, Property & Procurement |
| 8 | `Over500_2026_P04_-_published.xlsx:784` | 2026-07-10 | E W BEARD LTD | £64,202.50 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:674` | 2026-05-20 | E W BEARD LTD | £60,039.70 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:675` | 2026-05-20 | E W BEARD LTD | £55,594.00 | Education & SEND |
| 9 | `Over500_2026_P02_-_published.xlsx:2198` | 2026-05-13 | SLOUGH BOROUGH COUNCIL | £296,177.15 | Finance, Property & Procurement |
| 10 | `Over500_2026_P03_-_published.xlsx:183` | 2026-06-03 | Sikandar Hayat t/a Prompt Cars | £73,296.50 | Education & SEND |
| 10 | `Over500_2026_P03_-_published.xlsx:203` | 2026-06-03 | Sikandar Hayat t/a Prompt Cars | £26,085.00 | Education & SEND |
| 10 | `Over500_2026_P03_-_published.xlsx:208` | 2026-06-03 | Sikandar Hayat t/a Prompt Cars | £17,607.50 | Education & SEND |

**T-03.6. Test.** Apply the T-03.1 step to the unmatched suppliers above the Key Decision value that T-03.1 did not draw, so that no supplier in that band falls between the strata. Locate the register entry and the contract, record its term, value and scope, and confirm it covers the sampled payments and any of the supplier's windows flagged by the aggregation test. Pass: a contract on the register covers them. Where no contract is found, a framework call-off goes to T-03.5, a waiver or exemption to T-07.3. [CPR-35, CPR-07, CPR-04, metric:$.tests.off_contract.headline.count, metric:$.tests.high_value_suppliers.tiers[2].headline.count, metric:$.tests.split_purchases.tiers[1].headline.windows]  
**Evidence to inspect:** Contract register extract, signed contract or call-off, award notification to Procurement, invoices for the sampled payments  
**Sample:** 5 items from `off-contract-unmatched.csv`, where dominant_tag = ['general_procurement', 'agency_staff'], match_class = none, annualised_estimate_gbp ≥ 500000, largest annualised_estimate_gbp first, 3 payments per supplier, excluding suppliers and rows already drawn in T-05.1, T-06.1, T-03.1, (only 5 available); 13 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P03_-_published.xlsx:661` | 2026-06-08 | ANDY AND ES LIMITED | £59,335.72 | Education & SEND |
| 1 | `Over500_2026_P04_-_published.xlsx:1283` | 2026-07-15 | ANDY AND ES LIMITED | £56,941.82 | Education & SEND |
| 1 | `Over500_2026_P02_-_published.xlsx:670` | 2026-05-13 | ANDY AND ES LIMITED | £54,881.31 | Education & SEND |
| 2 | `Over500_2026_P02_-_published.xlsx:530` | 2026-05-27 | Elior UK PLC | £23,694.03 | Adult Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:440` | 2026-06-16 | Elior UK PLC | £23,516.69 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:533` | 2026-07-28 | Elior UK PLC | £23,173.08 | Adult Social Care |
| 3 | `Over500_2026_P04_-_published.xlsx:589` | 2026-07-16 | BBOWT | £118,027.50 | Environment |
| 3 | `Over500_2026_P04_-_published.xlsx:623` | 2026-07-16 | BBOWT | £25,000.00 | Environment |
| 3 | `Over500_2026_P02_-_published.xlsx:641` | 2026-05-21 | BBOWT | £1,289.93 | Environment |
| 4 | `Over500_2026_P03_-_published.xlsx:2217` | 2026-06-10 | BRACKNELL FOREST BOROUGH CNCL | £130,310.57 | Finance, Property & Procurement |
| 5 | `Over500_2026_P02_-_published.xlsx:738` | 2026-05-20 | ANCHOR PIPEWORK LIMITED | £33,148.00 | Finance, Property & Procurement |
| 5 | `Over500_2026_P03_-_published.xlsx:2406` | 2026-06-18 | ANCHOR PIPEWORK LIMITED | £33,148.00 | Finance, Property & Procurement |
| 5 | `Over500_2026_P02_-_published.xlsx:23` | 2026-05-29 | ANCHOR PIPEWORK LIMITED | £10,111.05 | Adult Social Care |

**T-03.4. Test.** Apply the T-03.1 step to a second stratum: unmatched suppliers whose annualised estimate sits from the notice threshold up to the Key Decision value, where the quotation and notice rules apply directly. Locate the register entry and the contract, record its term, value and scope, and confirm it covers the sampled payments and any of the supplier's windows flagged by the aggregation test. Pass: a contract on the register covers them. Where no contract is found, a framework call-off goes to T-03.5, a waiver or exemption to T-07.3. [CPR-35, CPR-07, CPR-70, CPR-72, metric:$.tests.off_contract.headline.count, metric:$.tests.split_purchases.tiers[1].headline.windows]  
**Evidence to inspect:** Contract register extract, signed contract or call-off, award notification to Procurement, invoices for the sampled payments  
**Sample:** 10 items from `off-contract-unmatched.csv`, where dominant_tag = ['general_procurement', 'agency_staff'], match_class = none, annualised_estimate_gbp ≥ 25000, annualised_estimate_gbp ≤ 500000, largest annualised_estimate_gbp first, 3 payments per supplier, excluding suppliers and rows already drawn in T-05.1, T-06.1, T-03.1; 23 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P03_-_published.xlsx:2143` | 2026-06-23 | WOKINGHAM BOROUGH COUNCIL | £95,104.51 | Finance, Property & Procurement |
| 1 | `Over500_2026_P02_-_published.xlsx:2201` | 2026-05-15 | WOKINGHAM BOROUGH COUNCIL | £24,416.73 | Finance, Property & Procurement |
| 2 | `Over500_2026_P03_-_published.xlsx:479` | 2026-06-29 | KPMG | £76,405.00 | Executive Director - Resources |
| 2 | `Over500_2026_P02_-_published.xlsx:655` | 2026-05-19 | KPMG | £34,250.00 | Finance, Property & Procurement |
| 2 | `Over500_2026_P02_-_published.xlsx:568` | 2026-05-29 | KPMG | £8,500.00 | Executive Director - Resources |
| 3 | `Over500_2026_P03_-_published.xlsx:730` | 2026-06-23 | SCOTTISH & SOUTHERN | £101,258.24 | Environment |
| 3 | `Over500_2026_P04_-_published.xlsx:1282` | 2026-07-03 | SCOTTISH & SOUTHERN | £9,502.74 | Education & SEND |
| 4 | `Over500_2026_P02_-_published.xlsx:478` | 2026-05-20 | Education Software Solutions Limited | £95,536.35 | Transformation, Customer & ICT |
| 4 | `Over500_2026_P02_-_published.xlsx:479` | 2026-05-20 | Education Software Solutions Limited | £14,794.00 | Transformation, Customer & ICT |
| 5 | `Over500_2026_P02_-_published.xlsx:178` | 2026-05-27 | Continental Landscapes Ltd | £67,604.74 | Environment |
| 5 | `Over500_2026_P02_-_published.xlsx:198` | 2026-05-27 | Continental Landscapes Ltd | £12,437.95 | Environment |
| 5 | `Over500_2026_P02_-_published.xlsx:180` | 2026-05-27 | Continental Landscapes Ltd | £12,396.75 | Environment |
| 6 | `Over500_2026_P03_-_published.xlsx:2001` | 2026-06-10 | MAISHA STAFFING SOLUTIONS LTD | £18,130.25 | Children's Social Care |
| 6 | `Over500_2026_P04_-_published.xlsx:3716` | 2026-07-29 | MAISHA STAFFING SOLUTIONS LTD | £11,100.00 | Children's Social Care |
| 6 | `Over500_2026_P04_-_published.xlsx:3897` | 2026-07-30 | MAISHA STAFFING SOLUTIONS LTD | £8,900.00 | Children's Social Care |
| 7 | `Over500_2026_P03_-_published.xlsx:2148` | 2026-06-12 | Bloom Procurement Services Ltd | £100,210.53 | Transformation, Customer & ICT |
| 8 | `Over500_2026_P02_-_published.xlsx:2197` | 2026-05-13 | ROYAL BOROUGH OF WINDSOR & MAIDENHEAD | £96,245.28 | Finance, Property & Procurement |
| 9 | `Over500_2026_P03_-_published.xlsx:688` | 2026-06-01 | R&A Haines Building Contractors | £20,332.89 | Development & Housing |
| 9 | `Over500_2026_P03_-_published.xlsx:742` | 2026-06-30 | R&A Haines Building Contractors | £18,707.55 | Development & Housing |
| 9 | `Over500_2026_P03_-_published.xlsx:740` | 2026-06-30 | R&A Haines Building Contractors | £16,600.00 | Development & Housing |
| 10 | `Over500_2026_P02_-_published.xlsx:2192` | 2026-05-21 | ARDENT | £11,692.50 | Environment |
| 10 | `Over500_2026_P03_-_published.xlsx:696` | 2026-06-16 | ARDENT | £11,188.00 | Environment |
| 10 | `Over500_2026_P04_-_published.xlsx:3189` | 2026-07-02 | ARDENT | £10,713.75 | Environment |

**T-03.3. Test.** For each sampled near match, compare the spend supplier with the candidate notice supplier by name, Companies House number and notice. Pass: the notice is confirmed as the same entity and covers the payments. Otherwise treat the supplier as unmatched and apply T-03.1. [CPR-35, CPR-70, metric:$.tests.off_contract.by_match_class.near_contain.count, metric:$.tests.off_contract.by_match_class.near_ratio.count]  
**Evidence to inspect:** Candidate notice, Companies House record, contract register entry  
**Sample:** 6 items from `near-matches.csv`, where dominant_tag = general_procurement, annualised_estimate_gbp ≥ 25000, largest annualised_estimate_gbp first, 1 payments per supplier, (only 6 available); 6 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P02_-_published.xlsx:173` | 2026-05-26 | Glen Cleaning Company Ltd | £5,829.96 | Finance, Property & Procurement |
| 2 | `Over500_2026_P04_-_published.xlsx:247` | 2026-07-09 | BAILEYS OF NEWBURY | £6,592.17 | Education & SEND |
| 3 | `Over500_2026_P04_-_published.xlsx:278` | 2026-07-14 | D J TRAVEL | £7,035.00 | Adult Social Care |
| 4 | `Over500_2026_P04_-_published.xlsx:178` | 2026-07-08 | S RICHARDS T/AS K RICKETTS & S RICHARDS TAXIS | £2,898.00 | Education & SEND |
| 5 | `Over500_2026_P04_-_published.xlsx:232` | 2026-07-10 | Kennet & Avon Group | £2,970.00 | Education & SEND |
| 6 | `Over500_2026_P04_-_published.xlsx:297` | 2026-07-08 | POTTINGER'S HIRE SERVICE | £1,981.67 | Education & SEND |

**C-03.2. Expected control.** Contracts at or above the three-quote threshold are let after invitations to quote through the Procurement Portal and a published contract notice; works contracts above the Key Decision value are let after a full competitive tender. [CPR-69, CPR-70, CPR-71, CPR-72, CPR-73]

**T-03.2. Test.** For each T-03.1, T-03.6 or T-03.4 supplier whose contract is found, confirm the route against the contract value: Procurement Portal invitations to quote and the published contract notice at or above the three-quote threshold, or the full tender record for works above the Key Decision value. Pass: the route matches the contract value. A framework call-off goes to T-03.5; a waiver or exemption goes to T-07.3. Where the check depends on the Threshold, conclude it only once the council confirms the figure applied in the period; otherwise record it as not concluded. [CPR-69, CPR-70, CPR-71, CPR-72, CPR-73, metric:$.tests.off_contract.headline.count]  
**Evidence to inspect:** Procurement Portal invitation and response records, contract notice, tender report, framework call-off record  
**Sample:** Uses the suppliers sampled in T-03.1, T-03.6 and T-03.4; no further transactions are drawn.

**C-03.3. Expected control.** A purchasing scheme (framework, dynamic purchasing system or similar) is used only after advice confirming the council may use it and the purchases fall within it, and a direct award under a scheme without further competition has prior written Monitoring Officer approval and, where applicable, prior board approval. [CPR-28, CPR-77] Owner: Officer responsible for the procurement (advice); Monitoring Officer (direct award approval).

**T-03.5. Test.** For each T-03.1, T-03.6 or T-03.4 supplier that the council says is covered by a framework or other purchasing scheme, obtain the scheme, the call-off and the advice sought before use, and for a direct award without further competition the prior written Monitoring Officer approval and any board approval. Pass: advice predates first use, the purchases fall within the scheme, and a direct award carries the prior approvals. Otherwise record the call-off as not supported. [CPR-28, CPR-77, metric:$.tests.off_contract.headline.count]  
**Evidence to inspect:** Framework or scheme agreement, call-off or order form, pre-use advice, Monitoring Officer approval, board approval  
**Sample:** Uses the suppliers sampled in T-03.1, T-03.6 and T-03.4 that the council says are covered by a purchasing scheme.


## R-08: Higher-value awards may not carry the decision and approval the rules require [4 (Moderate; Moderate)]

**Audit objective.** Conclude whether contracts with high-value general-procurement suppliers were awarded with the decision and approvals their total value requires.

**C-08.1. Expected control.** Every contract is authorised by a decision at the level its total value requires: Service Director delegation up to the Threshold, a board-approved report below the Key Decision value, a Key Decision with a board-approved report under the Call-In and Forward Plan rules above it, and Executive approval at the top band. For contracts let under the Procurement Legislation a written award report is produced and kept for three years. [CPR-02, CPR-64, CPR-65, CPR-04, CPR-66, CPR-67, CPR-29, CPR-30] Owner: Relevant Service Director; the Executive at the top band.

**T-08.1. Test.** For each sampled supplier, each T-03.1 or T-03.6 supplier whose contract is found, and each T-06.1 supplier whose award exceeds the Key Decision value, obtain the contract's total value and term, place it in its Appendix A value band, and inspect the decision record: the delegation or board-approved report, the Key Decision with its Forward Plan entry and Call-In record, or the Executive approval. For contracts let under the Procurement Legislation, inspect the written award report. Confirm the contract covers the supplier's payments in the period, including any flagged by the aggregation test. Pass: the decision matches the band and predates the award, and the contract covers the payments. Where the check depends on the Threshold, conclude it only once the council confirms the figure applied in the period; otherwise record it as not concluded. [CPR-04, CPR-66, CPR-67, CPR-65, CPR-64, CPR-02, CPR-29, CPR-30, metric:$.tests.high_value_suppliers.tiers[2].headline.count, metric:$.tests.split_purchases.tiers[1].headline.windows]  
**Evidence to inspect:** Decision record, board report, Forward Plan entry, Call-In record, Executive approval, award report  
**Sample:** 5 items from `high-value-suppliers.csv`, where dominant_tag = ['general_procurement', 'agency_staff'], annualised_estimate_gbp ≥ 500000, largest annualised_estimate_gbp first, 3 payments per supplier, excluding suppliers and rows already drawn in T-03.1, T-03.6, T-06.1; 13 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P02_-_published.xlsx:437` | 2026-05-20 | Newbury & District Ltd | £60,797.19 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:267` | 2026-06-01 | Newbury & District Ltd | £59,626.76 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:270` | 2026-06-30 | Newbury & District Ltd | £59,007.20 | Environment |
| 2 | `Over500_2026_P02_-_published.xlsx:669` | 2026-05-26 | ASCIA CONSTRUCTION LIMITED | £332,579.29 | Education & SEND |
| 3 | `Over500_2026_P04_-_published.xlsx:450` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £9,615.23 | Education & SEND |
| 3 | `Over500_2026_P04_-_published.xlsx:452` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £9,483.38 | Education & SEND |
| 3 | `Over500_2026_P04_-_published.xlsx:183` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £8,226.54 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:321` | 2026-07-14 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £4,074.00 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:266` | 2026-07-14 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £4,018.00 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:467` | 2026-07-09 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £4,018.00 | Education & SEND |
| 5 | `Over500_2026_P04_-_published.xlsx:260` | 2026-07-13 | BROADWAY CARS | £5,487.69 | Education & SEND |
| 5 | `Over500_2026_P04_-_published.xlsx:259` | 2026-07-13 | BROADWAY CARS | £5,330.00 | Education & SEND |
| 5 | `Over500_2026_P04_-_published.xlsx:264` | 2026-07-13 | BROADWAY CARS | £5,330.00 | Education & SEND |


## R-02: Related requirements may not have been aggregated before the procurement route was chosen [9 (High; Medium - High)]

**Audit objective.** Conclude whether related general-procurement purchases from one supplier were treated as one requirement and procured by the route their combined value requires.

**C-02.1. Expected control.** The full value of a requirement is established before the procurement route is chosen, no requirement is split or disaggregated to avoid the Rules, and at or above the three-quote threshold the aggregate is procured through Procurement Portal quotations with a published contract notice. [CPR-12, CPR-69, CPR-70, CPR-71, CPR-72]

**T-02.1. Test.** For each sampled window, obtain the orders, invoices and any contract behind its largest payments, and the order references for the rest of the window, and establish whether the window's payments met one requirement. Where they did, check the route against the window total: Procurement Portal invitations to quote and a contract notice, with the quotation records held on file. Pass: the payments are separate requirements, instalments under a contract already let (confirmed, then set aside), or procured by the route the aggregate value requires. Suppliers whose contract file is examined in T-03.1, T-03.6, T-03.4, T-05.1, T-06.1 or T-08.1 are not drawn here; whether their windows fall under a contract is answered there. Where the check depends on the Threshold, conclude it only once the council confirms the figure applied in the period; otherwise record it as not concluded. [CPR-12, CPR-69, CPR-70, CPR-71, CPR-72, CPR-31, CPR-32, metric:$.tests.split_purchases.tiers[1].headline.windows]  
**Evidence to inspect:** Purchase orders, invoices, quotation records, Procurement Portal invitations, contract notice or contract  
**Sample:** 10 items from `split-purchases.csv`, where tag = general_procurement, threshold = 25000, largest total_gbp first, largest 5 payments per item, one item per supplier_norm, excluding suppliers and rows already drawn in T-03.1, T-03.6, T-03.4, T-05.1, T-06.1, T-08.1; 47 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:735` | 2026-07-13 | Roadside Technologies Ltd | £21,000.00 | Environment |
| 1 | `Over500_2026_P04_-_published.xlsx:733` | 2026-07-13 | Roadside Technologies Ltd | £11,188.22 | Environment |
| 1 | `Over500_2026_P04_-_published.xlsx:1287` | 2026-07-13 | Roadside Technologies Ltd | £10,298.22 | Environment |
| 1 | `Over500_2026_P04_-_published.xlsx:601` | 2026-07-13 | Roadside Technologies Ltd | £9,103.64 | Environment |
| 1 | `Over500_2026_P04_-_published.xlsx:740` | 2026-07-13 | Roadside Technologies Ltd | £9,103.64 | Environment |
| 2 | `Over500_2026_P03_-_published.xlsx:649` | 2026-06-18 | Triple Value Impact | £24,244.00 | Chief Executive |
| 2 | `Over500_2026_P03_-_published.xlsx:641` | 2026-06-17 | Triple Value Impact | £13,275.00 | Chief Executive |
| 2 | `Over500_2026_P03_-_published.xlsx:2393` | 2026-06-17 | Triple Value Impact | £13,110.00 | Chief Executive |
| 2 | `Over500_2026_P03_-_published.xlsx:2392` | 2026-06-17 | Triple Value Impact | £10,787.00 | Chief Executive |
| 2 | `Over500_2026_P03_-_published.xlsx:642` | 2026-06-17 | Triple Value Impact | £6,612.00 | Chief Executive |
| 3 | `Over500_2026_P03_-_published.xlsx:2132` | 2026-06-09 | PAYPOINT MOBILE & ONLINE | £15,451.51 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:2131` | 2026-06-09 | PAYPOINT MOBILE & ONLINE | £14,706.08 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:2139` | 2026-06-09 | PAYPOINT MOBILE & ONLINE | £14,227.57 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:3081` | 2026-06-09 | PAYPOINT MOBILE & ONLINE | £10,928.48 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:2138` | 2026-06-09 | PAYPOINT MOBILE & ONLINE | £3,085.02 | Environment |
| 4 | `Over500_2026_P03_-_published.xlsx:248` | 2026-06-17 | SOUTHERN COACH LINES LTD | £7,058.87 | Education & SEND |
| 4 | `Over500_2026_P03_-_published.xlsx:175` | 2026-06-16 | SOUTHERN COACH LINES LTD | £6,754.78 | Education & SEND |
| 4 | `Over500_2026_P03_-_published.xlsx:339` | 2026-06-17 | SOUTHERN COACH LINES LTD | £6,657.26 | Education & SEND |
| 4 | `Over500_2026_P03_-_published.xlsx:211` | 2026-06-16 | SOUTHERN COACH LINES LTD | £6,588.28 | Education & SEND |
| 4 | `Over500_2026_P03_-_published.xlsx:174` | 2026-06-16 | SOUTHERN COACH LINES LTD | £6,304.46 | Education & SEND |
| 5 | `Over500_2026_P03_-_published.xlsx:667` | 2026-06-09 | Home Front Ltd | £17,160.76 | Community Services |
| 5 | `Over500_2026_P03_-_published.xlsx:697` | 2026-06-25 | Home Front Ltd | £17,160.76 | Community Services |
| 5 | `Over500_2026_P03_-_published.xlsx:679` | 2026-06-25 | Home Front Ltd | £15,875.26 | Community Services |
| 6 | `Over500_2026_P04_-_published.xlsx:227` | 2026-07-22 | COMPASS EXECUTIVE CARS (UK) LTD | £4,455.00 | Education & SEND |
| 6 | `Over500_2026_P04_-_published.xlsx:478` | 2026-07-21 | COMPASS EXECUTIVE CARS (UK) LTD | £3,885.00 | Education & SEND |
| 6 | `Over500_2026_P04_-_published.xlsx:235` | 2026-07-15 | COMPASS EXECUTIVE CARS (UK) LTD | £3,654.00 | Education & SEND |
| 6 | `Over500_2026_P04_-_published.xlsx:429` | 2026-07-15 | COMPASS EXECUTIVE CARS (UK) LTD | £3,264.50 | Adult Social Care |
| 6 | `Over500_2026_P04_-_published.xlsx:288` | 2026-07-30 | COMPASS EXECUTIVE CARS (UK) LTD | £3,135.00 | Education & SEND |
| 7 | `Over500_2026_P02_-_published.xlsx:747` | 2026-05-18 | SUMMIT CONTRACTORS BUILD LTD | £18,425.00 | Development & Housing |
| 7 | `Over500_2026_P03_-_published.xlsx:735` | 2026-06-08 | SUMMIT CONTRACTORS BUILD LTD | £16,128.59 | Development & Housing |
| 7 | `Over500_2026_P03_-_published.xlsx:736` | 2026-06-11 | SUMMIT CONTRACTORS BUILD LTD | £6,817.50 | Development & Housing |
| 7 | `Over500_2026_P03_-_published.xlsx:712` | 2026-06-16 | SUMMIT CONTRACTORS BUILD LTD | £5,197.46 | Development & Housing |
| 8 | `Over500_2026_P02_-_published.xlsx:677` | 2026-05-01 | Bolinda UK Ltd | £12,000.00 | Community Services |
| 8 | `Over500_2026_P02_-_published.xlsx:679` | 2026-05-05 | Bolinda UK Ltd | £10,500.00 | Community Services |
| 8 | `Over500_2026_P02_-_published.xlsx:678` | 2026-05-01 | Bolinda UK Ltd | £8,000.00 | Community Services |
| 8 | `Over500_2026_P02_-_published.xlsx:648` | 2026-05-21 | Bolinda UK Ltd | £7,500.00 | Community Services |
| 8 | `Over500_2026_P02_-_published.xlsx:680` | 2026-05-05 | Bolinda UK Ltd | £7,000.00 | Community Services |
| 9 | `Over500_2026_P04_-_published.xlsx:148` | 2026-07-01 | Glen Cleaning Company Ltd | £5,829.96 | Finance, Property & Procurement |
| 9 | `Over500_2026_P04_-_published.xlsx:399` | 2026-07-24 | Glen Cleaning Company Ltd | £5,829.96 | Finance, Property & Procurement |
| 9 | `Over500_2026_P03_-_published.xlsx:307` | 2026-06-30 | Glen Cleaning Company Ltd | £2,543.28 | Adult Social Care |
| 9 | `Over500_2026_P04_-_published.xlsx:127` | 2026-07-20 | Glen Cleaning Company Ltd | £2,439.00 | Adult Social Care |
| 9 | `Over500_2026_P03_-_published.xlsx:132` | 2026-06-30 | Glen Cleaning Company Ltd | £1,911.14 | Community Services |
| 10 | `Over500_2026_P02_-_published.xlsx:217` | 2026-05-18 | D J TRAVEL | £6,700.00 | Adult Social Care |
| 10 | `Over500_2026_P02_-_published.xlsx:218` | 2026-05-19 | D J TRAVEL | £6,520.00 | Adult Social Care |
| 10 | `Over500_2026_P03_-_published.xlsx:156` | 2026-06-04 | D J TRAVEL | £6,365.00 | Adult Social Care |
| 10 | `Over500_2026_P03_-_published.xlsx:155` | 2026-06-02 | D J TRAVEL | £6,194.00 | Adult Social Care |
| 10 | `Over500_2026_P02_-_published.xlsx:934` | 2026-05-06 | D J TRAVEL | £3,100.00 | Adult Social Care |


## R-04: Duplicate supplier payments may not be prevented or detected [6 (Moderate; Moderate)]

**Audit objective.** Conclude whether same-supplier, same-amount general-procurement payments each settle a distinct purchase, and whether any duplicate was detected and recovered.

**C-04.1. Expected control.** Each payment is supported by written evidence of the purchase it settles, so that each invoice is paid once. [CPR-32]

**T-04.1. Test.** For each sampled group paid at different times, match each payment to its own invoice and order. Pass: every payment settles a distinct invoice for a distinct supply. Where two payments settle one invoice, confirm the council detected it and recovered or credited the amount. [CPR-32, metric:$.tests.duplicates.tiers.different_time.by_tag.general_procurement.rows]  
**Evidence to inspect:** Invoices, purchase orders, payment-run records, supplier statements, credit notes or recovery records  
**Sample:** 5 items from `duplicates.csv`, where tag = general_procurement, tier = different_time, largest excess_gbp first, one item per supplier_norm; 13 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:3308` | 2026-07-15 | VolkerHighways Ltd | £101,925.86 | Environment |
| 1 | `Over500_2026_P04_-_published.xlsx:618` | 2026-07-17 | VolkerHighways Ltd | £101,925.86 | Environment |
| 2 | `Over500_2026_P02_-_published.xlsx:2160` | 2026-05-12 | TWO SAINTS LTD | £27,147.69 | Development & Housing |
| 2 | `Over500_2026_P02_-_published.xlsx:2161` | 2026-05-13 | TWO SAINTS LTD | £27,147.69 | Development & Housing |
| 3 | `Over500_2026_P04_-_published.xlsx:598` | 2026-07-13 | Roadside Technologies Ltd | £5,594.11 | Environment |
| 3 | `Over500_2026_P04_-_published.xlsx:734` | 2026-07-13 | Roadside Technologies Ltd | £5,594.11 | Environment |
| 3 | `Over500_2026_P04_-_published.xlsx:789` | 2026-07-13 | Roadside Technologies Ltd | £5,594.11 | Environment |
| 3 | `Over500_2026_P04_-_published.xlsx:1288` | 2026-07-13 | Roadside Technologies Ltd | £5,594.11 | Environment |
| 4 | `Over500_2026_P04_-_published.xlsx:259` | 2026-07-13 | BROADWAY CARS | £5,330.00 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:264` | 2026-07-13 | BROADWAY CARS | £5,330.00 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:474` | 2026-07-13 | BROADWAY CARS | £5,330.00 | Education & SEND |
| 5 | `Over500_2026_P02_-_published.xlsx:8` | 2026-05-13 | Pavillion Publishing and Media Ltd | £9,084.60 | Adult Social Care |
| 5 | `Over500_2026_P02_-_published.xlsx:643` | 2026-05-14 | Pavillion Publishing and Media Ltd | £9,084.60 | Executive Director People - Children's Services |

**T-04.2. Test.** For each sampled group paid within a single payment run, match each payment to its own invoice and order. Pass: every payment settles a distinct invoice for a distinct supply. Where two payments settle one invoice, confirm the council detected it and recovered or credited the amount. [CPR-32, metric:$.tests.duplicates.tiers.same_timestamp.by_tag.general_procurement.rows]  
**Evidence to inspect:** Invoices, purchase orders, payment-run records, supplier statements, credit notes or recovery records  
**Sample:** 5 items from `duplicates.csv`, where tag = general_procurement, tier = same_timestamp, largest excess_gbp first, one item per supplier_norm, excluding suppliers and rows already drawn in T-04.1; 10 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P03_-_published.xlsx:2134` | 2026-06-18 | SEISMIC SEWAGE SYSTEMS LTD | £5,360.00 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:2141` | 2026-06-18 | SEISMIC SEWAGE SYSTEMS LTD | £5,360.00 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3663` | 2026-07-29 | MAISHA STAFFING SOLUTIONS LTD | £3,737.50 | Children's Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:3894` | 2026-07-29 | MAISHA STAFFING SOLUTIONS LTD | £3,737.50 | Children's Social Care |
| 3 | `Over500_2026_P04_-_published.xlsx:162` | 2026-07-21 | COMPASS EXECUTIVE CARS (UK) LTD | £2,178.00 | Education & SEND |
| 3 | `Over500_2026_P04_-_published.xlsx:171` | 2026-07-21 | COMPASS EXECUTIVE CARS (UK) LTD | £2,178.00 | Education & SEND |
| 4 | `Over500_2026_P03_-_published.xlsx:165` | 2026-06-30 | DANIEL GRIFFITHS T/A BLUEBIRD PASSENGER SERVICES | £2,050.00 | Education & SEND |
| 4 | `Over500_2026_P03_-_published.xlsx:334` | 2026-06-30 | DANIEL GRIFFITHS T/A BLUEBIRD PASSENGER SERVICES | £2,050.00 | Education & SEND |
| 5 | `Over500_2026_P03_-_published.xlsx:2413` | 2026-06-25 | AMR CONSULT LTD | £2,046.67 | Education & SEND |
| 5 | `Over500_2026_P03_-_published.xlsx:716` | 2026-06-25 | AMR CONSULT LTD | £2,046.67 | Education & SEND |


## R-07: Waivers and exceptions may not be authorised and documented as the rules require [6 (Moderate; Moderate)]

**Audit objective.** Conclude whether waivers of and exceptions to the Rules were granted in advance, by the officer and at the level the Rules require, and fully documented.

**C-07.1. Expected control.** Waivers and exceptions are granted only in advance, in exceptional circumstances, by the Monitoring Officer and/or S151 Officer at the level the contract value requires; a discretionary waiver by an Executive Director or the Chief Executive carries written reasons, and urgency is relied on only on the grounds the Rules state. [CPR-21, CPR-20, CPR-22, CPR-23, CPR-24, CPR-19] Owner: Monitoring Officer and/or S151 Officer.

**T-07.1. Test.** Obtain the council's waiver and exception register for the spend period. For each selected waiver, confirm the approval predates the commitment, the approver is the officer the Rules name, and the approval level matches the contract value. Where an Executive Director or the Chief Executive exercised discretion, inspect the written reasons; where urgency was the ground, confirm the stated conditions applied. Pass: all hold. Where the check depends on the Threshold, conclude it only once the council confirms the figure applied in the period; otherwise record it as not concluded. [CPR-21, CPR-20, CPR-22, CPR-23, CPR-24, CPR-19]  
**Evidence to inspect:** Waiver and exception register, waiver applications and dated approvals  
**Sample:** No waiver data is published. The auditor selects five waivers or exceptions from the council's register for the spend period, largest contract value first.

**C-07.2. Expected control.** Each waiver or exception is fully documented, reported in advance to the relevant board where competition is not excluded by the Procurement Legislation, and approved by the S151 Officer with a record that the reasons were considered and are genuinely exceptional. [CPR-25, CPR-26, CPR-27] Owner: S151 Officer.

**T-07.2. Test.** For the waivers selected in T-07.1, inspect the supporting documentation, the exception report to the relevant board where competition was not excluded by law, and the S151 Officer's record that the reasons were considered and are genuinely exceptional. Pass: each is complete and dated before the commitment. [CPR-25, CPR-26, CPR-27]  
**Evidence to inspect:** Waiver file, board exception report and minute, S151 Officer approval record  
**Sample:** Uses the waivers selected in T-07.1.

**C-07.3. Expected control.** A contract excluded from competition carries prior written Monitoring Officer approval, and an exempted contract above the Threshold carries relevant board approval. [CPR-75, CPR-82] Owner: Monitoring Officer; relevant board.

**T-07.3. Test.** For each T-03.1, T-03.6 or T-03.4 supplier where the council cites a waiver or exemption instead of a published notice, locate the waiver register entry or exemption record and confirm its approval: the waiver approvals tested in T-07.1 and T-07.2, prior written Monitoring Officer approval for a contract excluded from competition, and relevant board approval where the exempted value requires it. Pass: an approved waiver or exemption covers the payments. Where the check depends on the Threshold, conclude it only once the council confirms the figure applied in the period; otherwise record it as not concluded. [CPR-21, CPR-75, CPR-82, metric:$.tests.off_contract.headline.count]  
**Evidence to inspect:** Waiver register entry or exemption record, Monitoring Officer approval, board approval  
**Sample:** Uses the suppliers sampled in T-03.1, T-03.6 and T-03.4 that the council says are covered by a waiver or exemption.


## Prepared-by-client (PBC) request list

Derived from the test steps above. Each item names the tests that need it.

| # | Risk | Item requested | For tests |
|---|---|---|---|
| 1 | R-05 | Extension approvals or replacement contracts for the suppliers sampled in T-05.1 | T-05.1 |
| 2 | R-06 | Supplier ledger from contract start to the end of the spend period for the suppliers sampled in T-06.1 | T-06.1 |
| 3 | R-06 | Contract, basis of the award value and any variations with their approvals for the suppliers sampled in T-06.1 | T-06.1 |
| 4 | R-06 | The Threshold figure the council applied in the spend period, with its source | T-06.1 |
| 5 | R-03 | Council contract register, full extract current for the spend period | T-03.1 |
| 6 | R-03 | Contracts or call-offs, with term, value and scope, for the suppliers sampled in T-03.1 | T-03.1 |
| 7 | R-03 | Contracts or call-offs, with term, value and scope, for the suppliers sampled in T-03.6 | T-03.6 |
| 8 | R-03 | Contracts or call-offs, with term, value and scope, for the suppliers sampled in T-03.4 | T-03.4 |
| 9 | R-03 | Procurement Portal records and contract notices for the contracts found in T-03.1, T-03.6 and T-03.4 | T-03.2 |
| 10 | R-03 | The Threshold figure the council applied in the spend period, with its source | T-03.2 |
| 11 | R-03 | Scheme agreements, call-offs, pre-use advice and direct-award approvals for T-03.1, T-03.6 and T-03.4 suppliers covered by a purchasing scheme | T-03.5 |
| 12 | R-03 | Contract register entry and contract for each near-match candidate notice | T-03.3 |
| 13 | R-08 | Award decision records, board reports, Forward Plan entries, Executive approvals and award reports for the contracts tested in T-08.1 | T-08.1 |
| 14 | R-08 | The Threshold figure the council applied in the spend period, with its source | T-08.1 |
| 15 | R-02 | Purchase orders and invoices for the sampled payments in each window | T-02.1 |
| 16 | R-02 | Quotation records, Procurement Portal invitations and any contract notice for the sampled windows | T-02.1 |
| 17 | R-02 | The Threshold figure the council applied in the spend period, with its source | T-02.1 |
| 18 | R-04 | Invoices and purchase orders for the sampled payments | T-04.1, T-04.2 |
| 19 | R-04 | Payment-run reports and any credit note or recovery record for the sampled groups | T-04.1, T-04.2 |
| 20 | R-07 | Waiver and exception register for the spend period | T-07.1 |
| 21 | R-07 | Waiver applications, approvals and exception reports for the waivers selected in T-07.1 | T-07.1 |
| 22 | R-07 | The Threshold figure the council applied in the spend period, with its source | T-07.1, T-07.3 |
| 23 | R-07 | Board exception reports and minutes for the waivers selected in T-07.1 | T-07.2 |
| 24 | R-07 | Exemption records and approvals for T-03.1, T-03.6 and T-03.4 suppliers without a published notice | T-07.3 |
