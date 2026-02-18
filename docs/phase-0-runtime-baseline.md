# Phase 0 Runtime Baseline Notes

## Goal

Capture repeatable baseline observations for:

- startup behavior,
- title-screen state,
- one playable level flow.

This complements `docs/phase-0-baseline.md` (static dependency inventory).

## Current status

- **Status:** Partial / blocked
- **Reason:** Runtime baseline requires a local build plus original game assets available in expected paths.

## Capture protocol (to run on maintainer workstation)

1. Build desktop target.
2. Provide required original assets in configured runtime location.
3. Launch app and record:
   - startup duration,
   - title-screen render + responsiveness,
   - one-level flow checkpoints:
     - level start,
     - first zombie spawn,
     - first projectile hit,
     - win/lose transition.
4. Save screenshots/log snippets and append to this document.

## Baseline template

- Build command:
- Runtime command:
- Asset source location:
- Startup duration:
- Title-screen notes:
- Level-flow notes:
- Known anomalies:

## Follow-up

After this document is filled with actual runtime measurements, mark Phase 0 runtime baseline item complete in `README.md`.
