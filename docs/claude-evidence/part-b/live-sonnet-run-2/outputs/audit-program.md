# Audit program

*Generated 2026-10-19 by `build_pack.py` from `audit-plan.json`, `risk-register.md` (revision 1), `auditor-comments.md` by tony dated 2026-10-19, `rules.json` and `analytics.json`. Status: DRAFT for challenge, QA review and auditor sign-off.*

**Indicators, not findings.** Every test below checks a control against a pattern in public data. Nothing here asserts wrongdoing by the council, a department, an officer or a supplier.

8 risks in scope, 13 controls, 20 tests, 571 sampled transactions. Samples are drawn by the builder from `analytics-full/` by the recipe stated under each test, and every transaction is listed with its workbook row.


## R-01: Payments may cluster just below procurement route boundaries [6 (Moderate; Moderate)]

**Audit objective.** Conclude whether the full requirement behind payments observed just below the printed quote boundaries was procured by the route the Rules require for its total value band.

**C-01.1. Expected control.** Purchases in the lowest competition band have at least one quote sought from an appropriate source. [CPR-68] Owner: Not named in the Rules.

**T-01.1. Test.** For each sampled payment, establish the total value of the underlying requirement by obtaining the orders, requisitions and any related payments to the same payee, and decide whether it exceeded the lowest quote boundary. If it did not, record that a quote was not required and that the payment alone could not show a failure. If it did, obtain the quote or quotes held and confirm that a quote was sought and that its value and date support the amount. Note whether the payee has repeat payments at the same value. [CPR-68, CPR-12, metric:$.tests.threshold_clustering.tiers[0].count]  
**Evidence to inspect:** Orders, requisitions, quotation, approval record, schedule of related payments  
**Sample:** 5 items from `threshold-clustering.csv`, where threshold = 1000, tag = general_procurement, largest pay_date first, one item per supplier_norm, excluding supplier_norm matching /^(E WALLET|PREPAID FINANCIAL SERVICES)$/; 5 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:34` | 2026-07-31 | Expert Access Solutions Ltd | £914.00 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:1016` | 2026-07-31 | ACCESS UK LIMITED | £950.00 | Adult Social Care - Transformation Projects |
| 3 | `Over500_2026_P04_-_published.xlsx:126` | 2026-07-30 | Glen Cleaning Company Ltd | £901.77 | Community Services |
| 4 | `Over500_2026_P04_-_published.xlsx:422` | 2026-07-30 | HSI FURNITURE | £980.00 | Finance, Property & Procurement |
| 5 | `Over500_2026_P04_-_published.xlsx:597` | 2026-07-30 | Roadside Technologies Ltd | £1,000.00 | Environment |

**C-01.2. Expected control.** Purchases at the next band have invitations to quote sent through the Procurement Portal to at least three appropriate sources, based on the total value of the requirement. [CPR-69, CPR-71] Owner: Not named in the Rules.

**T-01.2. Test.** For each sampled payment, obtain the contract, award notice or requisition and establish the total value of the full requirement, with the VAT basis the Council applies. Decide which band that value falls in, then obtain the invitations to quote and the responses. Confirm that the route used matched the band, that at least three sources were invited through the Portal, that an SME or VCSE and a local supplier were included where appropriate and possible, and that the award followed the quotes received. Where the payee also appears in the award-rate test, compare the award value and term with the route used. Payees that are other public authorities are excluded from this sample. [CPR-69, CPR-71, CPR-12, metric:$.tests.threshold_clustering.tiers[1].count]  
**Evidence to inspect:** Contract or award notice, requisition, Portal invitation record, quotes received, evaluation note, award decision  
**Sample:** 5 items from `threshold-clustering.csv`, where threshold = 25000, tag = general_procurement, largest amount_pence first, one item per supplier_norm, excluding supplier_norm matching /\b(COUNCIL|BOROUGH|CNCL)\b/; 5 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:1281` | 2026-07-29 | The Better Group Ltd | £24,476.02 | Adult Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:649` | 2026-06-18 | Triple Value Impact | £24,244.00 | Chief Executive |
| 3 | `Over500_2026_P02_-_published.xlsx:560` | 2026-05-12 | DevComms South East Ltd | £24,227.07 | Development & Housing |
| 4 | `Over500_2026_P03_-_published.xlsx:396` | 2026-06-10 | BookingLab Limited | £24,000.00 | Transformation, Customer & ICT |
| 5 | `Over500_2026_P02_-_published.xlsx:530` | 2026-05-27 | Elior UK PLC | £23,694.03 | Adult Social Care |


## R-02: Related requirements may not be aggregated for procurement purposes [9 (High; Medium - High)]

**Audit objective.** Conclude whether related requirements were treated as one purchase when the route was chosen, or were bought in parts, and whether aggregated requirements above the key decision boundary followed the approval route.

**C-02.1. Expected control.** Requirements are not split or disaggregated to avoid the Procurement Legislation or the Rules, and related needs are considered together when the route is chosen. [CPR-12] Owner: Not named in the Rules.

