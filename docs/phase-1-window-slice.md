# Phase 1 Window/Input Slice

## What was migrated

- Extended `RunLawnApp(...)` to accept both `platform::IWindow&` and `platform::IInput&` in startup path.
- Injected `DesktopWindowAdapter` and `DesktopInputAdapter` from `main.cpp` into the shared runner call.
- Routed startup-level interface seams through abstractions:
  - `IWindow::SetTitle(...)`
  - `IWindow::SetCursorVisible(...)`
  - `IInput::IsKeyDown(...)` marker call

## Why this matters

- Starts replacing startup-adjacent window/input behavior with platform abstractions.
- Keeps migration incremental and low-risk while maintaining one runner path.
- Prepares equivalent operations for web adapters later.

## Next wiring step

- Route fullscreen/window mode decisions through `IWindow`.
- Replace one real startup-adjacent input touchpoint with `IInput`.
