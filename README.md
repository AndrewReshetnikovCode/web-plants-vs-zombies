# web-plants-vs-zombies

This repository starts from the existing PvZ decompilation/modernization codebase and tracks the migration path toward a browser-playable web version.

## Mission

Build a browser-playable PvZ runtime by introducing platform abstractions, reducing WinAPI coupling, and adding a dedicated web build pipeline while preserving gameplay parity.

## Repository scaffold (web migration)

```text
web-plants-vs-zombies/
├─ app/                         # app entrypoints and bootstrap glue
├─ assets/
│  ├─ manifests/                # generated resource manifests
│  ├─ processed/                # converted/packed assets for runtime
│  └─ raw/                      # source assets (policy-dependent)
├─ audio/
│  ├─ common/                   # backend-agnostic audio layer
│  ├─ desktop/                  # native desktop audio backend
│  └─ webaudio/                 # browser audio backend
├─ cmake/                       # target/toolchain split (desktop/web)
├─ docs/                        # migration notes, reports, decisions
├─ engine/
│  ├─ core/                     # loop/timing/application services
│  ├─ gameplay/                 # extracted game rules and systems
│  ├─ math/                     # shared math helpers
│  ├─ resources/                # resource loading/group orchestration
│  └─ serialization/            # save/load and data formats
├─ platform/
│  ├─ desktop/                  # desktop platform adapters
│  ├─ interfaces/               # IWindow, IInput, IAudio, etc.
│  └─ web/                      # web/emscripten adapters
├─ render/
│  ├─ common/                   # renderer-agnostic draw command API
│  ├─ desktop_gl/               # desktop OpenGL compatibility backend
│  └─ webgl/                    # browser rendering backend
├─ tests/
│  ├─ gameplay/                 # deterministic simulation checks
│  ├─ golden/                   # visual parity snapshots
│  └─ unit/                     # isolated module tests
├─ third_party/                 # external deps/vendor sources
├─ tools/
│  ├─ asset_packer/             # packaging/compression scripts
│  ├─ resource_manifest_gen/    # resource manifest generation
│  └─ validation/               # build/runtime validation scripts
└─ web/
   ├─ public/                   # static files served with web build
   ├─ scripts/                  # web build/start scripts
   └─ shell/                    # index.html/bootstrap shell
```

## Current status

- ✅ Initial migration tree folders are present.
- ✅ First platform interface headers are added in `platform/interfaces`.
- ✅ Desktop no-op adapters are added to unblock wiring in Phase 1.
- ✅ Web shell and web CMake placeholders are added.
- ✅ Phase 0 dependency inventory and baseline metric definitions are documented in `docs/phase-0-baseline.md`.
- ✅ Added repeatable inventory script: `tools/validation/winapi_inventory.sh`.
- ✅ Added migration progress summary script: `tools/validation/phase_progress.sh`.
- ✅ Added runtime baseline capture template: `docs/phase-0-runtime-baseline.md`.
- ✅ Extracted startup sequence into `app/LawnAppRunner.cpp` and injected `IFileSystem` into startup path.
- ✅ Added entrypoint bridge in `main.cpp` (WinMain + fallback `main`) that reuses one startup dispatcher.
- ✅ Wired startup timing through `IClock` in `RunLawnApp(...)` with desktop clock adapter injection.
- ✅ Wired startup window/input seams through `IWindow` + `IInput` in the shared runner path (title/cursor/fullscreen/size + input marker).
- ✅ Added process-optimization skill/workflow and progress validator for vertical-slice PR execution.
- ✅ Added startup seam guard validation script to prevent signature/injection regressions.

## Migration tracker (phases + milestones)

Use these checklists as the source of truth and keep them updated in PRs.

### Phase 0 — Baseline and inventory

- [x] Enumerate all WinAPI/DirectX usages (`windows.h`, `HWND`, `HINSTANCE`, `ddraw.h`, `d3d.h`).
- [ ] Capture baseline run profile (startup, title screen, one level flow). Track in `docs/phase-0-runtime-baseline.md`.
- [x] Define acceptance metrics for parity (logic, rendering, audio, load times).

**Milestone M0 (Done when):** audited dependency report + baseline behavior notes are committed under `docs/`.

