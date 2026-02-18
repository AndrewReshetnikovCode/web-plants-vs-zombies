# Phase 1 Clock Slice

## What was migrated

- Extended `RunLawnApp(...)` to accept `platform::IClock&` in addition to `platform::IFileSystem&`.
- Wired `DesktopClockAdapter` from `main.cpp` into the shared startup dispatcher path.
- Added startup and lifecycle timing markers in startup runner:
  - `startupBeginMs` sampled before startup platform hooks,
  - `startupReadyMs` sampled after `LawnApp::Init()`,
  - `startupDeltaMs` derived as guarded `startupReadyMs - startupBeginMs`,
  - `shutdownDoneMs` sampled after app shutdown.
- Emitted logs through the seam only (`TodTraceAndLog(...)` with values from `IClock::NowMilliseconds()`).

## Why this matters

- Keeps timing collection behind the platform abstraction seam.
- Makes startup and shutdown timing externally observable without adding new runtime dependencies.
- Provides stable markers for future desktop/web parity checks.

## Next wiring step

- Route one gameplay-path timing read through `IClock` rather than only startup/teardown markers.
- Add a future per-frame timing seam once rendering migration starts.

## Guardrail update

- Added `tools/validation/clock_seam_guard.py` to enforce timing marker presence and startup duration derivation contract.
