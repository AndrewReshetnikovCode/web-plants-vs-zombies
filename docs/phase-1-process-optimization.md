# Phase 1 Process Optimization

## Applied optimization

A repository-local skill was added to enforce small vertical-slice PR workflow:

- Skill: `skills/pvz-migration-slice/SKILL.md`
- Progress script: `skills/pvz-migration-slice/scripts/phase_progress.py`
- Validation wrapper: `tools/validation/phase_progress.sh`

## Enforced per-slice DoD

- single seam per PR,
- doc update,
- checklist update,
- reproducible validation artifacts.

## Immediate usage

Run:

- `tools/validation/winapi_inventory.sh`
- `tools/validation/phase_progress.sh`
