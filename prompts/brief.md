# Brief — daily sprint status report

The prompt a Delivery Manager gives pm-agent almost every day, built on the 5 prompting principles (S1).

```
Context: I am the Delivery Manager of the DAT board at PrescriberPoint.
I check sprint status almost daily to decide fast when priorities or pace
change. The team runs Scrum (two-week sprints). 
Holidays this sprint: should be explicitly asked for the sprint. 
Absences: should be explicitly asked for the sprint. 

Task: Run Mode 1 (Sprint Status & Hygiene) on the active sprint of DAT and
present that one report in two forms: text and artifact.

Use: the sprint-status skill for the steps and format; the Atlassian MCP
for Jira (read-only); Python for every number; decisions.md for the board
setup and the sprint's artifact URL; the report-critic subagent to review
the report; the Artifact tool for the human-friendly view.

Constraints: read-only on Jira; no invented data; cite issue keys; no
ranking of people; English.

Done when: the 8-section report is complete, report-critic returns PASS,
the artifact shows the same metrics and findings, and a new entry is
appended to decisions.md.
```

| Principle | Where |
|---|---|
| Single responsibility | One mode, one board, one sprint; the artifact is the same report, not a new task |
| Context first | Who asks and why (daily DM decisions), board, cadence, holidays, absences |
| Tool directives | sprint-status skill, Atlassian MCP, Python, decisions.md, report-critic, Artifact tool |
| Definition of done | 8 sections + critic PASS + matching artifact + memory entry |
| No filler | Direct instructions only |
