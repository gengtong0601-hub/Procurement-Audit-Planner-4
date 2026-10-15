# Guide lesson 1 (Setup) and prerequisites

| | |
|---|---|
| Date | 2026-10-15 |
| Environment | Claude Code desktop app (Code tab) on macOS, model Claude Opus 5.5, opened on this project folder |

The project folder, `CLAUDE.md` brief, data and empty folders were first prepared by a teammate
with Codex (commit `caebffd`). This session took that folder as its starting point and checked
each setup step in Claude Code before running lessons 2–5.

| Guide item | What was done or checked in Claude Code |
|---|---|
| Prerequisite: VS Code | Not used. The work ran in the Claude Code desktop app, which provides the same project folder, file view and terminal tools. |
| Prerequisite: Claude Code installed and signed in | Claude Code desktop app, signed in. The CLI (`claude`) is not installed on this machine; see lesson 5 for why that mattered. |
| 1.1 Folder open in Claude Code | Session opened on `procurement-audit-planner 2`. The repository was initialised in git (`caebffd`). |
| 1.2 Project brief | Claude Code loaded `CLAUDE.md` at session start and summarised the system, skills, agents and both human gates before any work. |
| 1.3 Data | All nine source files are in `data/`. Their SHA-256 hashes were re-checked against `data/manifest.json`: **9 match, 0 mismatch**. |
| 1.4 Python and tools | `.venv` created with `python3 -m venv .venv` and `pip install -r requirements.txt` (pandas, openpyxl, pypdf, Flask, pytest). Poppler (`pdftotext`, `pdftoppm`) was installed into a temporary conda environment for this session. The quote verifiers also work with pypdf alone (commit `436c77a`). |
| 1.5 Folders | `.claude/skills/`, `.claude/agents/`, `scripts/` and `outputs/` exist. Claude Code discovered the three skills (`/extract-rules` is user-invocable) and all six agents as named sub-agent types without extra configuration. |
