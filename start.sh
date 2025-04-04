#!/bin/bash

set -e

# Set environment variables for production
export DEBUG=False
export SECRET_KEY="your-production-secret-key-here"

# Make sure static files directory exists
mkdir -p staticfiles

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
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