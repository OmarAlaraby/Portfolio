set -e

# Production environment settings
export DEBUG=False
export PYTHONUNBUFFERED=1

# Create required directories
mkdir -p staticfiles media
chmod -R 755 staticfiles media

# Verify Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry not found. Please run build.sh first."
    exit 1
fi

# Apply database migrations
echo "Applying database migrations..."
poetry run python manage.py migrate

# Collect static files
echo "Collecting static files..."
poetry run python manage.py collectstatic --noinput --clear

# Install Gunicorn if needed
poetry add gunicorn &> /dev/null || true

# Start Gunicorn
echo "Starting Gunicorn server..."
exec poetry run gunicorn \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    portfolio.wsgi:application

