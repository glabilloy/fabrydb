import os
from global_settings import *

try:
    from local_settings import *
    from local_settings_secret import *
except ImportError:
    import warnings
    warnings.warn('Local settings have not been found (src.conf.local_settings). Trying to import Heroku config...')

    try:
        from local_settings_heroku import *
        from local_settings_heroku_secret import *
        warnings.warn('Local Heroku config loaded')

    except ImportError:
        warnings.warn('Heroku local settings not found neither (src.conf.local_settings_heroku)')


# FORCE_SCRIPT_NAME overrides the interpreted 'SCRIPT_NAME' provided by the
# web server. since the URLs below are used for various purposes outside of
# the WSGI application (static and media files), these need to be updated to
# reflect this alteration
if FORCE_SCRIPT_NAME:
    ADMIN_MEDIA_PREFIX = os.path.join(FORCE_SCRIPT_NAME, ADMIN_MEDIA_PREFIX[1:])

    STATIC_URL = os.path.join(FORCE_SCRIPT_NAME, STATIC_URL[1:])
    MEDIA_URL = os.path.join(FORCE_SCRIPT_NAME, MEDIA_URL[1:])

    LOGIN_URL = os.path.join(FORCE_SCRIPT_NAME, LOGIN_URL[1:])
    LOGOUT_URL = os.path.join(FORCE_SCRIPT_NAME, LOGOUT_URL[1:])
    LOGIN_REDIRECT_URL = os.path.join(FORCE_SCRIPT_NAME, LOGIN_REDIRECT_URL[1:])


# This is used as a "seed" for various hashing algorithms. This must be set to
# a very long random string (40+ characters)
SECRET_KEY = 'read from secret settings'

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_PATH, '_site/static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
