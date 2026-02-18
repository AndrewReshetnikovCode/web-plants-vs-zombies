#!/usr/bin/env python3
from pathlib import Path
import re

readme = Path('README.md').read_text().splitlines()

phase_rows = []
current = None
for line in readme:
    if line.startswith('### Phase '):
        current = {'phase': line.strip(), 'done': 0, 'todo': 0}
        phase_rows.append(current)
        continue
    if current and re.match(r'- \[[ x]\] ', line):
        if line.startswith('- [x]'):
            current['done'] += 1
        else:
            current['todo'] += 1

print('Migration phase completion snapshot')
for row in phase_rows:
    total = row['done'] + row['todo']
    pct = (row['done'] / total * 100.0) if total else 0.0
    print(f"- {row['phase']}: {row['done']}/{total} ({pct:.0f}%)")

try:
    start = readme.index('## WinAPI migration checklist (operational)')
except ValueError:
    raise SystemExit(0)

w_done = w_todo = 0
for line in readme[start + 1:]:
    if line.startswith('## '):
        break
    if re.match(r'- \[[ x]\] ', line):
        if line.startswith('- [x]'):
            w_done += 1
        else:
            w_todo += 1

total = w_done + w_todo
pct = (w_done / total * 100.0) if total else 0.0
print(f"- WinAPI checklist: {w_done}/{total} ({pct:.0f}%)")
