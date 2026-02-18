# Phase 1 Clock Slice

## What was migrated

- Extended `RunLawnApp(...)` to accept `platform::IClock&` in addition to `platform::IFileSystem&`.
- Wired `DesktopClockAdapter` from `main.cpp` into the shared startup dispatcher path.
- Added a startup-ready timing marker (`startupReadyMs`) after `LawnApp::Init()` for future runtime-baseline logging.

## Why this matters

- Moves startup timing dependency behind the platform abstraction layer.
- Advances the timing checklist item without changing gameplay loop behavior.
- Prepares for platform-specific timing implementations (desktop/web) with one call path.

## Next wiring step

- Expose startup timing marker to baseline docs/log collection workflow.
- Begin routing selected input/window startup interactions through interfaces.


## Follow-up update

- Startup ready marker is now emitted through `TodTraceAndLog(...)` in `RunLawnApp(...)` using `IClock::NowMilliseconds()`.
- This keeps startup timing collection on the platform abstraction seam and makes baseline capture reproducible from logs.
