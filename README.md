# pm-agent — Sprint Status kit

A Claude Code kit that writes the daily **Sprint Status & Hygiene** report for a Jira Scrum board: hygiene findings, scope change, progress vs. time, feasibility against past velocity, and the sprint goal verdict. Read-only on Jira.

## What's inside

| Block | File | Role |
|---|---|---|
| S1 Prompting | `prompts/brief.md` | The daily prompt, built on the 5 principles |
| S2 Workspace | `CLAUDE.md` | Agent role, board setup, constraints |
| S3 Skill | `.claude/skills/sprint-status/SKILL.md` | Mode 1: steps, formulas, report format |
| S3 Hook | `.claude/hooks/guard.py` + `.claude/settings.json` | Blocks Jira writes and access to `.env`/credentials |
| S4 Subagent | `.claude/agents/report-critic.md` | Read-only reviewer: sections, keys, math, verdict rule |
| S4 Memory | `decisions.md` | Run log + board setup cache |
| S5 MCP | `mcp-atlassian.json` | Atlassian MCP, the only server loaded |

## Install (≈5 min)
1. Requirements: Claude Code, Python 3, a PrescriberPoint Atlassian account.
2. Copy or clone this folder.
3. In a terminal, inside the folder: `./start.sh`
4. Type `/mcp`, pick **atlassian**, and authenticate in the browser.

## Run
1. Copy the prompt from `prompts/brief.md`, fill in `<KEY>`, holidays and absences, and paste it.
2. Approve the Jira read calls when asked (any write call is blocked by the hook).
3. The report comes back after `report-critic` passes, and a new entry lands in `decisions.md`.

## Versioning
No git in this environment. Before each work session run `./snapshot.sh "label"`: it saves a full copy of the kit to `../pm-agent-versions/` and logs it in `CHANGELOG.md`. To restore, copy a snapshot folder back over `pm-agent/`. Inside a session, Claude Code's `/rewind` undoes recent edits.

## Guardrails
- Read-only: the hook blocks any Atlassian tool that creates, edits, transitions, comments or deletes.
- No secrets: the hook blocks reads and edits of `.env` and credential files.
- Findings are about process, never about individuals.
