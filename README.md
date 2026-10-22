# pm-agent — Sprint Status kit

A Claude Code kit that writes the daily **Sprint Status & Hygiene** report for any Jira Scrum board you point it at by URL: hygiene findings, scope change, progress vs. time, feasibility against past velocity, and the sprint goal verdict. Read-only on Jira.

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
1. Requirements: Claude Code, Python 3, and an Atlassian account with Browse access to the board you want to analyze.
2. Copy or clone this folder.
3. In a terminal, inside the folder: `./start.sh`
4. Type `/mcp`, pick **atlassian**, and sign in with **your own** Atlassian account. The kit inherits your Jira permissions: it sees only the sites and boards you can see. No site, board or `cloudId` is hardcoded.

## Run
1. Paste the prompt from `prompts/brief.md`. On the first run the agent asks for your board URL (e.g. `https://<site>.atlassian.net/jira/software/c/projects/<KEY>/boards/<ID>`); on the first run of each sprint it asks for holidays and absences. Answers are saved in `profile.local.json` (yours only, git-ignored), so later runs need no questions. To switch boards, put the new URL in the prompt.
2. Approve the Jira read calls when asked (any write call is blocked by the hook).
3. The report comes back after `report-critic` passes, and a new entry lands in `decisions.md`.

## What you get
An 8-section sprint report in the terminal (verdict, executive summary, numbers, hygiene, scope changes, sprint goal, recommendations, assumptions), the same report as a human-friendly Artifact on claude.ai (private to you by default), and a new run entry in `decisions.md`.

## Troubleshooting
| Symptom | Fix |
|---|---|
| `/mcp` shows "connection timed out" | Run `/mcp` again and reconnect **atlassian**. |
| "Input must be provided…" or "Unknown command" | Claude was started outside an interactive terminal or with the wrong flags. Open a new Terminal window and run `./start.sh`. |
| "BLOCKED by guard hook" | Intended: the kit is read-only on Jira. The agent turns the change into a recommendation. |
| "Your Atlassian account has no access to <URL>" | Your account cannot browse that board. Ask the board admin for access, or check you signed in to the right Atlassian account in `/mcp`. |
| The agent does not find `sprint-status` or `report-critic` | Start it with `./start.sh` from inside the kit folder; it loads the project's `.claude/` settings. |

## Versioning
Git holds the kit's history: commit before and after each run. As an extra local backup, `./snapshot.sh "label"` saves a full copy of the kit to `../pm-agent-versions/` and logs it in `CHANGELOG.md`. Inside a session, Claude Code's `/rewind` undoes recent edits.

## Guardrails
- Read-only: the hook blocks any Atlassian tool that creates, edits, transitions, comments or deletes.
- No secrets: the hook blocks reads and edits of `.env` and credential files.
- Findings are about process, never about individuals.
