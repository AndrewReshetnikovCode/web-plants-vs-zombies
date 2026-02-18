# Phase 1 Startup Slice

## What was migrated

This slice extracts the startup sequence from `WinMain` into `app/LawnAppRunner.cpp` and routes the initial resource-path probe through `platform::IFileSystem`.

## Why this matters

- Keeps behavior intact while introducing a platform seam.
- Reduces direct startup coupling to legacy static file helpers.
- Prepares for a future portable `main()` / web runner without touching gameplay loop internals.

## Next wiring step

- Continue replacing direct WinAPI touchpoints in startup-adjacent modules after entry abstraction.
- Wire clock/input/window interfaces into the same startup runner incrementally.
