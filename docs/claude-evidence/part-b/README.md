# Part B: deployed independent harness

| | |
|---|---|
| URL | https://procurement-audit-studio-8xno.onrender.com |
| Host | Render, free web service (Docker), built from `render.yaml` on `main` of this repository (commit `3ae69fa`) |
| Deployed | 2026-10-15 by the student (Render account login and Blueprint creation are theirs) |
| Mode available | Prepared-evidence mode, which needs no secrets. Live mode is off because no API key is configured |

## Hosted end-to-end check

[smoke-test.txt](smoke-test.txt) shows a run of [smoke_online.py](smoke_online.py) against the public URL.
It covers `/health`, then a new prepared run, the 9-risk register, approval of all nine
(reviewer clearly labelled `SMOKE TEST (Claude)`), planning, QA verdict **READY FOR SIGN-OFF
(4/4)**, the memo, matrix, program and challenges documents, sign-off (labelled as a smoke test),
stage `complete` and the zip download. Each run is isolated on the server; the repository's
signed-off outputs are unchanged.

Free-plan limits: the service sleeps when idle, so the first request can take about a minute,
and runs are lost on restart because there is no persistent disk.

## Live mode (Claude API)

- [live-sonnet-run-2](live-sonnet-run-2/README.md): Sonnet 5.5, end to end, QA 4/4, signed off.
- [live-sonnet-run-1-blocked](live-sonnet-run-1-blocked/README.md): the earlier blocked run and its fix.
