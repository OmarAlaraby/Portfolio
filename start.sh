set -e

# Set environment variables
export DEBUG=False

# Directory setup
mkdir -p staticfiles media
chmod -R 755 staticfiles media

# Poetry installation
if [ -f "pyproject.toml" ]; then
    pip install poetry
    poetry lock --no-update  # Add this line
    poetry install --no-interaction --no-ansi --no-root
fi

# Django commands
python manage.py collectstatic --noinput --clear
python manage.py migrate

# Start Gunicorn
gunicorn --workers=3 portfolio.wsgi:application 
