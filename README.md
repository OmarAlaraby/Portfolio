# Portfolio

A personal portfolio website built with Django to showcase projects, skills, and resume.

## Development Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Portfolio
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
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
- Gunicorn
- PostgreSQL (recommended for production)

### Deployment Steps

1. Clone the repository on your server:
   ```
   git clone <repository-url>
   cd Portfolio
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure production settings:
   - Update `portfolio/settings_prod.py` with your domain and email settings
   - Set `SECRET_KEY` in an environment variable
   - Configure database settings if using PostgreSQL

5. Set up SSL (if needed):
   - You can use a reverse proxy or configure Gunicorn directly with SSL
   - For development testing with HTTPS, install django-sslserver:
     ```
     pip install django-sslserver
     ```
     Then run: `python manage.py runsslserver`

6. Set up the systemd service:
   - Copy `portfolio.service` to `/etc/systemd/system/`
   - Update paths to match your server
   - Enable and start the service:
     ```
     sudo systemctl daemon-reload
     sudo systemctl enable portfolio
     sudo systemctl start portfolio
     ```

7. Monitor the application logs:
   ```
   sudo journalctl -u portfolio.service
   ```

## Quick Start with the Production Script

To start the application in production mode using Gunicorn:

1. Make the script executable:
   ```
   chmod +x start_production.sh
   ```

2. Run the script:
   ```
   ./start_production.sh
   ```

This will collect static files, apply migrations, and start Gunicorn with the production settings.

## Maintenance

- Updating the application:
  ```
  git pull
  source .venv/bin/activate
  pip install -r requirements.txt
  python manage.py migrate
  sudo systemctl restart portfolio
  ```

- Backing up the database:
  ```
  python manage.py dumpdata > backup.json
  ```

## Handling Static Files in Production

For proper static file handling in production (including admin static files):

1. Make sure your `portfolio/settings_prod.py` has the correct static file settings:
   ```python
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   STATIC_URL = '/static/'
   STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static'),
   ]
   ```

2. Collect static files before starting the server:
   ```
   # Run with production settings
   export DJANGO_SETTINGS_MODULE=portfolio.settings_prod
   python manage.py collectstatic --noinput --clear
   ```
   
   Or use the provided script:
   ```
   ./collect_static.sh
   ```

3. For static file serving in production, you have several options:
   - Configure Gunicorn to serve static files directly
   - Use a CDN service
   - Use Django's built-in static file serving for small projects (not recommended for high-traffic sites)
   - Use whitenoise package for more efficient static file serving in Django

If you're having issues with static files, check the application logs for specific errors.