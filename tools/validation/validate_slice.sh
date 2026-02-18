#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

python3 tools/validation/startup_seam_guard.py
python3 tools/validation/window_seam_guard.py
python3 tools/validation/input_seam_guard.py
python3 tools/validation/clock_seam_guard.py
python3 tools/validation/runner_lifecycle_guard.py
./tools/validation/winapi_inventory.sh
./tools/validation/phase_progress.sh
