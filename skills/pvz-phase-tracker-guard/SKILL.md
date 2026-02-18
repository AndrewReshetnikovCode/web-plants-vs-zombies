---
name: pvz-phase-tracker-guard
description: Use this skill to keep README migration checklists and phase progress snapshots in sync and to catch malformed phase/checklist sections before PR.
---

# pvz-phase-tracker-guard

## When to use

- Any PR that edits migration docs, checklists, or phase claims.

## Workflow

1. Run `python3 tools/validation/phase_tracker_guard.py`.
2. Run `tools/validation/phase_progress.sh`.
3. Include outputs in PR validation notes.
