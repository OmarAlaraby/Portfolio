#!/bin/bash
set -e

# Verify Python version
python_version=$(python --version 2>&1)
required_version="Python 3.12"

if [[ $python_version != *"$required_version"* ]]; then
    echo "Error: Python 3.12 is required (current version: $python_version)"
    echo "Please use Python 3.12 or modify the Python requirement in pyproject.toml"
    exit 1
fi

echo "Using $python_version"

# Ensure pip is updated
python -m pip install --upgrade pip

# Install Poetry (pinned version for stability)
pip install poetry==1.8.2

# Set Poetry to use the system Python 3.12
poetry env use $(which python)

# Install project dependencies
poetry install --only main --no-interaction --no-ansi

echo "Build completed successfully with Python 3.12"