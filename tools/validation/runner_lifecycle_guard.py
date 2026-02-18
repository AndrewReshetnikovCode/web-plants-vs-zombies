#!/usr/bin/env python3
"""Validate stable startup runner lifecycle structure.

This guard protects against accidental reordering of key calls while migration is
in progress and code churn is high.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
RUNNER_CPP = ROOT / 'app' / 'LawnAppRunner.cpp'


def find_index(text: str, needle: str) -> int:
    return text.find(needle)


def main() -> int:
    text = RUNNER_CPP.read_text(encoding='utf-8')
    errors: list[str] = []

    ordered_markers = [
        ('window title', 'window.SetTitle("Plants vs. Zombies")'),
        ('startup input marker log', 'TodTraceAndLog("Startup input marker: left=%d x=%d y=%d"'),
        ('window size probe', 'const auto startupWindowSize = window.GetSize();'),
        ('LawnApp allocation', 'gLawnApp = new LawnApp();'),
        ('LawnApp init', 'gLawnApp->Init();'),
        ('fullscreen handoff', 'window.SetFullscreen(!gLawnApp->mIsWindowed);'),
        ('startup ready marker log', 'TodTraceAndLog("Startup ready marker: %llu ms", startupReadyMs);'),
        ('game start', 'gLawnApp->Start();'),
        ('game shutdown', 'gLawnApp->Shutdown();'),
        ('shutdown marker log', 'TodTraceAndLog("Shutdown marker: %llu ms", shutdownDoneMs);'),
        ('app delete', 'delete gLawnApp;'),
        ('app null reset', 'gLawnApp = nullptr;'),
    ]

    last_idx = -1
    for label, needle in ordered_markers:
        idx = find_index(text, needle)
        if idx == -1:
            errors.append(f'missing lifecycle step: {label}')
            continue
        if idx < last_idx:
            errors.append(f'lifecycle order regression around: {label}')
        last_idx = max(last_idx, idx)

    if 'if (gLawnApp)' not in text:
        errors.append('RunLawnApp must guard delete with if (gLawnApp)')

    if errors:
        print('runner lifecycle guard: FAILED')
        for item in errors:
            print(f'- {item}')
        return 1

    print('runner lifecycle guard: OK')
    print('- startup runner lifecycle call order and cleanup markers are intact')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
