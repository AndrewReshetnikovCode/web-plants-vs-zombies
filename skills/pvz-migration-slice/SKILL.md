---
name: pvz-migration-slice
description: Use this skill when continuing the web-port migration in this repository to keep work optimized as small vertical slices with explicit Definition of Done, checklist updates, and reproducible validation artifacts.
---

# pvz-migration-slice

Use this workflow for every migration PR to keep progress measurable and low-risk.

## When to use

- User asks to continue migration work.
- You need to optimize process, reduce PR noise, or improve tracking discipline.

## Slice workflow (mandatory)

1. Pick one narrow scope (one seam): entrypoint, timing, input/window, audio route, render route, resource route.
2. Implement only that seam without broad unrelated edits.
3. Update migration docs/checklists in `README.md` to reflect partial/complete status.
4. Produce one reproducible artifact by running:
   - `tools/validation/winapi_inventory.sh`
   - `python3 skills/pvz-migration-slice/scripts/phase_progress.py`
5. Include those command outputs in PR validation section.

## Definition of Done for a slice

- One seam changed in code.
- One doc note added under `docs/phase-1-*.md` (or relevant phase file).
- `README.md` status/checklist updated.
- Validation commands executed.

## Notes

- Prefer additive interfaces and thin adapters first.
- Avoid touching gameplay logic unless the slice explicitly targets it.
- Keep PR title format: `Phase X: <seam> slice`.
