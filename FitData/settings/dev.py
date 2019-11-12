import os
from os import environ
from .common import *


SECRET_KEY = os.environ['FITNESS_SECRET_KEY']
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'fitnessinitiativedata.herokuapp.com']


# For production: create whitelist to allow React frontend access to API
CORS_ORIGIN_ALLOW_ALL=True
