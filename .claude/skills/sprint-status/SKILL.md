---
name: sprint-status
description: Mode 1 — Sprint Status & Hygiene report for a Jira Scrum board (hygiene, scope change, progress, feasibility, sprint goal). Use when the manager asks how the current sprint is going.
---

# Mode 1 — Sprint Status & Hygiene

## Context
The manager wants to know how the current sprint is going: whether the board data is healthy, and whether the sprint will finish well and meet its goal.

## Task
Produce the Sprint Report for the active sprint (or the one named) with hygiene, scope changes, progress, feasibility and sprint goal assessment.

## Use
- Board: resolved from the board URL (see CLAUDE.md). Base JQL: `project = <KEY> AND sprint in openSprints()` (or `sprint = "<name>"`); when the board filters more than one project, use the board's sprints via `executeRead` instead.
- Sprint field → name, dates, goal.
- Sprint field changelog of each issue → detect issues added after `startDate`.
- History: the last 3–6 closed sprints of the board, for reference velocity.

## How to compute the hard numbers
Jira keeps no snapshot of a sprint, so reconstruct it from changelogs:
- **SP at start:** issues that were in the sprint at `startDate`, using each issue's SP value *as of `startDate`* (estimates change mid-sprint; take the value from the SP field changelog).
- **Added:** issues whose Sprint field gained this sprint after `startDate`. Use their SP at the time they were added.
- **Removed:** issues whose Sprint field lost this sprint after `startDate`. Candidate set: `project = <KEY> AND updated >= "<startDate>"`, then check each changelog. Try the sprint report via `discover` first; if neither works, list it as missing data. Never estimate it.
- **Estimate changes:** SP changed mid-sprint on issues that stayed. Report them separately; they are not scope added or removed.
- **Velocity (per closed sprint):** SP of issues in Done status category whose resolution date is on or before the sprint's complete date. Completed SP, not committed SP.

## Steps
1. **Identification:** sprint name, dates, total / elapsed / remaining working days, % of time elapsed.
2. **Hygiene** (list keys in every case):
   - Unassigned issues.
   - Issues without SP (exclude subtasks, and bugs if the team does not estimate them; state the rule).
   - Issues without a parent (count only; full analysis belongs to a future mode).
   - To Do issues with no movement after more than 50% of the sprint has elapsed.
   - In Progress issues with no status change for more than 3 working days (bugs) or 5 working days (other types), measured from the status changelog, not from `updated`.
   - Parent/child inconsistency inside the sprint: a parent in Done with children not Done.
3. **Scope changes:**
   - SP at start, SP added, SP removed, current SP.
   - % scope change = (added + removed) / SP at start.
   - List of added and removed keys, with dates.
4. **Progress:**
   - SP Done / In Progress / To Do and % complete.
   - Compare % complete with % of time elapsed.
5. **Feasibility:**
   - Projected remaining capacity = average daily velocity (average velocity of the last closed sprints ÷ working days per sprint) × remaining working days, adjusted for the reported absences.
   - Compare it with pending SP.
   - Show this sprint's velocity trend against the previous closed sprints (↑ / ↓ / →).
6. **Verdict:** evaluate both criteria; **the worse color wins**.
   - 🟢 On track: gap (% time − % complete) ≤ 10 pp **and** pending SP ≤ projected capacity.
   - 🟡 At risk: gap between 10 and 25 pp, **or** pending SP up to 120% of capacity.
   - 🔴 Off track: gap > 25 pp, **or** pending SP > 120% of capacity.
   - Without history, use only the gap and mark confidence as low.
7. **Sprint goal:**
   - No goal → hygiene finding; recommend writing one.
   - Goal present → identify the issues that support it by matching the goal text against issue summaries and parents. This is always an inference: label it as such and list the matched keys so the manager can correct them.
   - Assess those issues' status. Verdict: Met / At risk / Not met, with 1–2 lines of reasoning.
8. **Recommendations:** at most 5, actionable, prioritized. Examples: "Estimate PROJ-12 and PROJ-15 before the daily", "Negotiate pulling PROJ-40 (5 SP) out to protect the goal". Each one has three parts:
   - **What:** the concrete actions, as bullets with issue keys.
   - **Why:** the finding and number that call for it.
   - **How it helps:** the effect on this sprint (focus, forecast, goal, board accuracy).

## Constraints
- Do not assume everything not Done will fail: an In Progress ticket with fewer than 2 days in that status (from the status changelog) counts as probable progress, but not as complete.
- Do not mix the active sprint with future sprints.
- If the board has more than one active sprint, ask which one to analyze, or analyze each separately.

## Done when
A report with these sections, in this order:
1. **Verdict:** a 3-column table with Sprint status (🟢/🟡/🔴), Sprint goal (🟢 Met / 🟡 At risk / 🔴 Not met) and Confidence, each with its one-line reason.
2. **Executive summary** (≤ 120 words), as labeled bullets (Progress, Scope, Fit, Blocked, Goal, Decision needed), not a paragraph.
3. **Numbers table:** SP start / added / removed / estimate changes / current / Done / pending, % time, % complete, projected capacity, velocity trend.
4. **Hygiene:** one table per finding type, with keys.
5. **Scope changes:** table with key, SP, added/removed, date.
6. **Sprint goal:** the goal, the linked issues (marked as inferred) and the verdict.
7. **Recommendations:** ≤ 5, each with What / Why / How it helps.
8. **Assumptions and missing data.**

Writing style for the report and the artifact: bullets over paragraphs. No paragraph longer than 2 sentences; break reasoning (goal verdict, summary, notes) into bullets.

## Human-friendly view (artifact)
After report-critic returns PASS, publish the same report as an Artifact for the manager:
- Show every metric and finding from the 8 sections: three prominent verdict cards at the top (Sprint status, Sprint goal, Confidence, each colored by its status with 2–3 bullet reasons), the executive summary as bullets, numbers as stat tiles, progress vs. time chart, hygiene and scope tables with issue keys, sprint goal verdict as bullets, recommendations with What / Why / How it helps, assumptions as bullets.
- Same numbers as the text report; nothing new, nothing rounded differently.
- One artifact per sprint. If `decisions.md` already lists an artifact URL for this board URL and sprint, update that artifact in place; otherwise create a new one in the same style and record its URL in the run entry.
