#!/bin/bash
set -e

# Get Python version and parse it
python_version=$(python --version 2>&1 | cut -d ' ' -f 2)
python_major=$(echo $python_version | cut -d. -f1)
python_minor=$(echo $python_version | cut -d. -f2)

# Check if Python version is at least 3.11
if [[ "$python_major" -lt 3 || ("$python_major" -eq 3 && "$python_minor" -lt 11) ]]; then
    echo "Error: Python 3.11 or higher is required (current version: $python_version)"
    echo "Please install Python 3.11+ or check your environment configuration"
    exit 1
fi

echo "Using Python $python_version (3.11+ required)"

# Ensure pip is updated
python -m pip install --upgrade pip

# Install Poetry (pinned version for stability)
pip install poetry==1.8.2

# Set Poetry to use the system Python
poetry env use $(which python)

# Install project dependencies
poetry install --only main --no-interaction --no-ansi

# Ensure Gunicorn is installed
poetry add gunicorn

# Create required directories
mkdir -p staticfiles media
chmod -R 755 staticfiles media

# Collect static files
echo "Collecting static files..."
poetry run python manage.py collectstatic --noinput --clear

echo "Build completed successfully"