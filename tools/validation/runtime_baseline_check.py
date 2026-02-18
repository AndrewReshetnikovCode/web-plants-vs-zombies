#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / 'docs/phase-0-runtime-baseline.md'

TEMPLATE_FIELDS = [
    '- Build command:',
    '- Runtime command:',
    '- Asset source location:',
    '- Startup duration:',
    '- Title-screen notes:',
    '- Level-flow notes:',
    '- Known anomalies:',
]


def main() -> int:
    text = DOC.read_text()
    missing_data = []
    for field in TEMPLATE_FIELDS:
        if field not in text:
            missing_data.append(f'missing template line: {field}')
            continue
        for line in text.splitlines():
            if line.startswith(field):
                if line.strip() == field:
                    missing_data.append(f'unfilled: {field}')
                break

    status_blocked = '**Status:** Partial / blocked' in text

    print('runtime baseline check: snapshot')
    print(f'- document: {DOC.relative_to(ROOT)}')
    print(f'- blocked_status_present: {status_blocked}')
    print(f'- unfilled_template_fields: {len(missing_data)}')

    if '--require-complete' in sys.argv:
        if status_blocked or missing_data:
            print('runtime baseline check: FAILED (require-complete mode)')
            for item in missing_data:
                print(f'  - {item}')
            if status_blocked:
                print('  - status still marked as Partial / blocked')
            return 1

    if status_blocked or missing_data:
        print('runtime baseline check: WARN (baseline still partial)')
    else:
        print('runtime baseline check: OK (baseline appears populated)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
