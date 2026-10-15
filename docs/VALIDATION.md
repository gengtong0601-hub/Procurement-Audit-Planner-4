# Local validation record

Prepared on 2026-10-05 (America/Los_Angeles). This record covers the local
implementation, not native Claude execution, a live API run or deployment.

## Automated tests

Final command:

```bash
.venv/bin/python -m pytest -q --basetemp runtime/test-temp
```

**40 passed**: 18 spend/data cases, 12 risk/gate cases, 10 harness cases.
Full result: `docs/qa/test-results.txt`.

Meaningful cases include moving Excel headers, explicit dates, packed
multi-supplier notices, uppercase buyer identity, exact versus near matching,
amount/window boundaries, unresolved parameters, missing input, decision
completeness, real score amendments, rejections, empty approved scope, stale
source inputs, changed plans, malformed JSON, private run tokens and safe
exports. A complete prepared workflow uses copied real evidence and all eight
draft risks, draws samples, passes all four QA checks and signs only as an
explicitly synthetic test reviewer. Tests assert the root human decisions
remain unchanged.

The provider adapter has mocked-response contract tests. No real provider
credential was used. Mocks are not represented as live model verification.

## Source and calculation checks

- Nine original data files match the stored SHA-256 manifest.
- Rule checker: 80 rules, 81 exclusions, four unresolved parameters;
  **ALL CHECKS PASSED**, zero warnings.
- History checker: 106 source-linked items, 81 quotations, four source
  documents; **ALL CHECKS PASSED**.
- Seven independent spot-checks reconcile flagged transactions directly to
  workbook rows and independently recompute selected source totals.
- Register builder: eight risks, zero failures and zero warnings.
- The genuine scope gate intentionally exits with failure: reviewer/date and
  every human decision remain blank, and no approved revision is asserted.

Detailed output: `docs/qa/source-and-gate-checks.txt`. The original input data
was not edited. PDF text and selected source-page images are in
`docs/reference/`; visual checks are listed in `EXTRACTION_NOTES.md`.

## Browser checks

The local application at `http://127.0.0.1:8000` was inspected through a real
browser. The initial page rendered correctly at its default viewport. Starting
a prepared run displayed the correct population, eight risks, unresolved
parameter notice, role activity and working documents. Metric placeholders in
rating justifications resolved to Python-computed values. Blank human input
was rejected. The New review action returned to the start screen. No real
reviewer decision or sign-off was entered through the browser.

JavaScript syntax passed `node --check harness/static/app.js`. No mobile-device
or cross-browser matrix is claimed.

## Outstanding verification

- Teammate: native Claude skill discovery/invocation, actual subagent runs,
  project memory, team messaging/lifecycle and the step-by-step evidence log.
- Human auditor: source spot-checks, unresolved thresholds if needed, every
  risk decision, treatment of open review points, final sign-off.
- Deployment owner: API credentials/model access, real live workflow,
  container build, hosted persistence and external-device smoke test.
- Submitter: publish repository and deployment, then enter their actual URLs.

Docker was unavailable locally, so no container-build success is claimed.
The website's browser checkboxes were not used to certify unperformed Claude
steps. See `CLAUDE_VERIFICATION.md` and `DEPLOYMENT.md` for concrete instructions.
