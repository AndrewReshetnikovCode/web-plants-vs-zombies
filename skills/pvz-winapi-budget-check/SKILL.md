---
name: pvz-winapi-budget-check
description: Use this skill when validating migration PRs for WinAPI regression budgets and hotspot drift. It runs budget checks against windows.h/HWND/HINSTANCE/WinMain counts and updates baseline snapshots when intentionally approved.
---

# pvz-winapi-budget-check

## When to use

- Any migration slice that touches platform seams or WinAPI-related files.
- Before opening a PR to ensure no accidental WinAPI dependency regressions.

## Workflow

1. Run `python3 tools/validation/winapi_budget_guard.py`.
2. If counts regress intentionally, refresh baseline with: `python3 tools/validation/winapi_budget_guard.py --update`.
3. Include guard output in PR validation notes.
