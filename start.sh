#!/bin/bash

set -e

# Set environment variables for production
export DEBUG=False

# Make sure directories exist with proper permissions
mkdir -p staticfiles
mkdir -p media
chmod -R 755 staticfiles
chmod -R 755 media

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    poetry shell
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start Gunicorn
echo "Starting Gunicorn server..."
gunicorn --workers=3 portfolio.wsgi:application 