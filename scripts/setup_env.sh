#!/usr/bin/env bash
set -e
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
echo "Environment ready. Activate with: source .venv/bin/activate"
