#!/bin/bash
set -e

# Production environment settings
export DEBUG=False
export PYTHONUNBUFFERED=1

# Create required directories
mkdir -p staticfiles media
chmod -R 755 staticfiles media

# Apply database migrations
echo "Applying database migrations..."
poetry run python manage.py migrate

# Start Gunicorn
echo "Starting Gunicorn server..."
exec poetry run gunicorn \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    portfolio.wsgi:application