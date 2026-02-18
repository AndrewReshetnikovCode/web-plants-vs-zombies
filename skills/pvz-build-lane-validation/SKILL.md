---
name: pvz-build-lane-validation
description: Use this skill to validate changes through two lanes: always-on no-network seam checks and optional full CMake build lane when dependencies/network are available.
---

# pvz-build-lane-validation

## When to use

- Every migration PR to keep validation deterministic in restricted environments.

## Workflow

1. Run `tools/validation/build_lanes.sh`.
2. For full build lane on capable runners, use `RUN_FULL_BUILD=1 tools/validation/build_lanes.sh`.
3. Report lane status (quick lane pass, full lane pass/skip/fail).
