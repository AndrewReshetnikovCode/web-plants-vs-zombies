#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASELINE_PATH = ROOT / 'tools/validation/budgets/winapi_budget.json'

METRICS = {
    'windows_h_includes': r'#include <windows\.h>',
    'ddraw_h_includes': r'#include <ddraw\.h>',
    'd3d_h_includes': r'#include <d3d\.h>',
    'hwnd_usages': r'\bHWND\b',
    'hinstance_usages': r'\bHINSTANCE\b',
    'winmain_usages': r'\bWinMain\b',
}


def rg_count(pattern: str) -> int:
    cmd = [
        'rg', '-n', pattern, '-S', '--glob', '*.{h,hpp,c,cpp}', str(ROOT),
    ]
    p = subprocess.run(cmd, text=True, capture_output=True)
    if p.returncode not in (0, 1):
        raise RuntimeError(p.stderr.strip() or p.stdout.strip())
    if p.returncode == 1:
        return 0
    return len(p.stdout.splitlines())


def collect() -> dict[str, int]:
    return {k: rg_count(v) for k, v in METRICS.items()}


def main() -> int:
    update = '--update' in sys.argv
    current = collect()

    if update:
        BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
        BASELINE_PATH.write_text(json.dumps(current, indent=2, sort_keys=True) + '\n')
        print(f'winapi budget guard: baseline updated at {BASELINE_PATH.relative_to(ROOT)}')
        return 0

    if not BASELINE_PATH.exists():
        print('winapi budget guard: baseline missing, creating from current counts')
        BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
        BASELINE_PATH.write_text(json.dumps(current, indent=2, sort_keys=True) + '\n')
        print(f'- wrote {BASELINE_PATH.relative_to(ROOT)}')
        return 0

    baseline = json.loads(BASELINE_PATH.read_text())
    regressions: list[str] = []

    print('winapi budget guard: snapshot')
    for key in METRICS:
        b = int(baseline.get(key, 0))
        c = int(current.get(key, 0))
        delta = c - b
        sign = '+' if delta > 0 else ''
        print(f'- {key}: baseline={b}, current={c}, delta={sign}{delta}')
        if c > b:
            regressions.append(f'{key} regressed: {b} -> {c}')

    if regressions:
        print('winapi budget guard: FAILED')
        for e in regressions:
            print(f'  - {e}')
        print('If regression is intentional, run with --update and document rationale.')
        return 1

    print('winapi budget guard: OK')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
