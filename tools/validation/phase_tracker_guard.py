#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / 'README.md'


def main() -> int:
    text = README.read_text().splitlines()
    phase_headers = [line for line in text if line.startswith('### Phase ')]
    if len(phase_headers) < 6:
        print('phase tracker guard: FAILED')
        print(f'- expected at least 6 phase headers, found {len(phase_headers)}')
        return 1

    checklist_lines = [line for line in text if re.match(r'- \[[ x]\] ', line)]
    if not checklist_lines:
        print('phase tracker guard: FAILED')
        print('- no checklist lines found')
        return 1

    cmd = ['python3', 'skills/pvz-migration-slice/scripts/phase_progress.py']
    run = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if run.returncode != 0:
        print('phase tracker guard: FAILED')
        print('- phase_progress.py failed to execute')
        print(run.stderr.strip() or run.stdout.strip())
        return run.returncode

    print('phase tracker guard: OK')
    print(f'- phase headers: {len(phase_headers)}')
    print(f'- checklist lines: {len(checklist_lines)}')
    print('- phase_progress.py execution: OK')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
