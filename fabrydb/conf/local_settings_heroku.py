import os
# from global_settings import PROJECT_PATH

# Uncomment to put the application in non-debug mode. This is useful
# for testing error handling and messages.
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Override this to match the application endpoint
FORCE_SCRIPT_NAME = ''

# Non-restricted email port for development, run in a terminal:
# python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_PORT = 1025
EMAIL_SUBJECT_PREFIX = '[fabrydb Local] '

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = '/app/_site/static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/


# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# Staticfiles_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

# This is used as a "seed" for various hashing algorithms. This must be set to
# a very long random string (40+ characters)
SECRET_KEY = 'secret'
