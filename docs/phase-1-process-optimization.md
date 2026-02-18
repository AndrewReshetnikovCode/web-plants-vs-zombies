# Phase 1 Process Optimization

## Applied optimization

Use one small vertical slice per PR and keep a fixed Definition of Done.

## Enforced per-slice DoD

- single seam-focused code change,
- docs/checklist update,
- reproducible validation artifacts.

## Core command wrappers

- `tools/validation/validate_slice.sh`
  - startup seam guard
  - window seam guard
  - input seam guard
  - WinAPI inventory
  - phase progress snapshot
- `tools/validation/build_lanes.sh`
  - quick validation lane (always)
  - optional full build lane (`RUN_FULL_BUILD=1`)

This keeps the migration loop fast while preserving minimum safety checks.
