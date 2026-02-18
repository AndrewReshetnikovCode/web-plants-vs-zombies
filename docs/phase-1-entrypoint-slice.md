# Phase 1 Entrypoint Slice

## What was migrated

- `main.cpp` now exposes a shared startup dispatcher (`RunDesktopEntry`) that both entry forms call.
- On Windows builds, `WinMain(...)` remains the active entrypoint.
- On non-Windows builds, a fallback `main(...)` entrypoint now delegates to the same startup dispatcher.

## Why this matters

- Introduces a portable entrypoint seam without changing startup/gameplay behavior.
- Keeps one startup path (`RunLawnApp(...)`) for both entrypoint forms.
- Reduces future refactor cost for web/non-Win32 launchers.

## Notes

This does **not** make the project cross-platform yet; the codebase still contains many WinAPI/DirectX dependencies. It only removes the hard requirement that entry wiring must be `WinMain`-only.
