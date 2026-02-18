#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[2]
runner_cpp = (root / 'app' / 'LawnAppRunner.cpp').read_text(encoding='utf-8')

errors = []
if 'input.IsMouseButtonDown(platform::MouseButton::Left)' not in runner_cpp:
    errors.append('RunLawnApp must probe startup primary mouse state via input.IsMouseButtonDown(platform::MouseButton::Left)')
if 'input.GetMouseX()' not in runner_cpp or 'input.GetMouseY()' not in runner_cpp:
    errors.append('RunLawnApp must read startup mouse position via input.GetMouseX()/input.GetMouseY()')
if not re.search(r'TodTraceAndLog\("Startup input marker: left=%d x=%d y=%d",\s*startupLeftDown\s*\?\s*1\s*:\s*0,\s*startupMouseX,\s*startupMouseY\s*\)', runner_cpp):
    errors.append('RunLawnApp must emit startup input marker log using captured IInput values')

if errors:
    print('input seam guard: FAIL')
    for e in errors:
        print('-', e)
    sys.exit(1)

print('input seam guard: OK')
print('- startup input marker reads button + mouse coordinates through IInput')
