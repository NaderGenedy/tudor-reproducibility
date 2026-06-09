#!/usr/bin/env bash
# TUDOR — one-shot reproducibility wrapper (synthetic / web-safe by default).
# Usage:  bash run_all.sh            # synthetic (works anywhere, incl. Claude web)
#         bash run_all.sh --real     # governed data (local workstation / UKB RAP only)
set -euo pipefail
cd "$(dirname "$0")"

PY="${PYTHON:-python}"
MODE="--synthetic"
[ "${1:-}" = "--real" ] && MODE="--real"

echo "==> Python: $($PY --version)"
echo "==> Installing pinned dependencies"
$PY -m pip install -q -r requirements.txt

if [ "$MODE" = "--synthetic" ]; then
  echo "==> Generating synthetic data (no real patients)"
  $PY make_synthetic_tudor_data.py
fi

echo "==> Inventory"
$PY TUDOR_MASTER.py --check || true

echo "==> Running full pipeline ($MODE)"
$PY TUDOR_MASTER.py $MODE --all

echo "==> Locked clinical targets (reference)"
$PY TUDOR_MASTER.py --reproduce

echo "==> Done. Outputs in ./output/"
