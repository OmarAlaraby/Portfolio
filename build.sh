#!/bin/bash
set -e

# Install dependencies via Poetry
echo "Installing dependencies..."
pip install poetry==1.8.2

# Regenerate the lock file
echo "Updating lock file..."
poetry lock --no-update

# Install dependencies
poetry install --no-interaction --no-ansi

# Ensure Gunicorn and python-dotenv are installed
poetry add gunicorn python-dotenv

echo "Build completed successfully"