**T-02.1. Test.** For each sampled window, obtain the orders, requisitions and any quotes behind the grouped payments. Establish whether they were one requirement and, if so, whether the route followed the combined value. Record the reason given for separate orders. Payees that are other public authorities are excluded from this sample. [CPR-12, CPR-69, CPR-71, metric:$.tests.split_purchases.tiers[1].headline.windows]  
**Evidence to inspect:** Purchase orders, requisitions, quotations, contract register entry, officer explanation  
**Sample:** 10 items from `split-purchases.csv`, where threshold = 25000, tag = general_procurement, largest total_gbp first, one item per supplier_norm, excluding supplier_norm matching /\b(COUNCIL|BOROUGH|CNCL)\b/; 175 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P02_-_published.xlsx:2174` | 2026-05-05 | VolkerHighways Ltd | £4,764.64 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2177` | 2026-05-05 | VolkerHighways Ltd | £16,876.43 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2178` | 2026-05-05 | VolkerHighways Ltd | £16,916.01 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2181` | 2026-05-05 | VolkerHighways Ltd | £9,068.36 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:695` | 2026-05-05 | VolkerHighways Ltd | £15,041.26 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:713` | 2026-05-05 | VolkerHighways Ltd | £7,742.55 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:723` | 2026-05-05 | VolkerHighways Ltd | £18,033.36 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:727` | 2026-05-11 | VolkerHighways Ltd | £3,196.62 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:696` | 2026-05-12 | VolkerHighways Ltd | £2,566.36 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:701` | 2026-05-12 | VolkerHighways Ltd | £17,896.87 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:714` | 2026-05-12 | VolkerHighways Ltd | £1,550.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:724` | 2026-05-12 | VolkerHighways Ltd | £7,828.20 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:703` | 2026-05-13 | VolkerHighways Ltd | £12,297.34 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2179` | 2026-05-19 | VolkerHighways Ltd | £17,882.35 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2193` | 2026-05-19 | VolkerHighways Ltd | £1,668.58 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2170` | 2026-05-20 | VolkerHighways Ltd | £16,304.62 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2185` | 2026-05-20 | VolkerHighways Ltd | £19,420.72 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:728` | 2026-05-20 | VolkerHighways Ltd | £10,169.81 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:731` | 2026-05-20 | VolkerHighways Ltd | £2,585.44 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2172` | 2026-05-22 | VolkerHighways Ltd | £2,070.26 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:730` | 2026-05-22 | VolkerHighways Ltd | £1,679.16 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:734` | 2026-05-22 | VolkerHighways Ltd | £5,199.81 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2180` | 2026-05-26 | VolkerHighways Ltd | £7,015.34 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2182` | 2026-05-26 | VolkerHighways Ltd | £4,046.54 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:697` | 2026-05-26 | VolkerHighways Ltd | £1,711.48 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:715` | 2026-05-26 | VolkerHighways Ltd | £5,225.72 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:716` | 2026-05-26 | VolkerHighways Ltd | £850.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:721` | 2026-05-26 | VolkerHighways Ltd | £10,122.39 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:726` | 2026-05-26 | VolkerHighways Ltd | £2,610.11 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:693` | 2026-05-27 | VolkerHighways Ltd | £5,997.50 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:694` | 2026-05-27 | VolkerHighways Ltd | £8,175.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:699` | 2026-05-27 | VolkerHighways Ltd | £1,793.45 | Environment |
| 2 | `Over500_2026_P02_-_published.xlsx:10` | 2026-05-28 | The Better Group Ltd | £19,605.14 | Children's Social Care |
| 2 | `Over500_2026_P02_-_published.xlsx:11` | 2026-05-28 | The Better Group Ltd | £2,557.08 | Education & SEND |
| 2 | `Over500_2026_P02_-_published.xlsx:9` | 2026-05-28 | The Better Group Ltd | £20,457.43 | Adult Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:13` | 2026-06-01 | The Better Group Ltd | £24,088.98 | Children's Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:16` | 2026-06-01 | The Better Group Ltd | £15,478.22 | Children's Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:19` | 2026-06-01 | The Better Group Ltd | £3,142.04 | Education & SEND |
| 2 | `Over500_2026_P03_-_published.xlsx:20` | 2026-06-01 | The Better Group Ltd | £2,018.90 | Education & SEND |
| 2 | `Over500_2026_P03_-_published.xlsx:2396` | 2026-06-01 | The Better Group Ltd | £18,039.18 | Adult Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:2397` | 2026-06-01 | The Better Group Ltd | £22,361.26 | Adult Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:26` | 2026-06-01 | The Better Group Ltd | £16,151.18 | Adult Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:379` | 2026-06-09 | The Better Group Ltd | £14,706.64 | Adult Social Care - Transformation Projects |
| 2 | `Over500_2026_P03_-_published.xlsx:394` | 2026-06-09 | The Better Group Ltd | £12,427.19 | Adult Social Care - Transformation Projects |
| 2 | `Over500_2026_P03_-_published.xlsx:395` | 2026-06-09 | The Better Group Ltd | £11,180.63 | Adult Social Care - Transformation Projects |
| 2 | `Over500_2026_P03_-_published.xlsx:15` | 2026-06-25 | The Better Group Ltd | £2,668.67 | Adult Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:27` | 2026-06-25 | The Better Group Ltd | £2,557.48 | Children's Social Care |
| 3 | `Over500_2026_P03_-_published.xlsx:268` | 2026-06-01 | Newbury & District Ltd | £13,826.61 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:357` | 2026-06-01 | Newbury & District Ltd | £6,349.35 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:171` | 2026-06-02 | Newbury & District Ltd | £10,529.33 | Education & SEND |
| 3 | `Over500_2026_P03_-_published.xlsx:336` | 2026-06-02 | Newbury & District Ltd | £9,861.00 | Education & SEND |
| 3 | `Over500_2026_P03_-_published.xlsx:341` | 2026-06-02 | Newbury & District Ltd | £794.67 | Education & SEND |
| 3 | `Over500_2026_P03_-_published.xlsx:264` | 2026-06-12 | Newbury & District Ltd | £6,331.70 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:269` | 2026-06-12 | Newbury & District Ltd | £14,852.00 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:176` | 2026-06-30 | Newbury & District Ltd | £7,785.00 | Education & SEND |
| 3 | `Over500_2026_P03_-_published.xlsx:213` | 2026-06-30 | Newbury & District Ltd | £8,312.63 | Education & SEND |
| 3 | `Over500_2026_P03_-_published.xlsx:251` | 2026-06-30 | Newbury & District Ltd | £627.37 | Education & SEND |
| 3 | `Over500_2026_P03_-_published.xlsx:274` | 2026-06-30 | Newbury & District Ltd | £13,663.85 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:359` | 2026-06-30 | Newbury & District Ltd | £5,921.50 | Environment |
| 3 | `Over500_2026_P03_-_published.xlsx:360` | 2026-06-30 | Newbury & District Ltd | £4,465.96 | Environment |
| 4 | `Over500_2026_P04_-_published.xlsx:181` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £1,197.90 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:183` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £8,226.54 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:195` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £730.27 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:196` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £862.12 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:245` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £1,214.56 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:246` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £4,549.40 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:253` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £2,118.96 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:300` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £999.32 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:301` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £1,039.14 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:302` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £7,911.27 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:309` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £2,974.60 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:450` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £9,615.23 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:451` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £574.66 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:452` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £9,483.38 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:459` | 2026-07-08 | WEAVAWAY TRAVEL LTD | £2,312.52 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:192` | 2026-07-24 | WEAVAWAY TRAVEL LTD | £6,662.12 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:197` | 2026-07-24 | WEAVAWAY TRAVEL LTD | £614.96 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:198` | 2026-07-24 | WEAVAWAY TRAVEL LTD | £2,504.93 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:249` | 2026-07-24 | WEAVAWAY TRAVEL LTD | £6,927.61 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:250` | 2026-07-24 | WEAVAWAY TRAVEL LTD | £3,831.07 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:305` | 2026-07-24 | WEAVAWAY TRAVEL LTD | £7,986.00 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:310` | 2026-07-24 | WEAVAWAY TRAVEL LTD | £1,784.39 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:311` | 2026-07-24 | WEAVAWAY TRAVEL LTD | £1,947.39 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:456` | 2026-07-24 | WEAVAWAY TRAVEL LTD | £8,097.04 | Education & SEND |
| 4 | `Over500_2026_P04_-_published.xlsx:460` | 2026-07-24 | WEAVAWAY TRAVEL LTD | £726.00 | Education & SEND |
| 5 | `Over500_2026_P04_-_published.xlsx:1287` | 2026-07-13 | Roadside Technologies Ltd | £10,298.22 | Environment |
| 5 | `Over500_2026_P04_-_published.xlsx:1288` | 2026-07-13 | Roadside Technologies Ltd | £5,594.11 | Environment |
| 5 | `Over500_2026_P04_-_published.xlsx:598` | 2026-07-13 | Roadside Technologies Ltd | £5,594.11 | Environment |
| 5 | `Over500_2026_P04_-_published.xlsx:601` | 2026-07-13 | Roadside Technologies Ltd | £9,103.64 | Environment |
| 5 | `Over500_2026_P04_-_published.xlsx:733` | 2026-07-13 | Roadside Technologies Ltd | £11,188.22 | Environment |
| 5 | `Over500_2026_P04_-_published.xlsx:734` | 2026-07-13 | Roadside Technologies Ltd | £5,594.11 | Environment |
| 5 | `Over500_2026_P04_-_published.xlsx:735` | 2026-07-13 | Roadside Technologies Ltd | £21,000.00 | Environment |
| 5 | `Over500_2026_P04_-_published.xlsx:740` | 2026-07-13 | Roadside Technologies Ltd | £9,103.64 | Environment |
| 5 | `Over500_2026_P04_-_published.xlsx:789` | 2026-07-13 | Roadside Technologies Ltd | £5,594.11 | Environment |
| 5 | `Over500_2026_P04_-_published.xlsx:597` | 2026-07-30 | Roadside Technologies Ltd | £1,000.00 | Environment |
| 6 | `Over500_2026_P02_-_published.xlsx:265` | 2026-05-12 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,912.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:380` | 2026-05-12 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,448.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:381` | 2026-05-12 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,716.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:382` | 2026-05-12 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £1,596.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:383` | 2026-05-12 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,210.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:384` | 2026-05-12 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,156.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:385` | 2026-05-12 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,324.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:241` | 2026-05-13 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £1,288.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:242` | 2026-05-13 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £693.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:266` | 2026-05-13 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £1,092.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:289` | 2026-05-13 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £1,980.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:290` | 2026-05-13 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £1,288.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:387` | 2026-05-13 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,590.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:388` | 2026-05-13 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,576.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:389` | 2026-05-13 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,744.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:390` | 2026-05-13 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,079.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:251` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £742.50 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:283` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,340.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:284` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £3,120.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:294` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,244.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:422` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,910.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:423` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,622.86 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:424` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,940.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:425` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,550.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:426` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,227.50 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:427` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,925.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:428` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,745.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:429` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £1,608.00 | Education & SEND |
| 6 | `Over500_2026_P02_-_published.xlsx:430` | 2026-05-28 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,187.50 | Education & SEND |
| 6 | `Over500_2026_P03_-_published.xlsx:164` | 2026-06-05 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £1,380.00 | Education & SEND |
| 6 | `Over500_2026_P03_-_published.xlsx:184` | 2026-06-05 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,490.00 | Education & SEND |
| 6 | `Over500_2026_P03_-_published.xlsx:228` | 2026-06-05 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,775.00 | Education & SEND |
| 6 | `Over500_2026_P03_-_published.xlsx:229` | 2026-06-05 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,760.00 | Education & SEND |
| 6 | `Over500_2026_P03_-_published.xlsx:255` | 2026-06-05 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £1,710.00 | Education & SEND |
| 6 | `Over500_2026_P03_-_published.xlsx:333` | 2026-06-05 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £1,380.00 | Education & SEND |
| 6 | `Over500_2026_P03_-_published.xlsx:346` | 2026-06-05 | FD TRAVELS LIMITED T/A SCHOOL EXPRESS | £2,310.00 | Education & SEND |
| 7 | `Over500_2026_P02_-_published.xlsx:530` | 2026-05-27 | Elior UK PLC | £23,694.03 | Adult Social Care |
| 7 | `Over500_2026_P03_-_published.xlsx:434` | 2026-06-11 | Elior UK PLC | £11,935.93 | Adult Social Care |
| 7 | `Over500_2026_P03_-_published.xlsx:440` | 2026-06-16 | Elior UK PLC | £23,516.69 | Adult Social Care |
| 7 | `Over500_2026_P03_-_published.xlsx:433` | 2026-06-17 | Elior UK PLC | £18,592.30 | Adult Social Care |
| 8 | `Over500_2026_P02_-_published.xlsx:240` | 2026-05-12 | BROADWAY CARS | £1,213.33 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:288` | 2026-05-12 | BROADWAY CARS | £2,426.67 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:364` | 2026-05-12 | BROADWAY CARS | £3,747.69 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:367` | 2026-05-12 | BROADWAY CARS | £2,800.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:368` | 2026-05-12 | BROADWAY CARS | £2,100.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:369` | 2026-05-12 | BROADWAY CARS | £3,640.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:371` | 2026-05-12 | BROADWAY CARS | £2,240.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:372` | 2026-05-12 | BROADWAY CARS | £3,640.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:245` | 2026-05-13 | BROADWAY CARS | £2,076.67 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:297` | 2026-05-13 | BROADWAY CARS | £1,148.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:314` | 2026-05-13 | BROADWAY CARS | £595.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:391` | 2026-05-13 | BROADWAY CARS | £1,785.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:394` | 2026-05-13 | BROADWAY CARS | £3,220.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:395` | 2026-05-13 | BROADWAY CARS | £3,640.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:396` | 2026-05-13 | BROADWAY CARS | £3,010.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:403` | 2026-05-26 | BROADWAY CARS | £3,000.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:404` | 2026-05-26 | BROADWAY CARS | £4,015.38 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:249` | 2026-05-27 | BROADWAY CARS | £1,300.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:250` | 2026-05-27 | BROADWAY CARS | £2,225.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:292` | 2026-05-27 | BROADWAY CARS | £2,600.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:299` | 2026-05-27 | BROADWAY CARS | £1,230.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:326` | 2026-05-27 | BROADWAY CARS | £595.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:410` | 2026-05-27 | BROADWAY CARS | £2,400.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:411` | 2026-05-27 | BROADWAY CARS | £2,250.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:412` | 2026-05-27 | BROADWAY CARS | £3,900.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:414` | 2026-05-27 | BROADWAY CARS | £3,220.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:415` | 2026-05-27 | BROADWAY CARS | £1,785.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:416` | 2026-05-27 | BROADWAY CARS | £3,900.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:418` | 2026-05-27 | BROADWAY CARS | £3,900.00 | Education & SEND |
| 8 | `Over500_2026_P02_-_published.xlsx:419` | 2026-05-27 | BROADWAY CARS | £3,010.00 | Education & SEND |
| 9 | `Over500_2026_P03_-_published.xlsx:688` | 2026-06-01 | R&A Haines Building Contractors | £20,332.89 | Development & Housing |
| 9 | `Over500_2026_P03_-_published.xlsx:733` | 2026-06-01 | R&A Haines Building Contractors | £9,666.85 | Development & Housing |
| 9 | `Over500_2026_P03_-_published.xlsx:709` | 2026-06-09 | R&A Haines Building Contractors | £5,487.25 | Development & Housing |
| 9 | `Over500_2026_P03_-_published.xlsx:740` | 2026-06-30 | R&A Haines Building Contractors | £16,600.00 | Development & Housing |
| 9 | `Over500_2026_P03_-_published.xlsx:742` | 2026-06-30 | R&A Haines Building Contractors | £18,707.55 | Development & Housing |
| 10 | `Over500_2026_P03_-_published.xlsx:2392` | 2026-06-17 | Triple Value Impact | £10,787.00 | Chief Executive |
| 10 | `Over500_2026_P03_-_published.xlsx:2393` | 2026-06-17 | Triple Value Impact | £13,110.00 | Chief Executive |
| 10 | `Over500_2026_P03_-_published.xlsx:641` | 2026-06-17 | Triple Value Impact | £13,275.00 | Chief Executive |
| 10 | `Over500_2026_P03_-_published.xlsx:642` | 2026-06-17 | Triple Value Impact | £6,612.00 | Chief Executive |
| 10 | `Over500_2026_P03_-_published.xlsx:649` | 2026-06-18 | Triple Value Impact | £24,244.00 | Chief Executive |

**T-02.2. Test.** For each general-procurement window at the highest boundary, obtain the contract, orders and requisitions behind the grouped payments. Establish whether they form one requirement, whether the aggregate value was considered when the route was chosen, and whether any call-off or framework arrangement applies. Record the reason given for any separate orders. [CPR-12, metric:$.tests.split_purchases.tiers[2].headline.windows]  
**Evidence to inspect:** Contract, purchase orders, requisitions, framework or call-off record, officer explanation  
**Sample:** 3 items from `split-purchases.csv`, where threshold = 500000, tag = general_procurement, largest total_gbp first, (only 3 available); 99 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P02_-_published.xlsx:727` | 2026-05-11 | VolkerHighways Ltd | £3,196.62 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:696` | 2026-05-12 | VolkerHighways Ltd | £2,566.36 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:700` | 2026-05-12 | VolkerHighways Ltd | £85,125.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:701` | 2026-05-12 | VolkerHighways Ltd | £17,896.87 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:710` | 2026-05-12 | VolkerHighways Ltd | £119,381.40 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:714` | 2026-05-12 | VolkerHighways Ltd | £1,550.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:720` | 2026-05-12 | VolkerHighways Ltd | £32,864.67 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:724` | 2026-05-12 | VolkerHighways Ltd | £7,828.20 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:692` | 2026-05-13 | VolkerHighways Ltd | £185,970.32 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:702` | 2026-05-13 | VolkerHighways Ltd | £195,844.36 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:703` | 2026-05-13 | VolkerHighways Ltd | £12,297.34 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2173` | 2026-05-19 | VolkerHighways Ltd | £28,217.54 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2176` | 2026-05-19 | VolkerHighways Ltd | £54,241.36 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2179` | 2026-05-19 | VolkerHighways Ltd | £17,882.35 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2184` | 2026-05-19 | VolkerHighways Ltd | £101,925.86 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2193` | 2026-05-19 | VolkerHighways Ltd | £1,668.58 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2170` | 2026-05-20 | VolkerHighways Ltd | £16,304.62 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2185` | 2026-05-20 | VolkerHighways Ltd | £19,420.72 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:704` | 2026-05-20 | VolkerHighways Ltd | £43,509.85 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:705` | 2026-05-20 | VolkerHighways Ltd | £157,038.29 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:728` | 2026-05-20 | VolkerHighways Ltd | £10,169.81 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:731` | 2026-05-20 | VolkerHighways Ltd | £2,585.44 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2172` | 2026-05-22 | VolkerHighways Ltd | £2,070.26 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:729` | 2026-05-22 | VolkerHighways Ltd | £46,320.84 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:730` | 2026-05-22 | VolkerHighways Ltd | £1,679.16 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:734` | 2026-05-22 | VolkerHighways Ltd | £5,199.81 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2180` | 2026-05-26 | VolkerHighways Ltd | £7,015.34 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2182` | 2026-05-26 | VolkerHighways Ltd | £4,046.54 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:697` | 2026-05-26 | VolkerHighways Ltd | £1,711.48 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:711` | 2026-05-26 | VolkerHighways Ltd | £200,305.25 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:712` | 2026-05-26 | VolkerHighways Ltd | £83,960.48 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:715` | 2026-05-26 | VolkerHighways Ltd | £5,225.72 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:716` | 2026-05-26 | VolkerHighways Ltd | £850.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:721` | 2026-05-26 | VolkerHighways Ltd | £10,122.39 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:725` | 2026-05-26 | VolkerHighways Ltd | £28,989.53 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:726` | 2026-05-26 | VolkerHighways Ltd | £2,610.11 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:693` | 2026-05-27 | VolkerHighways Ltd | £5,997.50 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:694` | 2026-05-27 | VolkerHighways Ltd | £8,175.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:698` | 2026-05-27 | VolkerHighways Ltd | £34,813.14 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:699` | 2026-05-27 | VolkerHighways Ltd | £1,793.45 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:706` | 2026-05-27 | VolkerHighways Ltd | £149,153.26 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:722` | 2026-05-27 | VolkerHighways Ltd | £54,099.60 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:707` | 2026-05-28 | VolkerHighways Ltd | £58,615.47 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:2117` | 2026-06-08 | VolkerHighways Ltd | £3,393.12 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:2133` | 2026-06-08 | VolkerHighways Ltd | £18,761.89 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:2402` | 2026-06-08 | VolkerHighways Ltd | £15,899.60 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:683` | 2026-06-08 | VolkerHighways Ltd | £23,591.22 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:699` | 2026-06-08 | VolkerHighways Ltd | £329,988.88 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:700` | 2026-06-08 | VolkerHighways Ltd | £95,421.19 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:702` | 2026-06-08 | VolkerHighways Ltd | £4,205.33 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:703` | 2026-06-08 | VolkerHighways Ltd | £46,778.61 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:728` | 2026-06-08 | VolkerHighways Ltd | £11,515.39 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:729` | 2026-06-08 | VolkerHighways Ltd | £299,416.56 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:701` | 2026-06-09 | VolkerHighways Ltd | £307,338.45 | Environment |
| 2 | `Over500_2026_P03_-_published.xlsx:684` | 2026-06-22 | VolkerHighways Ltd | £366,872.38 | Environment |
| 2 | `Over500_2026_P03_-_published.xlsx:727` | 2026-06-24 | VolkerHighways Ltd | £1,151.28 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1291` | 2026-07-06 | VolkerHighways Ltd | £118,015.06 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3192` | 2026-07-06 | VolkerHighways Ltd | £7,341.73 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:792` | 2026-07-07 | VolkerHighways Ltd | £1,024.51 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1289` | 2026-07-13 | VolkerHighways Ltd | £651.56 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3184` | 2026-07-13 | VolkerHighways Ltd | £17,882.35 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3210` | 2026-07-13 | VolkerHighways Ltd | £54,241.36 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3786` | 2026-07-13 | VolkerHighways Ltd | £1,500.00 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:602` | 2026-07-13 | VolkerHighways Ltd | £4,081.14 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:621` | 2026-07-13 | VolkerHighways Ltd | £13,855.87 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:736` | 2026-07-13 | VolkerHighways Ltd | £577.53 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:791` | 2026-07-13 | VolkerHighways Ltd | £1,675.31 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:799` | 2026-07-13 | VolkerHighways Ltd | £800.00 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1295` | 2026-07-14 | VolkerHighways Ltd | £11,615.51 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1310` | 2026-07-14 | VolkerHighways Ltd | £6,704.19 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3186` | 2026-07-14 | VolkerHighways Ltd | £1,432.22 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3303` | 2026-07-14 | VolkerHighways Ltd | £3,323.18 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:794` | 2026-07-14 | VolkerHighways Ltd | £76,834.61 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:795` | 2026-07-14 | VolkerHighways Ltd | £161,847.24 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:798` | 2026-07-14 | VolkerHighways Ltd | £77,034.27 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1292` | 2026-07-15 | VolkerHighways Ltd | £56,244.83 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1293` | 2026-07-15 | VolkerHighways Ltd | £2,500.00 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3187` | 2026-07-15 | VolkerHighways Ltd | £1,606.50 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3211` | 2026-07-15 | VolkerHighways Ltd | £14,141.01 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3304` | 2026-07-15 | VolkerHighways Ltd | £12,585.51 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3308` | 2026-07-15 | VolkerHighways Ltd | £101,925.86 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3787` | 2026-07-15 | VolkerHighways Ltd | £1,000.00 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:619` | 2026-07-15 | VolkerHighways Ltd | £195,182.14 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:620` | 2026-07-15 | VolkerHighways Ltd | £69,616.13 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:739` | 2026-07-15 | VolkerHighways Ltd | £10,165.33 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:819` | 2026-07-15 | VolkerHighways Ltd | £12,778.97 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:821` | 2026-07-15 | VolkerHighways Ltd | £11,256.01 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:822` | 2026-07-15 | VolkerHighways Ltd | £14,660.85 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1296` | 2026-07-16 | VolkerHighways Ltd | £4,797.35 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3185` | 2026-07-16 | VolkerHighways Ltd | £17,882.35 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3302` | 2026-07-16 | VolkerHighways Ltd | £54,241.36 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3309` | 2026-07-17 | VolkerHighways Ltd | £3,337.15 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:618` | 2026-07-17 | VolkerHighways Ltd | £101,925.86 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:742` | 2026-07-17 | VolkerHighways Ltd | £7,732.30 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:777` | 2026-07-17 | VolkerHighways Ltd | £2,391.13 | Environment |
| 3 | `Over500_2026_P02_-_published.xlsx:473` | 2026-05-27 | SoftwareONE UK Ltd | £375,697.68 | Transformation, Customer & ICT |
| 3 | `Over500_2026_P02_-_published.xlsx:474` | 2026-05-27 | SoftwareONE UK Ltd | £85,871.04 | Transformation, Customer & ICT |
| 3 | `Over500_2026_P02_-_published.xlsx:653` | 2026-05-27 | SoftwareONE UK Ltd | £59,650.56 | Transformation, Customer & ICT |
| 3 | `Over500_2026_P02_-_published.xlsx:654` | 2026-05-27 | SoftwareONE UK Ltd | £1,759.34 | Transformation, Customer & ICT |

