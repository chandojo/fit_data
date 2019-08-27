import os
from os import environ
from .common import *

SECRET_KEY = os.environ['FITNESS_SECRET_KEY']
DEBUG = False

ALLOWED_HOSTS = ['fitnessinitiativedata.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USERNAME'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOSTNAME'],
        'PORT': os.environ['DB_PORT'],
    }
}

STATIC_ROOT = '/var/www/static/

SECURE_HSTS_SECONDS = 60
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER - True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# Create whitelist to allow React frontend access to API. Should NOT be set to 'True' before deployment
CORS_ORIGIN_ALLOW_ALL=False
