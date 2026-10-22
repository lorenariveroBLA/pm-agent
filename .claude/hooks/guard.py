#!/usr/bin/env python3
"""PreToolUse guard: keep pm-agent read-only on Jira and away from secrets.

Exit code 2 blocks the tool call and shows the reason to Claude.
"""
import json
import re
import sys

event = json.load(sys.stdin)
tool = event.get("tool_name", "")
tool_input = json.dumps(event.get("tool_input", {}))

# 1. Jira is read-only: block any Atlassian MCP tool that writes.
WRITE_VERBS = r"^(create|edit|update|transition|add|delete|remove|executeWrite|executeDestructive)"
name = tool.removeprefix("mcp__atlassian__")
if tool.startswith("mcp__atlassian__") and re.search(WRITE_VERBS, name, re.IGNORECASE):
    print(f"BLOCKED by guard hook: {tool} writes to Jira. pm-agent is read-only; "
          "propose the change as a recommendation instead.", file=sys.stderr)
    sys.exit(2)

# 2. Secrets: block reads/edits of .env and credential files.
SECRET_PATHS = r"(\.env\b|credentials|\.pem\b|id_rsa|\.netrc|secrets?\.)"
if tool in ("Read", "Edit", "Write", "Bash", "Grep", "Glob") and re.search(SECRET_PATHS, tool_input, re.IGNORECASE):
    print("BLOCKED by guard hook: access to .env or credential files is not allowed.", file=sys.stderr)
    sys.exit(2)

sys.exit(0)
