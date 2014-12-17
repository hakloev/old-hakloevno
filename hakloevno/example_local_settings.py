import os
from settings import BASE_DIR
from django.contrib.messages import constants as messages

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = not DEBUG # Set to True in prod

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/'
)

ADMINS = (
    ('name', 'email@email.com'),
)

DEFAULT_FROM_EMAIL = "noreply@domain.com"

ALLOWED_HOSTS = ['.DOMAIN.NO']

SECRET_KEY = ''

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/ABSOLUTE_PATH/'
