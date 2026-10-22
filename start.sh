#!/bin/zsh
# Launch Claude Code in the CURRENT folder in near-vanilla mode:
# only project settings (this kit's hooks; no personal plugins) and only the Atlassian MCP. Built-in commands (/mcp, /context, /usage) stay on.
claude --setting-sources project --strict-mcp-config --mcp-config "${0:A:h}/mcp-atlassian.json" "$@"
