# Portfolio

A personal portfolio website built with Django to showcase projects, skills, and resume.

View the live portfolio: [omar-alaraby-portfolio.onrender.com](https://omar-alaraby-portfolio.onrender.com)

## Development Setup with Poetry

1. Clone the repository:
   ```
   git clone https://github.com/OmarAlaraby/Portfolio.git
   cd Portfolio
   ```

2. Install Poetry (if not already installed):
   ```
   # On Linux/macOS
   curl -sSL https://install.python-poetry.org | python3 -

   # On Windows (PowerShell)
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

3. Set up the Poetry environment and install dependencies:
   ```
   # Install dependencies from pyproject.toml
   poetry install

   # Activate the Poetry virtual environment
   poetry shell
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the site at http://127.0.0.1:8000/

## Production Deployment

### Server Requirements

- Python 3.8+
- Poetry
- Gunicorn
- Whitenoise (for static files serving)
- PostgreSQL (recommended for production)

### Deployment Steps

1. Clone the repository on your server:
   ```
   git clone https://github.com/OmarAlaraby/Portfolio.git
   cd Portfolio
   ```

2. Install Poetry and set up the environment:
   ```
   # Install Poetry
   curl -sSL https://install.python-poetry.org | python3 -

   # Install dependencies
   poetry install --no-dev

   # Activate the Poetry environment
   poetry shell
   ```

3. Configure environment variables:
   - Add the following to your server environment or to a `.env` file:
     ```
     DEBUG=False
     SECRET_KEY=your-secure-secret-key-here
     ```

4. Set up SSL (if needed):
   - You can use a reverse proxy or configure Gunicorn directly with SSL
   - For development testing with HTTPS, install django-sslserver:
     ```
     poetry add django-sslserver
     ```
     Then run: `python manage.py runsslserver`

5. Set up the systemd service:
   - Copy `portfolio.service` to `/etc/systemd/system/`
   - Update paths to match your server and Poetry environment
   - Enable and start the service:
     ```
     sudo systemctl daemon-reload
     sudo systemctl enable portfolio
     sudo systemctl start portfolio
     ```

6. Monitor the application logs:
   ```
   sudo journalctl -u portfolio.service
   ```

## Quick Start with the Production Script

To start the application in production mode using Gunicorn:

1. Make the script executable:
   ```
   chmod +x start.sh
   ```

2. Update the SECRET_KEY in the script:
   ```
   # Edit start.sh and update this line:
   export SECRET_KEY="your-production-secret-key-here"
   ```

3. Run the script through Poetry:
   ```
   poetry run ./start.sh
   ```

This will collect static files, apply migrations, and start Gunicorn with production settings.

## Maintenance

- Updating the application:
  ```
  git pull
  poetry install
  poetry run python manage.py migrate
  sudo systemctl restart portfolio
  ```

- Adding new dependencies:
  ```
  poetry add package-name
  ```

- Backing up the database:
  ```
  poetry run python manage.py dumpdata > backup.json
  ```

## Understanding the Poetry Setup

This project uses Poetry for dependency management. Key files:

- `pyproject.toml`: Defines project metadata and dependencies
- `poetry.lock`: Ensures reproducible installations with exact package versions

Common Poetry commands:
```
poetry add package-name        # Add a new dependency
poetry remove package-name     # Remove a dependency
poetry update                  # Update all dependencies
poetry show                    # List all packages
poetry export -f requirements.txt > requirements.txt  # Export to requirements.txt
```

## Handling Static Files in Production

This project uses Whitenoise to serve static files efficiently in production:

1. Static files configuration (already set in `portfolio/settings.py`):
   ```python
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static'),
   ]
   
   # In production (DEBUG=False), Whitenoise is used:
   if not DEBUG:
       STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

2. Collect static files before starting the server:
   ```
   # Set environment variable for production
   export DEBUG=False
   
   # Collect static files with Poetry
   poetry run python manage.py collectstatic --noinput --clear
   ```
   
   Or use the provided script:
   ```
   poetry run ./start.sh
   ```

3. Whitenoise will automatically serve static files via Django's middleware.

If you're having issues with static files, check the application logs for specific errors.