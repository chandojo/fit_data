import os
from os import environ
from .common import *
import dj_database_url

SECRET_KEY = os.environ['FITNESS_SECRET_KEY']
DEBUG = False

ALLOWED_HOSTS = ['fitnessinitiativedata.herokuapp.com',]

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

SECURE_HSTS_SECONDS = 60
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

CORS_ORIGIN_WHITELIST = [
    'https://www.fitinitproj.com'
]
