# Phase 1 Startup Seam Guard

## What was added

- Added validation script: `tools/validation/startup_seam_guard.py`.

## What it verifies

- `RunLawnApp(...)` signature keeps required startup abstraction parameters:
  - `IFileSystem`
  - `IClock`
  - `IWindow`
  - `IInput`
- `main.cpp` keeps matching desktop adapter injection and forwards all seam dependencies.

## Why this matters

This is a lightweight guardrail to prevent accidental regressions while iterating on startup migration slices.
