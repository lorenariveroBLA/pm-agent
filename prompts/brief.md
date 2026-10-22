# Brief — daily sprint status report

The prompt a Delivery Manager gives pm-agent almost every day, built on the 5 prompting principles (S1).

```
Context: I manage the <KEY> board at PrescriberPoint. The team runs Scrum
(two-week sprints). Holidays this sprint: <none | dates>.
Absences: <none | who and which days>.

Task: Run Mode 1 (Sprint Status & Hygiene) on the active sprint of <KEY>.

Use: the Atlassian MCP for Jira (read-only), Python for every number,
and decisions.md for the board setup from previous runs.

Constraints: read-only; no invented data; cite issue keys; no ranking
of people; English.

Done when: the 8-section report is complete, report-critic returns PASS,
and a new entry is appended to decisions.md.
```

| Principle | Where |
|---|---|
| Single responsibility | One mode, one board, one sprint |
| Context first | Board, cadence, holidays, absences |
| Tool directives | Atlassian MCP, Python, decisions.md |
| Definition of done | 8 sections + critic PASS + memory entry |
| No filler | Direct instructions only |
