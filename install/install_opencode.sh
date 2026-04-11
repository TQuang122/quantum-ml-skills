#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_INSTALLER="${SCRIPT_DIR}/install_opencode.py"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  printf 'Error: Python is required to run install/install_opencode.py.\n' >&2
  printf 'Install Python 3, or use the manual copy flow documented in README.md and examples/use-with-opencode.md.\n' >&2
  exit 1
fi

exec "${PYTHON_BIN}" "${PY_INSTALLER}" "$@"
