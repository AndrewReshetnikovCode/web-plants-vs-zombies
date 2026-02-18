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

## Repair update

- Rewired `main.cpp` to inject `DesktopFileSystemAdapter`, `DesktopClockAdapter`, `DesktopWindowAdapter`, and `DesktopInputAdapter` through one `RunDesktopEntry()` path.
- Expanded `RunLawnApp(...)` signature in `app/LawnAppRunner.h`/`.cpp` to require `IFileSystem`, `IClock`, `IWindow`, and `IInput`.
- Added a non-Windows `main(...)` fallback that reuses the same runner wiring as `WinMain(...)`.

This brings the code back in sync with the startup seam guard contract and Phase 1 docs.
