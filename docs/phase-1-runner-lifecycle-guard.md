# Phase 1 Runner Lifecycle Guard

## Purpose

Protect startup runner call order and cleanup behavior while migration churn is high.

## Guard script

- `tools/validation/runner_lifecycle_guard.py`

## Contract protected by the guard

The guard enforces that these lifecycle steps are present and remain in order:

1. window title set,
2. startup input marker log,
3. startup window size probe,
4. `LawnApp` allocation,
5. `LawnApp::Init()`,
6. fullscreen handoff,
7. startup ready marker,
8. app `Start()`,
9. app `Shutdown()`,
10. shutdown marker,
11. app deletion,
12. global pointer reset to `nullptr`.

## Why this matters

- Prevents accidental reorder regressions during seam refactors.
- Ensures cleanup remains explicit and deterministic.
- Keeps startup migration work auditable via simple static checks.

## Operational usage

This guard is executed through:

- `tools/validation/validate_slice.sh`
- `tools/validation/build_lanes.sh`

No separate command is needed in normal loop execution.
