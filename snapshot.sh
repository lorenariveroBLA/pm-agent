#!/bin/zsh
# Lightweight version control without git: copies the kit into ../pm-agent-versions/<timestamp>-<label>/
# and logs the entry in CHANGELOG.md. Usage: ./snapshot.sh "short label"
KIT="${0:A:h}"
LABEL="${1:-snapshot}"
STAMP="$(date +%Y-%m-%d_%H%M)"
DEST="${KIT:h}/pm-agent-versions/${STAMP}-${LABEL// /-}"
mkdir -p "$DEST"
rsync -a --exclude ".DS_Store" "$KIT/" "$DEST/"
echo "- ${STAMP} — ${LABEL} → pm-agent-versions/${STAMP}-${LABEL// /-}" >> "$KIT/CHANGELOG.md"
echo "Saved: $DEST"