**C-02.2. Expected control.** Awards of aggregated value above the key decision boundary are authorised as the Rules require, as a Key Decision with a board-approved written report, or with Executive approval at the highest band. [CPR-02, CPR-04, CPR-66, CPR-67] Owner: Relevant Service Director, in consultation with the Portfolio Holder; the Executive at the highest band.

**T-02.3. Test.** For the same highest-boundary windows, establish the aggregate contract value and obtain the award decision. Confirm that it was taken at the level the Rules require for that value, that the written report was approved by the relevant board where required, and that the Key Decision procedure was followed. Where the aggregate is in the highest band, confirm Executive approval or delegated authority. [CPR-02, CPR-04, CPR-66, CPR-67, metric:$.tests.split_purchases.tiers[2].headline.windows]  
**Evidence to inspect:** Award decision record, Key Decision notice, board-approved written report, Executive minute or delegation  
**Sample:** 3 items from `split-purchases.csv`, where threshold = 500000, tag = general_procurement, largest total_gbp first, (only 3 available); 99 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P02_-_published.xlsx:727` | 2026-05-11 | VolkerHighways Ltd | £3,196.62 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:696` | 2026-05-12 | VolkerHighways Ltd | £2,566.36 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:700` | 2026-05-12 | VolkerHighways Ltd | £85,125.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:701` | 2026-05-12 | VolkerHighways Ltd | £17,896.87 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:710` | 2026-05-12 | VolkerHighways Ltd | £119,381.40 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:714` | 2026-05-12 | VolkerHighways Ltd | £1,550.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:720` | 2026-05-12 | VolkerHighways Ltd | £32,864.67 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:724` | 2026-05-12 | VolkerHighways Ltd | £7,828.20 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:692` | 2026-05-13 | VolkerHighways Ltd | £185,970.32 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:702` | 2026-05-13 | VolkerHighways Ltd | £195,844.36 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:703` | 2026-05-13 | VolkerHighways Ltd | £12,297.34 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2173` | 2026-05-19 | VolkerHighways Ltd | £28,217.54 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2176` | 2026-05-19 | VolkerHighways Ltd | £54,241.36 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2179` | 2026-05-19 | VolkerHighways Ltd | £17,882.35 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2184` | 2026-05-19 | VolkerHighways Ltd | £101,925.86 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2193` | 2026-05-19 | VolkerHighways Ltd | £1,668.58 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2170` | 2026-05-20 | VolkerHighways Ltd | £16,304.62 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2185` | 2026-05-20 | VolkerHighways Ltd | £19,420.72 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:704` | 2026-05-20 | VolkerHighways Ltd | £43,509.85 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:705` | 2026-05-20 | VolkerHighways Ltd | £157,038.29 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:728` | 2026-05-20 | VolkerHighways Ltd | £10,169.81 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:731` | 2026-05-20 | VolkerHighways Ltd | £2,585.44 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2172` | 2026-05-22 | VolkerHighways Ltd | £2,070.26 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:729` | 2026-05-22 | VolkerHighways Ltd | £46,320.84 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:730` | 2026-05-22 | VolkerHighways Ltd | £1,679.16 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:734` | 2026-05-22 | VolkerHighways Ltd | £5,199.81 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2180` | 2026-05-26 | VolkerHighways Ltd | £7,015.34 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:2182` | 2026-05-26 | VolkerHighways Ltd | £4,046.54 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:697` | 2026-05-26 | VolkerHighways Ltd | £1,711.48 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:711` | 2026-05-26 | VolkerHighways Ltd | £200,305.25 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:712` | 2026-05-26 | VolkerHighways Ltd | £83,960.48 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:715` | 2026-05-26 | VolkerHighways Ltd | £5,225.72 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:716` | 2026-05-26 | VolkerHighways Ltd | £850.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:721` | 2026-05-26 | VolkerHighways Ltd | £10,122.39 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:725` | 2026-05-26 | VolkerHighways Ltd | £28,989.53 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:726` | 2026-05-26 | VolkerHighways Ltd | £2,610.11 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:693` | 2026-05-27 | VolkerHighways Ltd | £5,997.50 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:694` | 2026-05-27 | VolkerHighways Ltd | £8,175.00 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:698` | 2026-05-27 | VolkerHighways Ltd | £34,813.14 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:699` | 2026-05-27 | VolkerHighways Ltd | £1,793.45 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:706` | 2026-05-27 | VolkerHighways Ltd | £149,153.26 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:722` | 2026-05-27 | VolkerHighways Ltd | £54,099.60 | Environment |
| 1 | `Over500_2026_P02_-_published.xlsx:707` | 2026-05-28 | VolkerHighways Ltd | £58,615.47 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:2117` | 2026-06-08 | VolkerHighways Ltd | £3,393.12 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:2133` | 2026-06-08 | VolkerHighways Ltd | £18,761.89 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:2402` | 2026-06-08 | VolkerHighways Ltd | £15,899.60 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:683` | 2026-06-08 | VolkerHighways Ltd | £23,591.22 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:699` | 2026-06-08 | VolkerHighways Ltd | £329,988.88 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:700` | 2026-06-08 | VolkerHighways Ltd | £95,421.19 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:702` | 2026-06-08 | VolkerHighways Ltd | £4,205.33 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:703` | 2026-06-08 | VolkerHighways Ltd | £46,778.61 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:728` | 2026-06-08 | VolkerHighways Ltd | £11,515.39 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:729` | 2026-06-08 | VolkerHighways Ltd | £299,416.56 | Environment |
| 1 | `Over500_2026_P03_-_published.xlsx:701` | 2026-06-09 | VolkerHighways Ltd | £307,338.45 | Environment |
| 2 | `Over500_2026_P03_-_published.xlsx:684` | 2026-06-22 | VolkerHighways Ltd | £366,872.38 | Environment |
| 2 | `Over500_2026_P03_-_published.xlsx:727` | 2026-06-24 | VolkerHighways Ltd | £1,151.28 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1291` | 2026-07-06 | VolkerHighways Ltd | £118,015.06 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3192` | 2026-07-06 | VolkerHighways Ltd | £7,341.73 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:792` | 2026-07-07 | VolkerHighways Ltd | £1,024.51 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1289` | 2026-07-13 | VolkerHighways Ltd | £651.56 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3184` | 2026-07-13 | VolkerHighways Ltd | £17,882.35 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3210` | 2026-07-13 | VolkerHighways Ltd | £54,241.36 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3786` | 2026-07-13 | VolkerHighways Ltd | £1,500.00 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:602` | 2026-07-13 | VolkerHighways Ltd | £4,081.14 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:621` | 2026-07-13 | VolkerHighways Ltd | £13,855.87 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:736` | 2026-07-13 | VolkerHighways Ltd | £577.53 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:791` | 2026-07-13 | VolkerHighways Ltd | £1,675.31 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:799` | 2026-07-13 | VolkerHighways Ltd | £800.00 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1295` | 2026-07-14 | VolkerHighways Ltd | £11,615.51 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1310` | 2026-07-14 | VolkerHighways Ltd | £6,704.19 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3186` | 2026-07-14 | VolkerHighways Ltd | £1,432.22 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3303` | 2026-07-14 | VolkerHighways Ltd | £3,323.18 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:794` | 2026-07-14 | VolkerHighways Ltd | £76,834.61 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:795` | 2026-07-14 | VolkerHighways Ltd | £161,847.24 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:798` | 2026-07-14 | VolkerHighways Ltd | £77,034.27 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1292` | 2026-07-15 | VolkerHighways Ltd | £56,244.83 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1293` | 2026-07-15 | VolkerHighways Ltd | £2,500.00 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3187` | 2026-07-15 | VolkerHighways Ltd | £1,606.50 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3211` | 2026-07-15 | VolkerHighways Ltd | £14,141.01 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3304` | 2026-07-15 | VolkerHighways Ltd | £12,585.51 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3308` | 2026-07-15 | VolkerHighways Ltd | £101,925.86 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3787` | 2026-07-15 | VolkerHighways Ltd | £1,000.00 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:619` | 2026-07-15 | VolkerHighways Ltd | £195,182.14 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:620` | 2026-07-15 | VolkerHighways Ltd | £69,616.13 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:739` | 2026-07-15 | VolkerHighways Ltd | £10,165.33 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:819` | 2026-07-15 | VolkerHighways Ltd | £12,778.97 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:821` | 2026-07-15 | VolkerHighways Ltd | £11,256.01 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:822` | 2026-07-15 | VolkerHighways Ltd | £14,660.85 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:1296` | 2026-07-16 | VolkerHighways Ltd | £4,797.35 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3185` | 2026-07-16 | VolkerHighways Ltd | £17,882.35 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3302` | 2026-07-16 | VolkerHighways Ltd | £54,241.36 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:3309` | 2026-07-17 | VolkerHighways Ltd | £3,337.15 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:618` | 2026-07-17 | VolkerHighways Ltd | £101,925.86 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:742` | 2026-07-17 | VolkerHighways Ltd | £7,732.30 | Environment |
| 2 | `Over500_2026_P04_-_published.xlsx:777` | 2026-07-17 | VolkerHighways Ltd | £2,391.13 | Environment |
| 3 | `Over500_2026_P02_-_published.xlsx:473` | 2026-05-27 | SoftwareONE UK Ltd | £375,697.68 | Transformation, Customer & ICT |
| 3 | `Over500_2026_P02_-_published.xlsx:474` | 2026-05-27 | SoftwareONE UK Ltd | £85,871.04 | Transformation, Customer & ICT |
| 3 | `Over500_2026_P02_-_published.xlsx:653` | 2026-05-27 | SoftwareONE UK Ltd | £59,650.56 | Transformation, Customer & ICT |
| 3 | `Over500_2026_P02_-_published.xlsx:654` | 2026-05-27 | SoftwareONE UK Ltd | £1,759.34 | Transformation, Customer & ICT |


