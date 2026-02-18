#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$ROOT_DIR"

echo "[core-cycle] validate_slice"
./tools/validation/validate_slice.sh

echo "[core-cycle] winapi budget guard"
python3 tools/validation/winapi_budget_guard.py

echo "[core-cycle] runtime baseline check"
python3 tools/validation/runtime_baseline_check.py

echo "[core-cycle] phase tracker guard"
python3 tools/validation/phase_tracker_guard.py

echo "[core-cycle] build lanes"
./tools/validation/build_lanes.sh
