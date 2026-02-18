#!/usr/bin/env python3
"""Guardrails for startup/shutdown timing seam usage in RunLawnApp.

This check ensures that timing markers continue to flow through IClock and that
startup duration stays derivable from logged timestamps.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
RUNNER_CPP = ROOT / 'app' / 'LawnAppRunner.cpp'


def main() -> int:
    text = RUNNER_CPP.read_text(encoding='utf-8')
    errors: list[str] = []

    if text.count('clock.NowMilliseconds()') < 3:
        errors.append('RunLawnApp must sample clock.NowMilliseconds() at startup-begin/startup-ready/shutdown markers')

    if 'startupBeginMs' not in text:
        errors.append('RunLawnApp must keep a startupBeginMs marker for startup duration derivation')

    if 'startupReadyMs' not in text:
        errors.append('RunLawnApp must keep a startupReadyMs marker after Init()')

    if 'startupDeltaMs' not in text:
        errors.append('RunLawnApp must compute startupDeltaMs using startupReadyMs - startupBeginMs')

    duration_pattern = re.compile(
        r'startupReadyMs\s*>=\s*startupBeginMs\s*\?\s*\(startupReadyMs\s*-\s*startupBeginMs\)\s*:\s*0'
    )
    if not duration_pattern.search(text):
        errors.append('RunLawnApp must guard startupDeltaMs against timestamp underflow')

    required_logs = [
        'TodTraceAndLog("Startup ready marker: %llu ms", startupReadyMs);',
        'TodTraceAndLog("Startup duration marker: %llu ms", startupDeltaMs);',
        'TodTraceAndLog("Shutdown marker: %llu ms", shutdownDoneMs);',
    ]
    for log_line in required_logs:
        if log_line not in text:
            errors.append(f'missing timing marker log: {log_line}')

    if errors:
        print('clock seam guard: FAILED')
        for item in errors:
            print(f'- {item}')
        return 1

    print('clock seam guard: OK')
    print('- startup begin/ready/duration/shutdown timing markers remain routed through IClock')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