## R-03: Supplier spend may lack a matching published contract notice [9 (High; Medium - High)]

**Audit objective.** Conclude whether contract opportunities and awards behind unmatched supplier spend, including managed-service agency spend and grants that may be contracts, were advertised, notified and recorded as the Rules require.

**C-03.1. Expected control.** Opportunities above the relevant boundary are advertised on the CDP before other media, and each CDP notice is approved and issued by the Service Lead for Procurement and Commissioning or their delegate. [CPR-70, CPR-72, CPR-10, CPR-11] Owner: Service Lead for Procurement and Commissioning or their delegate.

**T-03.1. Test.** For each sampled supplier, obtain the Council's contract register entry and any CDP or Find a Tender notice. Where no notice or entry exists, ask for the contract, the route taken and any exemption relied on. Confirm who approved the notice. [CPR-70, CPR-72, CPR-10, CPR-11, metric:$.tests.off_contract.eligible_suppliers, metric:$.matching.none]  
**Evidence to inspect:** Contract register entry, CDP or Find a Tender notice, contract, approval of notice  
**Sample:** 10 items from `off-contract.csv`, where dominant_tag = general_procurement, match_class = none, largest total_gbp first, 3 payments per supplier, excluding supplier matching /(?i)\b(COUNCIL|BOROUGH|CNCL)\b/; 30 transactions

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
| 4 | `Over500_2026_P02_-_published.xlsx:665` | 2026-05-15 | The Better Group Ltd | £64,500.00 | Adult Social Care |
| 4 | `Over500_2026_P02_-_published.xlsx:666` | 2026-05-15 | The Better Group Ltd | £58,833.00 | Adult Social Care |
| 4 | `Over500_2026_P03_-_published.xlsx:670` | 2026-06-01 | The Better Group Ltd | £48,784.37 | Adult Social Care |
| 5 | `Over500_2026_P02_-_published.xlsx:473` | 2026-05-27 | SoftwareONE UK Ltd | £375,697.68 | Transformation, Customer & ICT |
| 5 | `Over500_2026_P02_-_published.xlsx:474` | 2026-05-27 | SoftwareONE UK Ltd | £85,871.04 | Transformation, Customer & ICT |
| 5 | `Over500_2026_P02_-_published.xlsx:653` | 2026-05-27 | SoftwareONE UK Ltd | £59,650.56 | Transformation, Customer & ICT |
| 6 | `Over500_2026_P02_-_published.xlsx:2200` | 2026-05-13 | Livity Life Ltd | £135,591.03 | Finance, Property & Procurement |
| 6 | `Over500_2026_P03_-_published.xlsx:3087` | 2026-06-17 | Livity Life Ltd | £127,886.78 | Finance, Property & Procurement |
| 6 | `Over500_2026_P04_-_published.xlsx:3310` | 2026-07-13 | Livity Life Ltd | £50,961.45 | Finance, Property & Procurement |
| 7 | `Over500_2026_P04_-_published.xlsx:784` | 2026-07-10 | E W BEARD LTD | £64,202.50 | Education & SEND |
| 7 | `Over500_2026_P02_-_published.xlsx:674` | 2026-05-20 | E W BEARD LTD | £60,039.70 | Education & SEND |
| 7 | `Over500_2026_P02_-_published.xlsx:675` | 2026-05-20 | E W BEARD LTD | £55,594.00 | Education & SEND |
| 8 | `Over500_2026_P03_-_published.xlsx:183` | 2026-06-03 | Sikandar Hayat t/a Prompt Cars | £73,296.50 | Education & SEND |
| 8 | `Over500_2026_P03_-_published.xlsx:203` | 2026-06-03 | Sikandar Hayat t/a Prompt Cars | £26,085.00 | Education & SEND |
| 8 | `Over500_2026_P03_-_published.xlsx:208` | 2026-06-03 | Sikandar Hayat t/a Prompt Cars | £17,607.50 | Education & SEND |
| 9 | `Over500_2026_P03_-_published.xlsx:661` | 2026-06-08 | ANDY AND ES LIMITED | £59,335.72 | Education & SEND |
| 9 | `Over500_2026_P04_-_published.xlsx:1283` | 2026-07-15 | ANDY AND ES LIMITED | £56,941.82 | Education & SEND |
| 9 | `Over500_2026_P02_-_published.xlsx:670` | 2026-05-13 | ANDY AND ES LIMITED | £54,881.31 | Education & SEND |
| 10 | `Over500_2026_P02_-_published.xlsx:530` | 2026-05-27 | Elior UK PLC | £23,694.03 | Adult Social Care |
| 10 | `Over500_2026_P03_-_published.xlsx:440` | 2026-06-16 | Elior UK PLC | £23,516.69 | Adult Social Care |
| 10 | `Over500_2026_P04_-_published.xlsx:533` | 2026-07-28 | Elior UK PLC | £23,173.08 | Adult Social Care |

