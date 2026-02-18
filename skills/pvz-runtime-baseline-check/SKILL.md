---
name: pvz-runtime-baseline-check
description: Use this skill to enforce Phase 0 runtime-baseline capture discipline by checking whether runtime baseline notes are still template-only or contain real measurements.
---

# pvz-runtime-baseline-check

## When to use

- Any PR that claims runtime baseline progress.
- Regularly during migration to keep baseline capture visible.

## Workflow

1. Run `python3 tools/validation/runtime_baseline_check.py`.
2. If maintainers have workstation assets/builds available, complete fields in `docs/phase-0-runtime-baseline.md`.
3. Re-run check and include result in PR notes.