### Phase 1 — Platform abstraction (WinAPI migration start)

- [x] Create interface contracts in `platform/interfaces` (`IWindow`, `IInput`, `IClock`, `IFileSystem`, `IAudio`).
- [x] Add initial desktop implementations in `platform/desktop` for incremental integration.
- [ ] Replace direct WinAPI calls in migrated pathways with interface calls. (Partial: startup path routes resource probe via `IFileSystem`, timing via `IClock`, and window title/cursor/fullscreen/size via `IWindow`; entry wiring is no longer `WinMain`-only.)
- [ ] Keep desktop behavior functional through the new adapters.

**Milestone M1 (Done when):** startup + selected gameplay paths compile and run without direct WinAPI usage in migrated modules.

### Phase 2 — Rendering migration

- [ ] Define render command surface in `render/common`.
- [ ] Add desktop parity backend in `render/desktop_gl`.
- [ ] Add browser backend in `render/webgl`.
- [ ] Validate visual output for title + one gameplay scene.

**Milestone M2 (Done when):** same scene renders in desktop/web pipelines with acceptable parity.

### Phase 3 — Audio migration

- [ ] Route sound/music requests through `IAudio`.
- [ ] Preserve desktop backend behavior.
- [ ] Implement `audio/webaudio` backend.
- [ ] Add browser autoplay-unlock flow after user interaction.

**Milestone M3 (Done when):** browser build plays core music + SFX reliably.

### Phase 4 — Resource pipeline and loading groups

- [ ] Implement manifest generator in `tools/resource_manifest_gen`.
- [ ] Preserve grouped loading semantics (`Init`, `DelayLoad_*`, etc.).
- [ ] Introduce web preload/lazy-load strategy for memory control.

**Milestone M4 (Done when):** resource groups load deterministically in browser build.

### Phase 5 — Build targets and CI

- [ ] Split desktop/web CMake target configuration under `cmake/`.
- [ ] Add local web run command/script in `web/scripts`.
- [ ] Add CI job that builds publishable web artifacts.

**Milestone M5 (Done when):** CI outputs runnable `index.html + .js + .wasm` artifact set.

### Phase 6 — Gameplay parity and optimization

- [ ] Add deterministic gameplay checks in `tests/gameplay`.
- [ ] Add golden visual comparisons in `tests/golden`.
- [ ] Track performance budgets (frame time, memory, load time).

**Milestone M6 (Done when):** at least one full level is browser-playable with acceptable parity/performance.

## WinAPI migration checklist (operational)

Track this list while working through Phases 1–3:

- [ ] Entry point: replace Win32-only `WinMain` assumptions with portable runner contract. (Partial: shared dispatcher + fallback `main` added.)
- [ ] Windowing: move window creation/mode/cursor handling behind `IWindow`. (Partial: startup path now injects `IWindow` and routes title/cursor/fullscreen/size through adapter.)
- [ ] Input: move keyboard/mouse routing behind `IInput`. (Partial: startup path now injects `IInput` marker call.)
- [ ] Timing: replace platform timing calls with `IClock`. (Partial: startup path now receives `IClock`.)
- [ ] Filesystem: standardize reads via `IFileSystem` for desktop + browser packaged assets.
- [ ] Audio: remove `HWND`/Win-specific coupling from gameplay-facing audio API.
- [ ] Render: eliminate direct DDraw/D3D dependencies from gameplay-side codepaths.
- [ ] Build: isolate Windows-only links/defines to desktop target only.

## Legal / asset note

This project does not include proprietary PopCap game assets. You must own the original game files and provide assets locally for runtime/testing.

## Prioritized suggestions (current relevance)

Decision: execute **all** of the following, in this order.

1. **Complete remaining Phase 0 runtime baseline capture**
   Record startup/title/one-level baseline notes so migration regressions can be measured objectively.
2. **Migrate a narrow startup slice first (entrypoint + clock + window shell)**
   Keep gameplay untouched while proving interface wiring in one safe path.
3. **Target highest WinAPI hotspot early (`SexyAppFramework/SexyAppBase.cpp`)**
   Reduce `HWND` coupling where it is currently most concentrated.
4. **Add lightweight adapter validation as wiring proceeds**
   Add small compile/runtime checks per adapter to avoid dead abstractions.

