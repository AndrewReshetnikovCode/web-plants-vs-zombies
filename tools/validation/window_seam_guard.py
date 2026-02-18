#!/usr/bin/env python3
from pathlib import Path
import re
import sys

errors = []
runner_cpp = Path('app/LawnAppRunner.cpp').read_text()

if 'window.GetSize()' not in runner_cpp:
    errors.append('RunLawnApp must read startup window size via window.GetSize()')

if not re.search(r'gLawnApp->mWidth\s*=\s*startupWindowSize\.width\s*;', runner_cpp):
    errors.append('RunLawnApp must route startup width from startupWindowSize.width')

if not re.search(r'gLawnApp->mHeight\s*=\s*startupWindowSize\.height\s*;', runner_cpp):
    errors.append('RunLawnApp must route startup height from startupWindowSize.height')

if not re.search(r'window\.SetFullscreen\(\s*!gLawnApp->mIsWindowed\s*\)', runner_cpp):
    errors.append('RunLawnApp must call window.SetFullscreen(!gLawnApp->mIsWindowed) after init')

if errors:
    print('window seam guard: FAILED')
    for e in errors:
        print(f'- {e}')
    sys.exit(1)

print('window seam guard: OK')
print('- startup size is read from IWindow::GetSize() and routed to LawnApp dimensions')
print('- startup fullscreen handoff uses IWindow::SetFullscreen(!mIsWindowed)')