**T-03.3. Test.** For each unmatched agency-staff supplier, obtain the managed-service or framework agreement, or the contract, that governs the spend. Establish the route by which it was let, whether a CDP or Find a Tender notice was published or an exemption applies, and whether the register holds an entry. Record the basis if a managed-service or framework route is relied on; do not assume one. [CPR-70, CPR-10, CPR-07, metric:$.tests.off_contract.unmatched_by_tag.agency_staff.suppliers]  
**Evidence to inspect:** Managed-service or framework agreement, notice or exemption record, contract register entry, approval of notice  
**Sample:** 1 item from `off-contract.csv`, where dominant_tag = agency_staff, match_class = none, largest total_gbp first, 5 payments per supplier, (only 1 available); 5 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P03_-_published.xlsx:9` | 2026-06-15 | Comensura Ltd | £107,880.99 | Strategy & Governance |
| 1 | `Over500_2026_P02_-_published.xlsx:5` | 2026-05-12 | Comensura Ltd | £104,728.31 | Strategy & Governance |
| 1 | `Over500_2026_P04_-_published.xlsx:19` | 2026-07-31 | Comensura Ltd | £103,047.79 | Strategy & Governance |
| 1 | `Over500_2026_P03_-_published.xlsx:12` | 2026-06-08 | Comensura Ltd | £101,567.70 | Strategy & Governance |
| 1 | `Over500_2026_P04_-_published.xlsx:6` | 2026-07-15 | Comensura Ltd | £100,668.47 | Strategy & Governance |

**C-03.2. Expected control.** Each award is notified to the Service Lead for Commissioning and Procurement for the Contract Register, and the register and tender invitations are published. [CPR-07, CPR-35, CPR-06] Owner: Relevant Service Director.

**T-03.2. Test.** Enquire how awards reach the Contract Register and how the register and tender invitations are published. Compare the register with the Contracts Finder notice file for completeness, and report any award with no notification or entry. [CPR-07, CPR-35, CPR-06]  
**Evidence to inspect:** Contract register, award notifications, publication records, process description  
**Sample:** Register completeness enquiry and document review; no transaction sample.

**T-03.4. Test.** For each sampled grant payee, obtain the grant agreement and the grant register entry. Establish whether the arrangement is a grant or amounts to a contract under the Rules' definition of entering a contract. Where it does, check that the award was notified for the Contract Register. Where it does not, record the basis for treating it as a grant. [CPR-07, CPR-35, metric:$.tests.off_contract.unmatched_by_tag.grant.suppliers]  
**Evidence to inspect:** Grant agreement, grant register entry, award notification, officer explanation of classification  
**Sample:** 5 items from `off-contract.csv`, where dominant_tag = grant, match_class = none, largest total_gbp first, 2 payments per supplier; 9 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P03_-_published.xlsx:511` | 2026-06-17 | JUBILEE DAY NURSERY | £400,824.68 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:623` | 2026-06-30 | JUBILEE DAY NURSERY | £6,769.87 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P03_-_published.xlsx:2075` | 2026-06-17 | ACRES OF FUN DAY NURSERY AND PRE SCHOOL | £323,872.96 | Education (DSG Funded) & Other Education Grants |
| 3 | `Over500_2026_P03_-_published.xlsx:525` | 2026-06-17 | ROCKING HORSE DAY NURSERY - NEWBURY RACECOURSE PLC | £317,171.95 | Education (DSG Funded) & Other Education Grants |
| 3 | `Over500_2026_P03_-_published.xlsx:620` | 2026-06-30 | ROCKING HORSE DAY NURSERY - NEWBURY RACECOURSE PLC | £3,291.55 | Education (DSG Funded) & Other Education Grants |
| 4 | `Over500_2026_P03_-_published.xlsx:579` | 2026-06-17 | TIGERS DAY NURSERY | £240,841.71 | Education (DSG Funded) & Other Education Grants |
| 4 | `Over500_2026_P04_-_published.xlsx:704` | 2026-07-03 | TIGERS DAY NURSERY | £1,500.00 | Education (DSG Funded) & Other Education Grants |
| 5 | `Over500_2026_P03_-_published.xlsx:2081` | 2026-06-17 | Tigers at Theale Day Nursery | £240,149.35 | Education (DSG Funded) & Other Education Grants |
| 5 | `Over500_2026_P03_-_published.xlsx:634` | 2026-06-30 | Tigers at Theale Day Nursery | £596.16 | Education (DSG Funded) & Other Education Grants |


