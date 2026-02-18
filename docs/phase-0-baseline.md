# Phase 0 Baseline & Inventory Report

## Scope

This report establishes the first-pass WinAPI/DirectX dependency inventory and baseline acceptance targets for the web migration.

## Dependency inventory (current snapshot)

Pattern scan was run across `*.h`, `*.hpp`, `*.c`, `*.cpp` files.

- `#include <windows.h>` occurrences: **13**
- `#include <ddraw.h>` occurrences: **4**
- `#include <d3d.h>` occurrences: **4**
- `HWND` token occurrences: **94**
- `HINSTANCE` token occurrences: **8**
- `WinMain` token occurrences: **1**

### Highest-impact `HWND` hotspots

Top files by `HWND` frequency:

1. `SexyAppFramework/SexyAppBase.cpp` (23)
2. `SexyAppFramework/misc/SEHCatcher.cpp` (17)
3. `SexyAppFramework/unused/scrnsave.c` (15)
4. `SexyAppFramework/misc/SEHCatcher.h` (6)
5. `SexyAppFramework/graphics/DDInterface.h` (3)
6. `SexyAppFramework/SexyAppBase.h` (3)

## Initial migration implications

- The entrypoint is still Windows-specific (`WinMain`), so app bootstrap abstraction remains a hard gate for Phase 1.
- Graphics stack still directly references DirectDraw/Direct3D headers, confirming renderer replacement/adapter work is required for web.
- `HWND` is still present in core app framework and sound/graphics interfaces, so platform adapter seams should start in `platform/interfaces` and be integrated from these hotspots outward.

## Baseline acceptance targets (for parity tracking)

Use these metrics in subsequent PRs to evaluate whether migration preserves behavior:

- **Logic parity**: deterministic level replay checksum stable on desktop baseline.
- **Render parity**: title screen and one gameplay scene pass golden image comparison.
- **Audio parity**: music starts and at least 3 critical SFX play via abstract `IAudio` route.
- **Load behavior**: startup + first-level load completes with no missing-resource errors.
- **Performance guardrails**: capture frame-time and memory snapshots for desktop baseline before web optimization.

## Next Phase 0 step (remaining)

- Capture runtime baseline notes (startup/title/one-level flow) once a reproducible test asset/runtime setup is documented under `docs/`.
