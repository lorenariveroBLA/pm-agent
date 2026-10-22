# decisions.md — pm-agent run log (memory)

One entry per run. pm-agent reads this before each run to reuse the board setup.

## Baseline (by hand)
- Date:
- Task: sprint status report for <board>
- Time by hand: __ min (estimate from the last manual report, not a fresh measurement)

### Why this task
A Delivery Manager (DM) needs to check sprint status almost daily to make fast, accurate decisions when priorities shift or the team's pace calls for it. In a chaotic sprint, for example, the right call may be to let one complex task slip so many others can finish and the sprint closes in better shape.

The DM needs a quick status that shows:
- how well the sprint is tracking against its goal and the overall roadmap;
- the current slippage and the likely risks, stated as precisely as possible.

### How estimates are treated
Estimates are the perception of experts, or of whoever will do the work, about how long a work item will take or how much effort it needs. Estimating most of the work items in a body of work gives a very high-level projected due date. That projection always carries an uncertainty buffer, which usually stays at or above 50% on top of the effort the developer or owner estimated.

### Scope decision for Mode 1
Mode 1 covers sprint status against the sprint goal only. Two needs above are deliberately left for future modes:
- roadmap alignment;
- due-date projection with the ≥50% uncertainty buffer.

## Board setup cache
<!-- pm-agent fills this on the first run per board: SP field, Sprint field, hierarchy, team type -->

### DAT (verified 2026-10-21, run 1)
- Board "Data Product" (id 1809), Scrum, project DAT. cloudId `7c906d30-c1f8-4539-97a4-a5dec982b02e`.
- Story Points = `customfield_10026`; Sprint = `customfield_10020`; Epic Link = `customfield_10014`.
- Hierarchy: Initiative → Epic → Story/Improvement/Spike/Bug → Sub-task. SP live at story level only.
- Extra statuses: Backlog, Ready for Development (To Do category); Blocked, Ready For Release (In Progress category).
- Board restarted Oct 2026: "Oct A - Nashville Takeaways" (1535) was a cleanup sprint (1 SP resolved), not usable as velocity. 2025 sprints are a different era. "Oct B - Governance Groundwork" (1617, 2026-10-16 → 10-29) is the 2nd sprint → low confidence on any projection.
- The team estimates in bulk after sprint start (whole sprint estimated 2026-10-19), so "SP at startDate" reads 0; use the first-estimate baseline and say so.
- Removal check via `updated >= start` returns ~750 issues (bulk edits); scan next-sprint issues instead.

## Runs

### 2026-10-21 — DAT — Oct B - Governance Groundwork (run 1)
- Mode: 1 Sprint Status & Hygiene, active sprint. Input: no holidays; one team member out of office this week.
- Run time: __ min (by hand: __ min)
- /context before → after: not captured
- Critic: not available yet (subagent added on 2026-10-22)
- What broke: SP-at-start reconstruction failed (bulk estimation after start); removal detection too broad (~750 candidates); the session used the claude.ai Atlassian connector instead of the kit's MCP; board setup was saved to Claude's auto-memory instead of this file.
- Output: report + "DAT Oct B Sprint Report" artifact (human-friendly view, requested after the report).
- Manager decision:

<!--
### YYYY-MM-DD — <board> — <sprint>
- Mode: 1 Sprint Status & Hygiene
- Run time: __ min (by hand: __ min)
- /context before → after: __% → __%
- Critic: PASS | FAIL (items)
- What broke:
- Manager decision:
-->
