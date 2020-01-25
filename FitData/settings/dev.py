import os
from os import environ
from .common import *


SECRET_KEY = os.environ['FITNESS_SECRET_KEY']
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost',
                 'fitnessinitiativedata.herokuapp.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILE_DIRS = (
    os.path.join(BASE_DIR, 'static')
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# For production: create whitelist to allow React frontend access to API
CORS_ORIGIN_ALLOW_ALL = True