## R-04: Payments may have been made more than once for the same amount and payee [9 (High; Medium - High)]

**Audit objective.** Conclude whether payments to the same payee for the same amount were valid separate payments or possible duplicates, separately for general procurement and for placements, and whether a pre-payment check operates.

**C-04.1. Expected control.** Written evidence, including electronic evidence, supports every purchase, so that each payment can be agreed to an invoice and order before release. [CPR-32] Owner: Not named in the Rules.

**T-04.1. Test.** General-procurement stratum, same-timestamp tier. For each sampled group, agree every payment to its own invoice, order and receipt. Establish whether the payments are separate valid charges or a repeated payment, and whether a pre-payment check would have caught it. Record any recovery action. [CPR-32, metric:$.tests.duplicates.tiers.same_timestamp.by_tag.general_procurement.rows]  
**Evidence to inspect:** Invoices, orders, receipt records, remittance advices, supplier statements  
**Sample:** 3 items from `duplicates.csv`, where tier = same_timestamp, tag = general_procurement, largest excess_gbp first, one item per supplier_norm; 6 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:601` | 2026-07-13 | Roadside Technologies Ltd | £9,103.64 | Environment |
| 1 | `Over500_2026_P04_-_published.xlsx:740` | 2026-07-13 | Roadside Technologies Ltd | £9,103.64 | Environment |
| 2 | `Over500_2026_P03_-_published.xlsx:2134` | 2026-06-18 | SEISMIC SEWAGE SYSTEMS LTD | £5,360.00 | Environment |
| 2 | `Over500_2026_P03_-_published.xlsx:2141` | 2026-06-18 | SEISMIC SEWAGE SYSTEMS LTD | £5,360.00 | Environment |
| 3 | `Over500_2026_P04_-_published.xlsx:3663` | 2026-07-29 | MAISHA STAFFING SOLUTIONS LTD | £3,737.50 | Children's Social Care |
| 3 | `Over500_2026_P04_-_published.xlsx:3894` | 2026-07-29 | MAISHA STAFFING SOLUTIONS LTD | £3,737.50 | Children's Social Care |

**T-04.2. Test.** General-procurement stratum, different-timestamp tier. For each sampled group, agree every payment to its own invoice, order and receipt. Establish whether it is a separate valid charge or a repeated payment, and whether the pre-payment check would have caught it. [CPR-32, metric:$.tests.duplicates.tiers.different_time.by_tag.general_procurement.rows]  
**Evidence to inspect:** Invoices, orders, receipt records, remittance advices  
**Sample:** 3 items from `duplicates.csv`, where tier = different_time, tag = general_procurement, largest excess_gbp first, one item per supplier_norm, excluding suppliers and rows already drawn in T-04.1; 7 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:3308` | 2026-07-15 | VolkerHighways Ltd | £101,925.86 | Environment |
| 1 | `Over500_2026_P04_-_published.xlsx:618` | 2026-07-17 | VolkerHighways Ltd | £101,925.86 | Environment |
| 2 | `Over500_2026_P02_-_published.xlsx:2160` | 2026-05-12 | TWO SAINTS LTD | £27,147.69 | Development & Housing |
| 2 | `Over500_2026_P02_-_published.xlsx:2161` | 2026-05-13 | TWO SAINTS LTD | £27,147.69 | Development & Housing |
| 3 | `Over500_2026_P04_-_published.xlsx:259` | 2026-07-13 | BROADWAY CARS | £5,330.00 | Education & SEND |
| 3 | `Over500_2026_P04_-_published.xlsx:264` | 2026-07-13 | BROADWAY CARS | £5,330.00 | Education & SEND |
| 3 | `Over500_2026_P04_-_published.xlsx:474` | 2026-07-13 | BROADWAY CARS | £5,330.00 | Education & SEND |

**T-04.3. Test.** Placement stratum, same-timestamp tier. This stratum holds most of the value beyond the first instance, so it carries the larger sample. For each sampled group, agree every payment to the individual service user's invoice and placement record. Establish whether the payments are separate charges, such as different service users at the same fee, or a repeated payment for one individual. [CPR-32, metric:$.tests.duplicates.tiers.same_timestamp.by_tag.care_or_education_placement.rows]  
**Evidence to inspect:** Provider invoices by service user, placement records, remittance advices, provider statements  
**Sample:** 5 items from `duplicates.csv`, where tier = same_timestamp, tag = care_or_education_placement, largest excess_gbp first, one item per supplier_norm; 38 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:1040` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1041` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1071` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1086` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1087` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1105` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1107` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1115` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1154` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1155` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1158` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1825` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1826` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1831` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1846` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1904` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1905` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:2678` | 2026-07-08 | BUPA Care Services | £8,476.52 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:1048` | 2026-07-15 | GCH (Alder) Ltd t/a Hungerford Care Home | £5,700.00 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:1097` | 2026-07-15 | GCH (Alder) Ltd t/a Hungerford Care Home | £5,700.00 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:1114` | 2026-07-15 | GCH (Alder) Ltd t/a Hungerford Care Home | £5,700.00 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:1126` | 2026-07-15 | GCH (Alder) Ltd t/a Hungerford Care Home | £5,700.00 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:1146` | 2026-07-15 | GCH (Alder) Ltd t/a Hungerford Care Home | £5,700.00 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:1917` | 2026-07-15 | GCH (Alder) Ltd t/a Hungerford Care Home | £5,700.00 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:1941` | 2026-07-15 | GCH (Alder) Ltd t/a Hungerford Care Home | £5,700.00 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:1942` | 2026-07-15 | GCH (Alder) Ltd t/a Hungerford Care Home | £5,700.00 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:2023` | 2026-07-15 | GCH (Alder) Ltd t/a Hungerford Care Home | £5,700.00 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:2670` | 2026-07-15 | GCH (Alder) Ltd t/a Hungerford Care Home | £5,700.00 | Adult Social Care |
| 3 | `Over500_2026_P03_-_published.xlsx:1381` | 2026-06-10 | OPTALIS LTD | £6,210.00 | Adult Social Care |
| 3 | `Over500_2026_P03_-_published.xlsx:1471` | 2026-06-10 | OPTALIS LTD | £6,210.00 | Adult Social Care |
| 3 | `Over500_2026_P03_-_published.xlsx:1472` | 2026-06-10 | OPTALIS LTD | £6,210.00 | Adult Social Care |
| 3 | `Over500_2026_P03_-_published.xlsx:2836` | 2026-06-10 | OPTALIS LTD | £6,210.00 | Adult Social Care |
| 3 | `Over500_2026_P03_-_published.xlsx:2837` | 2026-06-10 | OPTALIS LTD | £6,210.00 | Adult Social Care |
| 3 | `Over500_2026_P03_-_published.xlsx:901` | 2026-06-10 | OPTALIS LTD | £6,210.00 | Adult Social Care |
| 4 | `Over500_2026_P04_-_published.xlsx:2229` | 2026-07-01 | Brighter Living Care Ltd | £19,317.76 | Adult Social Care |
| 4 | `Over500_2026_P04_-_published.xlsx:2968` | 2026-07-01 | Brighter Living Care Ltd | £19,317.76 | Adult Social Care |
| 5 | `Over500_2026_P04_-_published.xlsx:2483` | 2026-07-29 | Arch Futures | £18,648.00 | Adult Social Care |
| 5 | `Over500_2026_P04_-_published.xlsx:2572` | 2026-07-29 | Arch Futures | £18,648.00 | Adult Social Care |

