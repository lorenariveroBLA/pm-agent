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

### DAT — https://team-1625057440965.atlassian.net/jira/software/c/projects/DAT/boards/1809 (verified 2026-10-21, run 1)
- Board "Data Product" (id 1809), Scrum, project DAT. cloudId `7c906d30-c1f8-4539-97a4-a5dec982b02e`.
- Story Points = `customfield_10026`; Sprint = `customfield_10020`; Epic Link = `customfield_10014`.
- Hierarchy: Initiative → Epic → Story/Improvement/Spike/Bug → Sub-task. SP live at story level only.
- Extra statuses: Backlog, Ready for Development (To Do category); Blocked, Ready For Release (In Progress category).
- Artifacts: Oct B - Governance Groundwork → https://claude.ai/artifact/KrAqL4j6iAnZo6S4hH7vm1
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
- Output: report + "DAT Oct B Sprint Report" artifact https://claude.ai/artifact/KrAqL4j6iAnZo6S4hH7vm1 (human-friendly view, requested after the report).
- Manager decision:

### 2026-10-22 — DAT — Oct B - Governance Groundwork (run 2)
- Mode: 1 Sprint Status & Hygiene, active sprint, via `prompts/brief.md`. Inputs: holidays not given (assumed none, after the manager declined the question prompt); absence: one team member OoO Fri Oct 16 → Fri Oct 23.
- Run time: 13.3 min (16:08:59 → 16:22:17 local, see measure.md). By hand: __ min
- /context before → after: 10% (95k) → 31% (312.9k)
- Critic: PASS (4 minor notes, all applied; one was a real miscount, 8 → 9 open Brand Insights issues)
- Result: 🔴 Off track (24.0% done vs 55.6% time, gap 31.6 pp; 228 SP pending vs ~63 SP run-rate, low confidence). Goal: At risk (25.3% of 91 goal SP).
- What broke: the kit's `atlassian` MCP wasn't loaded (the session wasn't started with start.sh), so the claude.ai connector was used and the guard hook didn't cover it. One changelog subagent was reported "failed" but had already written its file (verified 41/41 keys). The scratchpad dir disappeared mid-run, so data moved to `runs/2026-10-22-DAT/`. There is no sprint report via MCP; removals to the backlog (206 candidates) were not checked. The calendar changed from run 1 (10 → 9 working days, excluding Oct 29, which ends at 09:00 ET).
- Board setup learned: sprint 1617's earlier name is "Oct B - Governance"; "Oct B - Governance 2" is a different sprint, so match by exact name. The removal scan of future sprints 1619/1620 works (86 issues, 3 removals found).
- Output: `runs/2026-10-22-DAT/report.md`; artifact updated in place: https://claude.ai/artifact/KrAqL4j6iAnZo6S4hH7vm1 (files/index.html v4; Oct 21 datasets relabelled as superseded).
- Manager feedback on the deliverable (applied the same day, written into the sprint-status skill): bullets instead of paragraphs; verdict cards for sprint status, goal and confidence; each recommendation gets What / Why / How it helps. Re-review: critic FAIL, then PASS. The FAIL caught a recommendation that named a Done issue (DAT-3773) and an unsupported claim about the verdict.
- Manager decision:

### 2026-10-22 — DAT — Oct B - Governance Groundwork (run 3)
- Mode: 1 Sprint Status & Hygiene via `prompts/brief.md`. Board from the new `profile.local.json` (created this run from this session's inputs; holidays saved as assumed none, since they were never answered).
- Run time: 3.1 min (17:10:34 → 17:13:40 local, see measure.md). By hand: __ min
- /context before → after: not captured
- Critic: PASS on the first review; 3 optional notes applied (rec 5 effect is on issue counts, not SP; "inferred" labels on goal-linked figures; why the goal is At risk and not Not met).
- Result: unchanged from run 2: 🔴 Off track, goal 🟡 At risk, low confidence.
- What worked: an incremental refresh. Diffing the new snapshot against run 2 found only DAT-4198 and DAT-4209 updated, and neither had new history, so 82 changelog fetches were skipped. Future sprints updated since 15:00 ET: only DAT-4216, never in sprint 1617.
- Output: `runs/2026-10-22-DAT-r3/report.md`; artifact files/index.html v6.
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
