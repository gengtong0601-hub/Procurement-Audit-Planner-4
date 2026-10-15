"""Independent reconciliation of the spend-analyst outputs to the raw workbooks.

Reads data/spend/*.xlsx with openpyxl (not pandas, not the project's scripts),
keys every data row by "<file>:<excel row>", and checks analytics outputs
against it. Prints counts and mismatches only; no data rows.
Usage: python reconcile.py PROJECT_ROOT
"""
import csv, json, sys
from collections import Counter
from datetime import datetime, date
from decimal import Decimal
from pathlib import Path

import openpyxl

root = Path(sys.argv[1])
EXPECTED = ["Service", "Expenditure category", "Narrative", "Date", "Net amount", "Supplier name"]
raw = {}
for f in sorted((root / "data/spend").glob("*.xlsx")):
    ws = openpyxl.load_workbook(f, read_only=True, data_only=True)["Data to publish"]
    header_at = None
    for i, row in enumerate(ws.iter_rows(values_only=True), start=1):
        cells = [str(c).strip() if c is not None else "" for c in row]
        if header_at is None:
            if cells[:6] == EXPECTED:
                header_at = i
            continue
        if not any(cells[:6]):
            continue
        d = row[3]
        d = d.date() if isinstance(d, datetime) else datetime.strptime(str(d).split()[0], "%m/%d/%y").date()
        raw[f"{f.name}:{i}"] = {"amount": Decimal(str(row[4])).quantize(Decimal("0.01")), "supplier": str(row[5]).strip(),
                                "date": d, "narrative": str(row[2] or ""), "service": str(row[0] or "")}
    print(f"{f.name}: header row {header_at}")

fails = []
def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + (f"  [{detail}]" if detail else ""))
    if not ok:
        fails.append(label)

an = json.loads((root / "outputs/analytics.json").read_text())
pop = an.get("population", {})
total = sum(r["amount"] for r in raw.values())
redacted = sum(1 for r in raw.values() if r["supplier"].casefold() == "redacted")
check("rows_raw matches raw workbooks", pop.get("rows_raw") == len(raw), f"json={pop.get('rows_raw')} raw={len(raw)}")
json_total = pop.get("total_gbp_raw", pop.get("total_gbp"))
print(f"INFO raw total £{total}; analytics population total fields: { {k: v for k, v in pop.items() if 'gbp' in k and not isinstance(v, dict)} }")
excl = pop.get("excluded", {}).get("redacted_supplier", {})
check("redacted_supplier exclusion rows match", excl.get("rows") == redacted, f"json={excl.get('rows')} raw={redacted}")
months = {(r["date"].year, r["date"].month) for r in raw.values()}
check("months_covered matches", pop.get("months_covered") == len(months), f"json={pop.get('months_covered')} raw={len(months)}")

full = root / "outputs/analytics-full"
def rows(name):
    p = full / name
    return list(csv.DictReader(p.open(encoding="utf-8"))) if p.exists() else None

def ids(cell):
    return [x for x in (cell or "").split(";") if x]

# Every flagged single payment exists with the stated amount.
tc = rows("threshold-clustering.csv")
if tc is None:
    check("threshold-clustering.csv present", False)
else:
    bad = [r["row_id"] for r in tc if r["row_id"] not in raw or raw[r["row_id"]]["amount"] != Decimal(r["Net amount"]).quantize(Decimal("0.01"))]
    check(f"threshold_clustering: {len(tc)} flagged rows exist with same amount", not bad, f"bad={bad[:5]}")
    out = [r["row_id"] for r in tc if not (Decimal("0.9") * Decimal(r["threshold"]) <= raw[r["row_id"]]["amount"] <= Decimal(r["threshold"]))]
    check("threshold_clustering: every amount within [0.9T, T]", not out, f"bad={out[:5]}")

for name, kind in (("split-purchases.csv", "split"), ("duplicates.csv", "dup")):
    groups = rows(name)
    if groups is None:
        check(f"{name} present", False)
        continue
    bad = Counter()
    for g in groups:
        members = ids(g.get("row_ids"))
        if any(m not in raw for m in members):
            bad["row_id missing in workbook"] += 1
            continue
        amts = [raw[m]["amount"] for m in members]
        dates = [raw[m]["date"] for m in members]
        if len(members) != int(g["n_payments"]):
            bad["n_payments differs from row_ids"] += 1
        if sum(amts) != Decimal(g["total_gbp"]).quantize(Decimal("0.01")):
            bad["re-summed total differs"] += 1
        span = (max(dates) - min(dates)).days
        if kind == "split":
            # Exclusive thresholds ("above £1,000") trigger one penny above T.
            trigger = Decimal(g["effective_trigger_pence"]) / 100
            if not all(a < trigger for a in amts): bad["a payment reaches the trigger"] += 1
            if sum(amts) < trigger: bad["window total below the trigger"] += 1
            if span > 29: bad["dates span more than 30 days"] += 1
        else:
            if len(set(amts)) != 1: bad["amounts not identical"] += 1
            if span > 7: bad["dates span more than 7 days"] += 1
    check(f"{kind}: {len(groups)} groups reconcile to raw rows (sum, n, amounts, date span)", not bad, dict(bad))

# Council notices in contracts.csv, counted independently.
with (root / "data/contracts.csv").open(encoding="utf-8-sig") as fh:
    notices = list(csv.DictReader(fh))
council = [n for n in notices if n.get("Organisation Name", "").strip().casefold() in {"west berkshire council", "west berkshire"}]
c = an.get("contracts", {})
check("contracts.csv rows_in_file", c.get("rows_in_file") == len(notices), f"json={c.get('rows_in_file')} raw={len(notices)}")
check("contracts.csv rows_for_council", c.get("rows_for_council") == len(council), f"json={c.get('rows_for_council')} raw={len(council)}")

print(f"\nSUMMARY failures={len(fails)}")
sys.exit(1 if fails else 0)
