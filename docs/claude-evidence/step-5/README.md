# Guide lesson 5: the agent team

| | |
|---|---|
| Date | 2026-10-15 |
| Lead | Claude Code (desktop app), main session Claude Opus 5.5, at the user's request |
| Auditor | Tony (sign-off is the auditor's; Claude never fills it) |

## 5.1 Close the gate

The guide's 5.1 approves any still-blank decisions. Here every decision had already been recorded
in step 4.2 and applied in 4.3, so nothing was blank.
[5.1-gate.txt](5.1-gate.txt): `gate closed: register revision 1, 9 decisions by Tony dated
2026-10-15`. In scope: R-02 (9), R-03 (12), R-04 (6), R-05 (4), R-06 (6), R-07 (6), R-08 (4).
Not in scope: R-01, R-09 (approved as rated). Exit 0.

## 5.2 Enable agent teams

`.claude/settings.json` holds `"env": {"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"}`, and the
running session's environment shows `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

## 5.3–5.6 Skill, teammates and checks, compared with the guide's copies

| File | Compared with the guide |
|---|---|
| `.claude/agents/planner.md` | identical |
| `.claude/agents/qa-reviewer.md` | identical |
| `.claude/agents/challenger.md` | identical except the quoted YAML `description` |
| `.claude/skills/audit-program/SKILL.md` | identical except the quoted YAML `description` |
| `.claude/skills/audit-program/build_pack.py` | 94% similar: gate hardening and validation before rendering (docs/IMPLEMENTATION_NOTES.md), plus relative hash keys (commit `436c77a`) |
| `scripts/checks/run_checks.py` | identical |
| `scripts/checks/check_quotes.py`, `check_numbers.py`, `check_trace.py`, `check_samples.py` | 90–97% similar: documented hardening (missing-artifact failures, sample-path safety), relative proof keys |

## 5.7 Run the team

The lead spawned `planner`, `challenger` and `qa-reviewer` as named background agents from
their files in `.claude/agents/`. Each was told the other two names, that the gate is closed,
and the in-scope risks. The planner started at once; the other two wait for `PACK READY v1`.
They were told to message each other with SendMessage and to report `NO TEAM MESSAGING`, not
simulate a teammate, if messaging is unavailable to them.

### What happened (attempt 1)

All three returned **NO TEAM MESSAGING**. In this Claude Code desktop session, agents spawned
with the Agent tool get only the tools in their definition (plus a hand-back to the lead). They
have neither SendMessage nor ToolSearch, so teammates cannot message each other, even with
`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` set. Following their instructions, challenger and
qa-reviewer stopped without writing anything or simulating a teammate.

The planner built pack v1 without the team protocol: 7 approved risks planned (R-02 to R-08),
10 controls, 12 tests, 139 sampled transactions in 8 sample files, 34 of 82 rules cited, and
48 rules listed as not tested with reasons. The builder reported 0 warnings and 0 failures, and
`pack-validation.json` has `ready: true`. No PACK READY was delivered, no challenge round took place, and no QA
review was written.

The lead ran `scripts/checks/run_checks.py` read-only on v1 (no `review.md` written): quotes 0 failures,
numbers 152 figures checked with 0 failures, samples 139 transactions found in the workbooks,
trace 1 failure (`challenges.md` absent, because the challenger could not run). Verdict: BLOCKED (3/4).

This is the case `docs/CLAUDE_VERIFICATION.md` anticipates: if the installed environment does not
support native agent teams, record it and do not present sequential or relayed calls as native
teammates.

### Attempt 2: lead-relayed team (auditor's choice, option A)

The auditor chose to finish the team run with the lead relaying messages. Every teammate
message went through the lead **verbatim**: [relay-log.md](relay-log.md) has 14 entries. One
message was withheld and logged with its reason; none was edited. Each teammate kept its own
context, read and wrote only the files it owns, and made its own judgments. **This is a relayed
team run, not native agent-team messaging.**

| Version | Trigger | Controls | Tests | Sampled transactions | Rules cited | Snapshot |
|---|---|---|---|---|---|---|
| v1 | planner's first build | 10 | 12 | 139 | 34/82 | [v1/](v1/) |
| v2 | round one, `CHALLENGE #1`–`#8` | 11 | 14 | 158 | 36/82 | [v2/](v2/) |
| v3 | round two, `CHALLENGE #9`–`#12` | 11 | 15 | 172 | 36/82 | [v3/](v3/) |

- `PLANNER DONE v3`. In scope R-05, R-06, R-03, R-08, R-02, R-04 and R-07 (plan order); R-01 and
  R-09 are out of scope. 10 sample files, 24 PBC items.
- `CHALLENGER DONE`. Of 12 challenges, 10 are resolved, 0 declined, 0 open, and 2 are **for the
  auditor**: #5 (placement scope; memo says "Placement spend is exempt from competition", which
  overstates CPR-81) and #11 (R-08 likelihood of 1 despite unmatched suppliers above the Key
  Decision value). The challenger also recorded for the auditor that v3 dropped two register
  caveats from the memo limitations.
- `QA DONE: READY FOR SIGN-OFF`: 4/4. `outputs/review.md` was written with the sign-off block blank.

### Lead's independent checks

- [qa-rerun-by-lead.txt](qa-rerun-by-lead.txt): the lead reran `run_checks.py` and got READY FOR SIGN-OFF
  (4/4), exit 0.
- A rebuild with `build_pack.py` leaves all 10 sample files and the pack documents byte-identical.
- The `review.md` sign-off block is blank (signed off by, date, decision, comment).
  `challenges.md` has 10 resolved and 2 for the auditor.
- [pytest.txt](pytest.txt): 47 passed, 1 failed. This is the known Part B harness prepared-mode
  test (step 4.3 README), and it is unrelated to the pack.

## 5.8 Sign off

The auditor gave the sign-off in chat and asked Claude to record it:

> signed off by Tony, 日期 2026-10-15 decision sign off通过

Claude wrote exactly those three fields into `outputs/review.md`: "Signed off by: Tony", "Date:
2026-10-15" and "Decision: sign off". Comment is left blank because none was given. No other line of the file
changed, and QA still reports READY FOR SIGN-OFF (4/4) after the edit. The auditor signed off v3
as it stands, with challenges #5 and #11 recorded "for the auditor" in `outputs/challenges.md`.
