# 交接给 Claude Code：审阅结论与下一步

> **状态更新（2026-10-15）：** 本文件第三节的两个问题已在提交 `436c77a` 修复，第四节的教程步骤已在 Claude Code 中全部完成并签核。最新情况和证据见 [README](../README.md#guide-completion-confirmation) 与 `docs/claude-evidence/`。以下为当时的交接原文，保留备查。

> 2026-10-15 审阅本项目后写成。在 Claude Code 里打开本文件夹后，先让它读这份文件（见第五节的开场提示词）。

## 一、在 Claude Code 里开始

1. VS Code → File → Open Folder → 选 `procurement-audit-planner 2`。
2. Terminal → New Terminal，运行：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
claude
```

3. Claude Code 启动后，粘贴第五节的开场提示词。

## 二、项目现状

| 部分 | 状态 |
|---|---|
| 3 个 Skills、6 个 Agents 定义 | 已有，在 `.claude/skills/`、`.claude/agents/` |
| rules.json（80 条规则）、analytics、history.json、风险登记表草稿（8 条风险） | 已有，由 Codex 在本地生成 |
| 在 Claude Code 里真正运行过 Skills / 子智能体 / Agent team | **没有**（README 自己写明由 Codex 准备） |
| 人工审批 `outputs/auditor-comments.md` | 空白：审批人、日期、8 条决定都没填 |
| 最终规划包（planning-memo / risk-control-matrix / audit-program / review） | 正式 `outputs/` 里还不存在 |
| 网页 harness（Part B） | 本地能跑；演示模式能从头走到签核（需避开下面的问题 1） |
| GitHub 仓库 / 部署网址 | 都还没有 |

## 三、已发现的问题

### 问题 1：装了 Poppler 后，16 条规则引文核对失败，网页流程卡住

- `verify_quotes.py` 在有 `pdftotext` 时优先用它读 PDF；但 `outputs/rules.json` 里的引文是从 pypdf 的文本摘出来的，带着 pypdf 的拆字痕迹（例如 `in ac cordance`、`Service Lead f or`、`“ Seal”`）。
- 结果：CPR-02、03、10、21、26、27、29、34、35、36、43、46、47、56、57、67 共 16 条报 `quote NOT FOUND`。
- 影响：教程 Setup 会让你装 Poppler，所以按教程操作就会触发；网页启动的第一步就是这个检查，会直接 blocked。Docker 镜像里没有 Poppler，部署后不受影响。
- 修复方向：
  - `verify_quotes.py`、`scripts/checks/check_quotes.py`、`harness/workflow.py` 用一致的方式读 PDF，并且比对时忽略空白差异，让两种提取器都能通过；
  - 在 guide 2.2 原生运行 `/extract-rules` 时，重新生成干净的引文；
  - 修完后在"有 pdftotext"和"没有 pdftotext"两种情况下各跑一遍核对。

### 问题 2：`outputs/gate-evidence.json` 用绝对路径记录哈希

- `.claude/skills/audit-program/build_pack.py` 用 `str(path.resolve())` 作为键；现在文件里是队友电脑上的路径 `/Users/leyanyu/Documents/ChatGPT/440-2 HW2/...`。
- 目前 `ready: false`，审批后会重写，所以暂时不出错；但在你的电脑上关闭审批门以后，只要换文件夹或别人 clone 仓库，门检查就会因为路径不同而失败。
- 修复方向：改成相对项目根目录的路径。

### 备注

- 审阅环境里没装 pytest，没有重跑他记录的 40 个测试；修完后请跑 `make test` 确认。
- 演示模式端到端测试（审批 7 条、拒绝 1 条，审批人用 `TEST REVIEWER`）：规划包生成、四项 QA 检查通过、签核完成。这次测试在隔离环境里进行，没有改动正式 `outputs/`。

## 四、建议顺序

1. **修问题 1、2**，跑 `make verify` 和 `make test`。
2. **按教程在 Claude Code 里真正跑一遍**（Part A 的核心）。对照 `docs/CLAUDE_VERIFICATION.md` 和课程网站逐步做，每步截图存到 `docs/claude-evidence/`：
   - 2.2 `/extract-rules`
   - 3.2 `Run the spend-analyst.`、3.4 `Run the findings-analyst.`、3.6–3.7 risk-assessor
   - 4.x 人工审批：**由你本人**在 `outputs/auditor-comments.md` 填审批人、日期，并对每条风险选 approve / amend / reject；之后让 risk-assessor 应用这些决定
   - 5.x Agent team：planner、challenger、qa-reviewer；最后由你在 `outputs/review.md` 签核
3. **更新 README** 的 Submission status 和 Guide completion confirmation，写上真实日期和证据链接。
4. **上传 GitHub**（不要上传 `.venv`、`runtime/`、`.env`），把仓库网址填进 README。→ 提交 Part A
5. **部署 Part B**：按 `docs/DEPLOYMENT.md` 操作。
   - `render.yaml` 里的 `starter` 是付费方案。免费方案通常不带持久磁盘，服务重启后运行记录会丢失。
   - 部署后先检查 `/health`，再在公网网址上把演示模式完整走一遍。
   - 如果要用实时模式，在平台后台设置 `ANTHROPIC_API_KEY`、`ANTHROPIC_MODEL`、`HARNESS_ACCESS_TOKEN`。
   - 把网址填进 README。→ 提交 Part B

## 五、开场提示词（复制粘贴到 Claude Code）

```text
Read CLAUDE.md, README.md, docs/CLAUDE_VERIFICATION.md and docs/HANDOFF-claude-code.md.
Summarise the three skills, six agents and two human gates, and tell me which guide
steps still need a native Claude Code run. Inspect existing files; do not recreate or
overwrite working implementations.

Then fix the two problems in section 三 of docs/HANDOFF-claude-code.md:
1. Quote verification must pass whether or not pdftotext is installed
   (verify_quotes.py, scripts/checks/check_quotes.py, harness/workflow.py).
2. gate-evidence.json must store paths relative to the project root.
Explain each fix before applying it, then run `make verify` and `make test`,
with and without pdftotext on PATH. Do not fill in auditor decisions or sign-off.
请用中文回复。
```
