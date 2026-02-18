# Phase 1 Startup Seam Guards

## What was added

- Added validation script: `tools/validation/startup_seam_guard.py`.
- Added supporting guard scripts used by the same migration loop:
  - `tools/validation/window_seam_guard.py`
  - `tools/validation/input_seam_guard.py`
  - `tools/validation/clock_seam_guard.py`
  - `tools/validation/runner_lifecycle_guard.py`

## What they verify

- `RunLawnApp(...)` signature keeps required startup abstraction parameters:
  - `IFileSystem`
  - `IClock`
  - `IWindow`
  - `IInput`
- `main.cpp` keeps matching desktop adapter injection and forwards all seam dependencies.
- `RunLawnApp(...)` startup path keeps:
  - window size/fullscreen handoff via `IWindow`,
  - startup input marker via `IInput`,
  - startup/shutdown timing markers via `IClock`,
  - stable lifecycle ordering and cleanup (`delete` + null reset).

## Why this matters

These guards are lightweight guardrails to prevent accidental regressions while iterating on startup migration slices.

## Repair baseline

The startup seam baseline currently relies on one shared desktop entry path (`RunDesktopEntry()`), then delegates to `RunLawnApp(fileSystem, clock, window, input)` for platform seam routing.
