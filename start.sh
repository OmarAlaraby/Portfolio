set -e

# Set environment variables for production
export DEBUG=False

# Make sure directories exist with proper permissions
mkdir -p staticfiles
mkdir -p media
chmod -R 755 staticfiles
chmod -R 755 media

# Install dependencies (replace poetry with pip if needed)
if [ -f "pyproject.toml" ]; then
    pip install poetry
    poetry install --no-interaction --no-ansi
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start Gunicorn
echo "Starting Gunicorn server..."
gunicorn --workers=3 portfolio.wsgi:application --bind 0.0.0.0:$PORT
