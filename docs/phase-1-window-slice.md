# Phase 1 Window/Input Slice

## What was migrated

- Extended `RunLawnApp(...)` to accept both `platform::IWindow&` and `platform::IInput&` in startup path.
- Injected `DesktopWindowAdapter` and `DesktopInputAdapter` from `main.cpp` into the shared runner call.
- Routed startup-level interface seams through abstractions:
  - `IWindow::SetTitle(...)`
  - `IWindow::SetCursorVisible(...)`
  - Startup window size routing via `IWindow::GetSize(...)` into `LawnApp` dimensions
  - Startup fullscreen mode routing via `IWindow::SetFullscreen(...)` after init config
  - Startup input probe + marker log via `IInput::IsMouseButtonDown(...)`, `IInput::GetMouseX()`, and `IInput::GetMouseY()`

## Why this matters

- Starts replacing startup-adjacent window/input behavior with platform abstractions.
- Keeps migration incremental and low-risk while maintaining one runner path.
- Prepares equivalent operations for web adapters later.

## Next wiring step

- Expand beyond startup marker probes by routing one gameplay-path input read through `IInput`.
- Expand guard coverage further once window mode toggles are routed beyond startup path.


## Guardrail update

- Added `tools/validation/window_seam_guard.py` to enforce startup window size/fullscreen seam expectations in `RunLawnApp(...)`.
- Added `tools/validation/input_seam_guard.py` to enforce startup input marker seam usage through `IInput`.
