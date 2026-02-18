#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

GLOB='*.{h,hpp,c,cpp}'

count() {
  local pattern="$1"
  rg -n "$pattern" -S --glob "$GLOB" | wc -l | tr -d ' '
}

echo "WinAPI/DirectX dependency inventory"
echo "root: $ROOT_DIR"
echo
printf "%-28s %s\n" "windows.h includes:" "$(count '#include <windows\.h>')"
printf "%-28s %s\n" "ddraw.h includes:" "$(count '#include <ddraw\.h>')"
printf "%-28s %s\n" "d3d.h includes:" "$(count '#include <d3d\.h>')"
printf "%-28s %s\n" "HWND usages:" "$(count '\bHWND\b')"
printf "%-28s %s\n" "HINSTANCE usages:" "$(count '\bHINSTANCE\b')"
printf "%-28s %s\n" "WinMain usages:" "$(count '\bWinMain\b')"
echo

echo "Top HWND hotspots"
rg -n "\bHWND\b" -S --glob "$GLOB" \
  | cut -d: -f1 \
  | sort \
  | uniq -c \
  | sort -nr \
  | head -n 10
