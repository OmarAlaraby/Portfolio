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
- Whitenoise (for static files serving)
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

4. Configure environment variables:
   - Add the following to your server environment or to a `.env` file:
     ```
     DEBUG=False
     SECRET_KEY=your-secure-secret-key-here
     ```

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
   chmod +x start.sh
   ```

2. Update the SECRET_KEY in the script:
   ```
   # Edit start.sh and update this line:
   export SECRET_KEY="your-production-secret-key-here"
   ```

3. Run the script:
   ```
   ./start.sh
   ```

This will collect static files, apply migrations, and start Gunicorn with production settings.

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
   
   # Collect static files
   python manage.py collectstatic --noinput --clear
   ```
   
   Or use the provided script:
   ```
   ./start.sh
   ```

3. Whitenoise will automatically serve static files via Django's middleware.

If you're having issues with static files, check the application logs for specific errors.