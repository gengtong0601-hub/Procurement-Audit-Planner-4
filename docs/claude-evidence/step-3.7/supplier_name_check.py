"""Check that no supplier name appears in the risk text of risk-ratings.json / risk-register.md.

Names come from every spend row (kept and excluded) and every notice supplier, both as
printed and normalised. Text fields and the register are uppercased with non-alphanumerics
collapsed to spaces, then searched for each name as a whole phrase.
Usage: python supplier_names.py PROJECT_ROOT
"""
import csv, json, re, sys
from pathlib import Path

root = Path(sys.argv[1])
full = root / "outputs/analytics-full"
squash = lambda s: " " + re.sub(r"[^A-Z0-9]+", " ", str(s).upper()).strip() + " "

names = set()
for f, cols in (("spend-clean.csv", ("Supplier name", "supplier_norm")), ("spend-excluded.csv", ("Supplier name", "supplier_norm")),
                ("notices-clean.csv", ("Supplier name", "supplier_norm"))):
    for row in csv.DictReader((full / f).open(encoding="utf-8")):
        for c in cols:
            n = squash(row.get(c, "")).strip()
            if len(n) >= 4 and n != "REDACTED":
                names.add(n)
print(f"supplier names checked: {len(names)}")

ratings = json.loads((root / "outputs/risk-ratings.json").read_text())
fields = []
for r in ratings["risks"]:
    for key in ("title", "statement", "proposed_focus", "scope_reason"):
        if r.get(key): fields.append((f"{r['id']}.{key}", r[key]))
    for part in ("likelihood", "impact"):
        fields.append((f"{r['id']}.{part}.justification", r[part]["justification"]))
for x in ratings.get("excluded", []):
    fields.append((f"excluded.{x.get('id', x.get('theme', '?'))}", x.get("reason", "")))
register = (root / "outputs/risk-register.md").read_text(encoding="utf-8")
# Register body excluding quoted rule text (verbatim CPR quotes may legitimately contain any words).
register_risk_text = "\n".join(l for l in register.splitlines() if not l.startswith("- [rule:"))
fields.append(("risk-register.md (excluding rule quotes)", register_risk_text))

hits = []
for where, text in fields:
    t = squash(text)
    for n in names:
        if f" {n} " in t:
            hits.append((where, n))
print(f"text fields checked: {len(fields)}")
for where, n in sorted(hits):
    print(f"HIT  {where}: {n}")
print(f"SUMMARY supplier-name hits={len(hits)}")
sys.exit(1 if hits else 0)
