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
