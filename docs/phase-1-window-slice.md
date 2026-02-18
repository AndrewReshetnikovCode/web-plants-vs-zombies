# Phase 1 Window/Input Slice

## What was migrated

- Extended `RunLawnApp(...)` to accept both `platform::IWindow&` and `platform::IInput&` in startup path.
- Injected `DesktopWindowAdapter` and `DesktopInputAdapter` from `main.cpp` into the shared runner call.
- Routed startup-level interface seams through abstractions:
  - `IWindow::SetTitle(...)`
  - `IWindow::SetCursorVisible(...)`
  - `IWindow::SetFullscreen(...)`
  - `IWindow::GetSize(...)` mapped into `LawnApp::mWidth/mHeight`
  - `IInput::IsKeyDown(...)` marker call

## Why this matters

- Starts replacing startup-adjacent window/input behavior with platform abstractions.
- Keeps migration incremental and low-risk while maintaining one runner path.
- Prepares equivalent operations for web adapters later.

## Next wiring step

- Route additional mode decisions through `IWindow` as they are migrated from legacy startup paths.
- Replace one real startup-adjacent input touchpoint with `IInput` (beyond marker call).
