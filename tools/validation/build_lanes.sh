#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

echo "build lanes: quick-validation lane"
python3 tools/validation/startup_seam_guard.py
python3 tools/validation/window_seam_guard.py
python3 tools/validation/input_seam_guard.py
./tools/validation/winapi_inventory.sh
./tools/validation/phase_progress.sh
python3 tools/validation/winapi_budget_guard.py
python3 tools/validation/runtime_baseline_check.py
python3 tools/validation/phase_tracker_guard.py

if [[ "${RUN_FULL_BUILD:-0}" != "1" ]]; then
  echo "build lanes: full-build lane skipped (set RUN_FULL_BUILD=1 to enable)"
  exit 0
fi

echo "build lanes: full-build lane"
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j4