**T-04.4. Test.** Placement stratum, different-timestamp tier. This stratum also holds a large share of the value beyond the first instance, so it carries the larger sample. For each sampled group, agree every payment to the individual service user's invoice and placement record. Establish whether each is a separate charge or a repeated payment for one individual. [CPR-32, metric:$.tests.duplicates.tiers.different_time.by_tag.care_or_education_placement.rows]  
**Evidence to inspect:** Provider invoices by service user, placement records, remittance advices  
**Sample:** 5 items from `duplicates.csv`, where tier = different_time, tag = care_or_education_placement, largest excess_gbp first, one item per supplier_norm, excluding suppliers and rows already drawn in T-04.3; 58 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P03_-_published.xlsx:2164` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2165` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2166` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2167` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2189` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2190` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2311` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:3106` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:3107` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2169` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2170` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2312` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2313` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:3109` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2173` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2195` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2315` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2316` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2317` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:3110` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:3111` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2175` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2176` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2199` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2200` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2201` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:3112` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:3113` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2177` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2203` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2204` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2321` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2322` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:2323` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:3114` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 1 | `Over500_2026_P03_-_published.xlsx:3115` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,337.45 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P02_-_published.xlsx:2242` | 2026-05-19 | Phoenix Child Care Limited -The Grange School | £21,988.16 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P02_-_published.xlsx:2243` | 2026-05-19 | Phoenix Child Care Limited -The Grange School | £21,988.16 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P02_-_published.xlsx:2247` | 2026-05-19 | Phoenix Child Care Limited -The Grange School | £21,988.16 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P02_-_published.xlsx:2249` | 2026-05-19 | Phoenix Child Care Limited -The Grange School | £21,988.16 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P02_-_published.xlsx:2252` | 2026-05-19 | Phoenix Child Care Limited -The Grange School | £21,988.16 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P02_-_published.xlsx:2253` | 2026-05-20 | Phoenix Child Care Limited -The Grange School | £21,988.16 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P02_-_published.xlsx:2255` | 2026-05-20 | Phoenix Child Care Limited -The Grange School | £21,988.16 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P02_-_published.xlsx:2257` | 2026-05-20 | Phoenix Child Care Limited -The Grange School | £21,988.16 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P02_-_published.xlsx:2260` | 2026-05-20 | Phoenix Child Care Limited -The Grange School | £21,988.16 | Education (DSG Funded) & Other Education Grants |
| 2 | `Over500_2026_P02_-_published.xlsx:2263` | 2026-05-21 | Phoenix Child Care Limited -The Grange School | £21,988.16 | Education (DSG Funded) & Other Education Grants |
| 3 | `Over500_2026_P03_-_published.xlsx:2157` | 2026-06-03 | Sukhbir Singh and Harvinder Singh T/A Calcot Services for Children (CSFC) | £18,768.75 | Education (DSG Funded) & Other Education Grants |
| 3 | `Over500_2026_P03_-_published.xlsx:2158` | 2026-06-03 | Sukhbir Singh and Harvinder Singh T/A Calcot Services for Children (CSFC) | £18,768.75 | Education (DSG Funded) & Other Education Grants |
| 3 | `Over500_2026_P03_-_published.xlsx:3102` | 2026-06-03 | Sukhbir Singh and Harvinder Singh T/A Calcot Services for Children (CSFC) | £18,768.75 | Education (DSG Funded) & Other Education Grants |
| 3 | `Over500_2026_P03_-_published.xlsx:2159` | 2026-06-03 | Sukhbir Singh and Harvinder Singh T/A Calcot Services for Children (CSFC) | £18,768.75 | Education (DSG Funded) & Other Education Grants |
| 3 | `Over500_2026_P03_-_published.xlsx:3103` | 2026-06-03 | Sukhbir Singh and Harvinder Singh T/A Calcot Services for Children (CSFC) | £18,768.75 | Education (DSG Funded) & Other Education Grants |
| 3 | `Over500_2026_P03_-_published.xlsx:2306` | 2026-06-03 | Sukhbir Singh and Harvinder Singh T/A Calcot Services for Children (CSFC) | £18,768.75 | Education (DSG Funded) & Other Education Grants |
| 4 | `Over500_2026_P02_-_published.xlsx:2266` | 2026-05-26 | Huckleberry House | £30,918.75 | Education (DSG Funded) & Other Education Grants |
| 4 | `Over500_2026_P02_-_published.xlsx:2267` | 2026-05-26 | Huckleberry House | £30,918.75 | Education (DSG Funded) & Other Education Grants |
| 4 | `Over500_2026_P02_-_published.xlsx:2269` | 2026-05-26 | Huckleberry House | £30,918.75 | Education (DSG Funded) & Other Education Grants |
| 5 | `Over500_2026_P03_-_published.xlsx:2008` | 2026-06-16 | Care Services To You | £23,989.77 | Children's Social Care |
| 5 | `Over500_2026_P03_-_published.xlsx:1931` | 2026-06-16 | Care Services To You | £23,989.77 | Children's Social Care |
| 5 | `Over500_2026_P03_-_published.xlsx:3044` | 2026-06-22 | Care Services To You | £23,989.77 | Children's Social Care |


## R-06: Spend may exceed the annual rate of the published award value [6 (Moderate; Moderate)]

**Audit objective.** Conclude whether spend above the annual rate of the published award value is supported by approved variations or extensions, for every supplier eligible for the test.

**C-06.1. Expected control.** Variations of scope are approved in advance by the Monitoring Officer and S151 Officer below the relevant boundary, and by the relevant board above it after an extension report. [CPR-79, CPR-80] Owner: Monitoring Officer and S151 Officer.

