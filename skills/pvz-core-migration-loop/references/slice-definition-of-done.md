# Slice Definition of Done (PvZ migration)

A slice is acceptable when all items below are true.

## 1) Scope

- The PR has one primary seam focus.
- Any secondary edits directly support that seam.
- The change can be described in one sentence.

## 2) Code

- The seam change is visible in production code (not docs-only).
- No unrelated refactors are mixed in.
- If a seam call is added, it is observable (state change, log marker, or behavior change).

## 3) Docs

- Update one phase-specific doc in `docs/`.
- Update the relevant status/checklist line in `README.md`.
- Keep statements factual and tied to what code now does.

## 4) Validation

Run these commands in order:

```bash
./tools/validation/validate_slice.sh
python3 tools/validation/winapi_budget_guard.py
python3 tools/validation/runtime_baseline_check.py
python3 tools/validation/phase_tracker_guard.py
./tools/validation/build_lanes.sh
```

Interpretation:

- `runtime_baseline_check.py` may emit WARN while baseline doc is intentionally partial.
- `build_lanes.sh` full-build lane may be skipped unless `RUN_FULL_BUILD=1`.

## 5) Commit/PR message contract

- Include seam focus.
- Include files changed.
- Include exact validation commands.
- Include known blocker/warn context.

## 6) Anti-patterns

Avoid these:

- Placeholder PR text.
- Docs claiming progress that code does not implement.
- Adding scripts/checks without wiring them into wrapper commands.
- Multiple unrelated seam migrations in one slice.
