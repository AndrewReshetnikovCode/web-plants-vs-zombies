---
name: pvz-core-migration-loop
description: Run one repeatable PvZ migration slice with a fixed order: implement one seam-focused change, update docs/checklists, run validation wrappers, and record outcomes for commit/PR notes.
---

# pvz-core-migration-loop

## When to use

Use this skill when the user asks to continue the migration loop, do "next tasks", or ship a batched slice that must include code + docs + validation.

## Core workflow

1. **Pick exactly one seam focus** for the slice (`startup`, `window`, `input`, `clock`, or `filesystem`).
2. **Implement the code change** in that seam with minimal blast radius.
3. **Update docs/checklists** in:
   - `docs/phase-1-*.md` for slice notes,
   - `README.md` migration status/checklist lines.
4. **Run validation wrappers** with `scripts/run_core_cycle.sh`.
5. **Record outputs** (pass/warn/fail, blockers) for commit and PR messaging.

## Validation order

Run the script:

```bash
skills/pvz-core-migration-loop/scripts/run_core_cycle.sh
```

It runs, in order:

1. `tools/validation/validate_slice.sh`
2. `python3 tools/validation/winapi_budget_guard.py`
3. `python3 tools/validation/runtime_baseline_check.py`
4. `python3 tools/validation/phase_tracker_guard.py`
5. `tools/validation/build_lanes.sh`

## Output expectations

- Treat runtime baseline as warning-only unless explicitly asked to require complete baseline.
- Keep `build_lanes.sh` full-build lane optional unless `RUN_FULL_BUILD=1` is set.
- Include seam focus, files touched, and exact commands in PR notes.

## References

- `references/slice-definition-of-done.md` defines the minimum slice contract.

