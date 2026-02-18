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


## Expanded validation skills

Added repo-local skills for broader migration validation coverage:

- `skills/pvz-winapi-budget-check/SKILL.md` (B: WinAPI regression budget checks)
- `skills/pvz-runtime-baseline-check/SKILL.md` (C: runtime baseline capture status checks)
- `skills/pvz-build-lane-validation/SKILL.md` (D: quick lane + optional full build lane)
- `skills/pvz-phase-tracker-guard/SKILL.md` (E: README phase/checklist consistency guard)

## Wrapped command bundles

- `tools/validation/validate_slice.sh` wraps:
  - `python3 tools/validation/startup_seam_guard.py`
  - `tools/validation/winapi_inventory.sh`
  - `tools/validation/phase_progress.sh`
- `tools/validation/build_lanes.sh` runs quick lane checks and optional full CMake build lane (`RUN_FULL_BUILD=1`).

- `tools/validation/validate_slice.sh` now also runs `python3 tools/validation/window_seam_guard.py`.
