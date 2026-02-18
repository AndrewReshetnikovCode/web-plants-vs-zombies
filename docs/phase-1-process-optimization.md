# Phase 1 Process Optimization

## Applied optimization

Use one seam-focused vertical slice per PR and keep a fixed Definition of Done.

## Enforced per-slice DoD

- one seam-focused production code change,
- docs/checklist update,
- reproducible validation artifacts.

## Core command wrappers

- `tools/validation/validate_slice.sh`
  - startup seam guard
  - window seam guard
  - input seam guard
  - clock seam guard
  - runner lifecycle guard
  - WinAPI inventory
  - phase progress snapshot
- `tools/validation/build_lanes.sh`
  - quick validation lane (always)
  - optional full build lane (`RUN_FULL_BUILD=1`)

## Optional skillized wrapper

- `skills/pvz-core-migration-loop/scripts/run_core_cycle.sh`
  - runs the full migration validation order used in PR checks.

This keeps the migration loop fast while preserving minimum safety checks.
