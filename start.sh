#!/bin/bash
set -e

# Production environment settings
export DEBUG=False
export PYTHONUNBUFFERED=1

# Start Gunicorn
echo "Starting Gunicorn server..."
exec poetry run gunicorn \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    portfolio.wsgi:application