**T-06.1. Test.** Every supplier eligible for the test is covered, because the eligible set is small enough to test in full. For each, obtain the award, any variation or extension record and the approval. Compare payments with the award value and term. Note the notice end date in the spend-versus-award file and, where the contract has ended or is close to ending, request the extension evidence. Confirm the approver required for the contract value signed off before the extra spend. [CPR-79, CPR-80, metric:$.tests.spend_vs_award.count]  
**Evidence to inspect:** Contract and award notice, variation or extension records, approval, board report  
**Sample:** 8 items from `spend-vs-award.csv`, largest ratio first, 3 payments per supplier, (only 8 available); 16 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:905` | 2026-07-22 | NEC SOFTWARE SOLUTIONS UK LIMITED | £129,125.00 | Finance, Property & Procurement |
| 1 | `Over500_2026_P04_-_published.xlsx:492` | 2026-07-22 | NEC SOFTWARE SOLUTIONS UK LIMITED | £91,629.15 | Finance, Property & Procurement |
| 1 | `Over500_2026_P04_-_published.xlsx:487` | 2026-07-22 | NEC SOFTWARE SOLUTIONS UK LIMITED | £52,054.00 | Finance, Property & Procurement |
| 2 | `Over500_2026_P03_-_published.xlsx:396` | 2026-06-10 | BookingLab Limited | £24,000.00 | Transformation, Customer & ICT |
| 3 | `Over500_2026_P03_-_published.xlsx:384` | 2026-06-04 | Exacom Systems Ltd | £12,105.85 | Development & Housing |
| 4 | `Over500_2026_P04_-_published.xlsx:1276` | 2026-07-22 | WCL UK Ltd (Trading as Everything ICT) | £102,882.78 | Education & SEND |
| 5 | `Over500_2026_P03_-_published.xlsx:276` | 2026-06-30 | SMS-Environmental Ltd | £2,070.00 | Adult Social Care |
| 5 | `Over500_2026_P04_-_published.xlsx:365` | 2026-07-09 | SMS-Environmental Ltd | £1,335.60 | Adult Social Care |
| 5 | `Over500_2026_P03_-_published.xlsx:29` | 2026-06-22 | SMS-Environmental Ltd | £1,175.00 | Adult Social Care |
| 6 | `Over500_2026_P02_-_published.xlsx:460` | 2026-05-20 | Softcat Ltd | £8,979.02 | Education & SEND |
| 6 | `Over500_2026_P03_-_published.xlsx:375` | 2026-06-17 | Softcat Ltd | £2,025.98 | Transformation, Customer & ICT |
| 7 | `Over500_2026_P03_-_published.xlsx:371` | 2026-06-08 | IDOX SOFTWARE LTD | £48,579.20 | Community Services |
| 7 | `Over500_2026_P02_-_published.xlsx:462` | 2026-05-20 | IDOX SOFTWARE LTD | £2,647.21 | Development & Housing |
| 8 | `Over500_2026_P03_-_published.xlsx:2130` | 2026-06-09 | TWO SAINTS LTD | £38,775.00 | Development & Housing |
| 8 | `Over500_2026_P04_-_published.xlsx:3181` | 2026-07-22 | TWO SAINTS LTD | £38,775.00 | Development & Housing |
| 8 | `Over500_2026_P02_-_published.xlsx:2160` | 2026-05-12 | TWO SAINTS LTD | £27,147.69 | Development & Housing |


## R-07: Waivers, exceptions and approvals may not be fully documented [6 (Moderate; Moderate)]

**Audit objective.** Conclude whether waivers and exceptions are documented, approved by the right officer and made in advance, and which Rules clause governs waiver authority.

**C-07.1. Expected control.** Every waiver or exception is fully documented, supported by a written exception report to the relevant board where competition is not excluded, and approved by the Section Officer for finance (S151 Officer) with recorded reasons. [CPR-25, CPR-26, CPR-27] Owner: S151 Officer.

**T-07.1. Test.** Obtain the waiver and exception register. Select exception reports and confirm each was documented, submitted in advance and carries the finance officer's approval recording that the circumstances were genuinely exceptional. [CPR-25, CPR-26, CPR-27]  
**Evidence to inspect:** Waiver and exception register, exception reports, finance officer approvals  
**Sample:** Document review of the waiver and exception register; items selected on receipt of the register.

**C-07.2. Expected control.** Waivers and exceptions are granted only by the officers the Rules name, in advance and in exceptional circumstances, at the approval level for the contract value. [CPR-19, CPR-20, CPR-21, CPR-22, CPR-23, CPR-24] Owner: Monitoring Officer and/or S151 Officer.

**T-07.2. Test.** Enquire which officers granted each waiver and exception, and check authority, timing and value band against the Rules. Ask management which of the two conflicting waiver-authority clauses it applies, and record the answer for the auditor. [CPR-19, CPR-20, CPR-21, CPR-22, CPR-23, CPR-24]  
**Evidence to inspect:** Waiver and exception register, delegation records, management response on clause conflict  
**Sample:** Enquiry and register review; no transaction sample.

**C-07.3. Expected control.** Contracts excluded from competition or let under a Purchasing Scheme without further competition have prior written Monitoring Officer approval, and board approval where required. [CPR-75, CPR-77, CPR-82] Owner: Monitoring Officer; relevant board.

**T-07.3. Test.** Obtain the list of contracts treated as exempt or let without further competition. For selected items, confirm prior written Monitoring Officer approval and relevant board approval where the contract value required it. [CPR-75, CPR-77, CPR-82]  
**Evidence to inspect:** Exemption list, Monitoring Officer approvals, board minutes  
**Sample:** Document review of exemption list; items selected on receipt.


## R-08: Provider choice for exempt placements may not be recorded [6 (Moderate; Moderate)]

**Audit objective.** Conclude whether the reasons for the choice of provider are recorded for placement payments exempt from competition.

**C-08.1. Expected control.** Service Directors ensure a record of the reasons for the choice of provider is kept on the individual's case notes. [CPR-81] Owner: Service Directors.

**T-08.1. Test.** For each sampled provider, select placements paid in the period and inspect the case notes for a recorded reason for the choice of provider. Note recurring payments and any provider paid across several services. [CPR-81, metric:$.tests.high_value_suppliers.by_tag.care_or_education_placement.suppliers]  
**Evidence to inspect:** Case notes, placement panel or approval records, provider agreement  
**Sample:** 5 items from `high-value-suppliers.csv`, where dominant_tag = care_or_education_placement, largest total_gbp first, 2 payments per supplier; 10 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:1850` | 2026-07-08 | BUPA Care Services | £10,400.00 | Adult Social Care |
| 1 | `Over500_2026_P04_-_published.xlsx:1039` | 2026-07-08 | BUPA Care Services | £9,903.62 | Adult Social Care |
| 2 | `Over500_2026_P04_-_published.xlsx:2320` | 2026-07-08 | Affinity Trust Support Ltd | £28,512.00 | Adult Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:1628` | 2026-06-24 | Affinity Trust Support Ltd | £26,394.66 | Adult Social Care |
| 3 | `Over500_2026_P03_-_published.xlsx:2171` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,534.90 | Education (DSG Funded) & Other Education Grants |
| 3 | `Over500_2026_P03_-_published.xlsx:2172` | 2026-06-17 | Oaklands SEN School Berkshire Limited | £20,534.90 | Education (DSG Funded) & Other Education Grants |
| 4 | `Over500_2026_P02_-_published.xlsx:823` | 2026-05-13 | RUSKIN MILL TRUST | £179,236.76 | Adult Social Care |
| 4 | `Over500_2026_P02_-_published.xlsx:1822` | 2026-05-13 | RUSKIN MILL TRUST | £151,859.86 | Adult Social Care |
| 5 | `Over500_2026_P02_-_published.xlsx:2095` | 2026-05-26 | Amegreen Childrens Services | £36,705.55 | Children's Social Care |
| 5 | `Over500_2026_P04_-_published.xlsx:3080` | 2026-07-17 | Amegreen Childrens Services | £36,705.55 | Children's Social Care |


## R-09: A limited-assurance audit of personal budget payments may bear on payment controls [9 (High; Medium - High)]

**Audit objective.** Conclude whether the weaknesses behind the adverse opinion on personal budget payments have been addressed and whether they bear on supplier payments in scope, including payments to payees that may be direct-payment or prepaid channels.

**C-09.1. Expected control.** Written evidence supports every purchase and payment, and agreed audit actions are implemented and monitored. [CPR-32] Owner: Not named in the Rules.

**T-09.1. Test.** Obtain the agreed actions, owners, due dates and implementation status from the personal budgets audit. Assess whether each weakness could apply to the supplier payments in scope and report any that do. [CPR-32]  
**Evidence to inspect:** Audit report, agreed action tracker, implementation evidence  
**Sample:** Enquiry and document review; no transaction sample.

**T-09.2. Test.** First ask the Council what each sampled payee represents and obtain its payment ledger for the period. The payments are drawn from the full payment history of each payee, not from the flagged value band, so the test can show whether the personal budget weaknesses bear on the channel. Where a payee is a direct-payment, allowance or prepaid-card channel, agree each sampled payment to the personal budget plan, allowance record or invoice, and check whether any weakness from the personal budgets audit applies. Where it is an ordinary purchase, record this for the auditor so the payments can be considered with the route sample. [CPR-32, metric:$.tests.threshold_clustering.tiers[0].count]  
**Evidence to inspect:** Payee descriptions, payee payment ledger, personal budget plans, allowance or top-up records, invoices, reconciliation of the channel to individuals  
**Sample:** 2 items from `supplier-totals.csv`, where supplier_norm = ['E WALLET', 'PREPAID FINANCIAL SERVICES'], largest total_gbp first, 5 payments per supplier; 9 transactions

| # | Row ID | Date | Supplier | Amount | Service |
|---|---|---|---|---|---|
| 1 | `Over500_2026_P04_-_published.xlsx:898` | 2026-07-13 | PREPAID FINANCIAL SERVICES | £1,070.00 | Adult Social Care |
| 1 | `Over500_2026_P02_-_published.xlsx:443` | 2026-05-27 | PREPAID FINANCIAL SERVICES | £1,060.00 | Adult Social Care |
| 1 | `Over500_2026_P02_-_published.xlsx:442` | 2026-05-20 | PREPAID FINANCIAL SERVICES | £1,015.00 | Adult Social Care |
| 1 | `Over500_2026_P03_-_published.xlsx:365` | 2026-06-10 | PREPAID FINANCIAL SERVICES | £1,015.00 | Adult Social Care |
| 1 | `Over500_2026_P02_-_published.xlsx:449` | 2026-05-27 | PREPAID FINANCIAL SERVICES | £1,000.00 | Development & Housing |
| 2 | `Over500_2026_P02_-_published.xlsx:2283` | 2026-05-01 | E-WALLET | £3,000.00 | Children's Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:2633` | 2026-06-17 | E-WALLET | £3,000.00 | Children's Social Care |
| 2 | `Over500_2026_P02_-_published.xlsx:2291` | 2026-05-01 | E-WALLET | £1,000.00 | Children's Social Care |
| 2 | `Over500_2026_P03_-_published.xlsx:3367` | 2026-06-17 | E-WALLET | £1,000.00 | Children's Social Care |


## Prepared-by-client (PBC) request list

Derived from the test steps above. Each item names the tests that need it.

| # | Risk | Item requested | For tests |
|---|---|---|---|
| 1 | R-01 | Orders, requisitions, quotes and approvals for the sampled payments | T-01.1 |
| 2 | R-01 | Schedule of all payments to each sampled payee in the period | T-01.1 |
| 3 | R-01 | Contracts, award notices and requisitions for the sampled payments | T-01.2 |
| 4 | R-01 | Portal invitation records and quotes | T-01.2 |
| 5 | R-01 | Statement of the VAT basis used when banding requirements | T-01.2 |
| 6 | R-02 | Orders, requisitions and quotes for the payments in each sampled window | T-02.1 |
| 7 | R-02 | Contracts, orders and requisitions for each highest-boundary window | T-02.2 |
| 8 | R-02 | Framework or call-off records where relied on | T-02.2 |
| 9 | R-02 | Award decisions, Key Decision notices and board reports for each highest-boundary window | T-02.3 |
| 10 | R-03 | Council contract register extract | T-03.1 |
| 11 | R-03 | Contracts and notices for the sampled suppliers | T-03.1 |
| 12 | R-03 | Record of any exemption or framework call-off relied on | T-03.1 |
| 13 | R-03 | Contract register extract with value, duration and supplier | T-03.2 |
| 14 | R-03 | Award notifications to the Service Lead for Commissioning and Procurement | T-03.2 |
| 15 | R-03 | Published tender invitations list | T-03.2 |
| 16 | R-03 | Agreement governing agency-staff spend and its route to award | T-03.3 |
| 17 | R-03 | Notice, exemption or register entry for that agreement | T-03.3 |
| 18 | R-03 | Grant register for the period | T-03.4 |
| 19 | R-03 | Grant agreements for the sampled payees | T-03.4 |
| 20 | R-04 | Invoices and remittances for the sampled general-procurement groups | T-04.1 |
| 21 | R-04 | Description of any duplicate-payment check before release | T-04.1 |
| 22 | R-04 | Invoices and remittances for the sampled general-procurement groups with differing timestamps | T-04.2 |
| 23 | R-04 | Invoices by service user and remittances for the sampled placement groups | T-04.3 |
| 24 | R-04 | Invoices by service user and remittances for the sampled placement groups with differing timestamps | T-04.4 |
| 25 | R-06 | Contract, award value and term for each eligible supplier | T-06.1 |
| 26 | R-06 | Variation and extension approvals | T-06.1 |
| 27 | R-06 | Extension evidence where the notice end date has passed or is near | T-06.1 |
| 28 | R-07 | Waiver and exception register for the period | T-07.1 |
| 29 | R-07 | Exception reports and approvals for selected items | T-07.1 |
| 30 | R-07 | Scheme of delegation extract | T-07.2 |
| 31 | R-07 | Management statement on waiver authority | T-07.2 |
| 32 | R-07 | List of contracts treated as exempt or let under a Purchasing Scheme | T-07.3 |
| 33 | R-07 | Approval records for selected contracts | T-07.3 |
| 34 | R-08 | Case notes for the sampled placements | T-08.1 |
| 35 | R-08 | Placement approval records | T-08.1 |
| 36 | R-09 | Agreed actions and implementation status from the personal budgets audit | T-09.1 |
| 37 | R-09 | Follow-up monitoring reports | T-09.1 |
| 38 | R-09 | Description of what each sampled payee represents | T-09.2 |
| 39 | R-09 | Payee payment ledger for the period | T-09.2 |
| 40 | R-09 | Personal budget plans or allowance records for the sampled payments | T-09.2 |
| 41 | R-09 | Reconciliation of the channel to individual service users | T-09.2 |
