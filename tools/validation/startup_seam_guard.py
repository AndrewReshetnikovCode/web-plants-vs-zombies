#!/usr/bin/env python3
from pathlib import Path
import re
import sys

errors = []

runner_h = Path('app/LawnAppRunner.h').read_text()
main_cpp = Path('main.cpp').read_text()

sig_pattern = re.compile(
    r"RunLawnApp\(\s*platform::IFileSystem&\s+\w+,\s*platform::IClock&\s+\w+,\s*platform::IWindow&\s+\w+,\s*platform::IInput&\s+\w+\s*\)"
)

if not sig_pattern.search(runner_h):
    errors.append('RunLawnApp signature must include IFileSystem, IClock, IWindow, IInput in app/LawnAppRunner.h')

required_includes = [
    'platform/desktop/DesktopFileSystemAdapter.h',
    'platform/desktop/DesktopClockAdapter.h',
    'platform/desktop/DesktopWindowAdapter.h',
    'platform/desktop/DesktopInputAdapter.h',
]
for inc in required_includes:
    if f'#include "{inc}"' not in main_cpp:
        errors.append(f'main.cpp missing include: {inc}')

call_pattern = re.compile(r'RunLawnApp\(fileSystem,\s*clock,\s*window,\s*input\)')
if not call_pattern.search(main_cpp):
    errors.append('main.cpp must call RunLawnApp(fileSystem, clock, window, input)')

if errors:
    print('startup seam guard: FAILED')
    for e in errors:
        print(f'- {e}')
    sys.exit(1)

print('startup seam guard: OK')
print('- runner signature includes IFileSystem/IClock/IWindow/IInput')
print('- main.cpp injects desktop adapters and delegates full seam call')
