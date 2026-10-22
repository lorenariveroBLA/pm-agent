# measure.md — run timing log

One row per pm-agent run. Times come from the session transcript (`~/.claude/projects/<project>/<session>.jsonl`), not from memory:
- **Start** = timestamp of the user message that launched the run.
- **End** = timestamp of the final report reply (critic PASS + artifact published + `decisions.md` entry written).
- **Duration** = End − Start, computed in Python. Local time is the machine's clock (UTC−3).
- **By hand** = how long the same report takes manually (fill in when known).

| Date | Board | Sprint | Mode | Session | Start (local) | End (local) | Duration (min) | By hand (min) | /context before → after | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-21 | DAT | Oct B - Governance Groundwork | 1 | c40c5165 | not captured | not captured | not captured | | not captured | Run 1; timing not logged |
| 2026-10-22 | DAT | Oct B - Governance Groundwork | 1 | 637146bb / 3e50f71b | 16:08:59 | 16:22:17 | 13.3 | | 10% (95k) → 31% (312.9k) | Run 2 via prompts/brief.md; critic PASS; artifact updated |
| 2026-10-22 | DAT | Oct B - Governance Groundwork | 1 | 3e50f71b | 17:10:34 | 17:13:40 | 3.1 | | not captured | Run 3; incremental refresh (no Jira changes since run 2); critic PASS on first review; artifact v6 |
| 2026-10-22 | DAT | Oct B - Governance Groundwork | 1 | 61677400 | 17:34:57 | 17:37:49 | 2.9 | | not captured | Run 4; incremental refresh found DAT-2022 (+8 SP); critic PASS first review; artifact v7. Start = first tool call |
| 2026-10-22 | DAT | Oct B - Governance Groundwork | 1 | current | 17:39:24 | ~17:41 | ~1.5 | | → 7% (71.7k) | Run 5; no-change check, run 4 report stands |
| 2026-10-22 | DAT | Oct B - Governance Groundwork | 1 | e839b4b2 | 17:50:54 | 17:52:55 | 2.0 | | 8% (77.8k) → 12% (115.7k) | Run 7 via brief; no-change refresh of run 4; critic PASS; artifact v7 kept |
