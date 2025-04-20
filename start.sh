#!/bin/bash
set -e

# Production environment settings
export DEBUG=False
export PYTHONUNBUFFERED=1

# Start Gunicorn
echo "Starting Gunicorn server..."
exec poetry run gunicorn \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --forwarded-allow-ips="*" \
    --error-logfile - \
    portfolio.wsgi:application
