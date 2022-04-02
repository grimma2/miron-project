import django_on_heroku
from decouple import config

from .base import *


SECRET_KEY = config('SECRET_KEY')

DEBUG = False

DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = ['grimma-django-first.herokuapp.com']

django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']
