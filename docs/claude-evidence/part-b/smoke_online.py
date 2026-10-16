"""End-to-end smoke test of the deployed harness in prepared mode (isolated run on the server)."""
import json, sys, time
import requests

BASE = sys.argv[1].rstrip("/")
s = requests.Session()

def show(label, r):
    print(f"{label}: HTTP {r.status_code}")
    if r.status_code >= 400:
        print("  ", r.text[:600]); sys.exit(1)
    return r.json()

print("health:", s.get(BASE + "/health", timeout=60).json())
print("config:", s.get(BASE + "/api/config", timeout=60).json())
started = show("start prepared run", s.post(BASE + "/api/runs", json={"mode": "prepared"}, timeout=60))
rid, token = started["id"], started["token"]
H = {"X-Run-Token": token}

def wait_for(stages, limit=300):
    t0 = time.time()
    while time.time() - t0 < limit:
        st = s.get(f"{BASE}/api/runs/{rid}", headers=H, timeout=60).json()
        if st.get("stage") in stages or st.get("error"):
            return st
        time.sleep(4)
    sys.exit(f"timeout waiting for {stages}")

st = wait_for({"risk-review", "blocked"})
print("stage:", st.get("stage"), "| error:", (st.get("error") or "")[:300])
if st.get("stage") != "risk-review": sys.exit(1)
risks = [r["id"] for r in st.get("risks", st.get("ratings", {}).get("risks", []))] or [f"R-0{i}" for i in range(1, 10)]
print("risks to decide:", risks)
dec = {"reviewer": "SMOKE TEST (Claude) - not an auditor decision",
       "decisions": [{"id": rid_, "decision": "approve", "comment": "Smoke test approval."} for rid_ in risks]}
show("decisions", s.post(f"{BASE}/api/runs/{rid}/decisions", headers=H, json=dec, timeout=120))
show("plan", s.post(f"{BASE}/api/runs/{rid}/plan", headers=H, json={}, timeout=60))
st = wait_for({"sign-off", "blocked", "complete"}, limit=420)
print("stage after planning:", st.get("stage"), "| error:", (st.get("error") or "")[:400])
review = s.get(f"{BASE}/api/runs/{rid}/documents/review.md", headers=H, timeout=60).json()["text"]
print("review verdict line:", [l for l in review.splitlines() if "READY" in l or "BLOCKED" in l][:2])
for doc in ("planning-memo.md", "risk-control-matrix.md", "audit-program.md", "challenges.md"):
    r = s.get(f"{BASE}/api/runs/{rid}/documents/{doc}", headers=H, timeout=60)
    print(f"  {doc}: HTTP {r.status_code}, {len(r.json().get('text', ''))} chars")
show("signoff", s.post(f"{BASE}/api/runs/{rid}/signoff", headers=H, json={"name": "SMOKE TEST (Claude) - not an auditor sign-off"}, timeout=60))
print("final stage:", s.get(f"{BASE}/api/runs/{rid}", headers=H, timeout=60).json().get("stage"))
r = s.get(f"{BASE}/api/runs/{rid}/download", headers=H, timeout=120)
print(f"download: HTTP {r.status_code}, {len(r.content)} bytes, {r.headers.get('Content-Type')}")
