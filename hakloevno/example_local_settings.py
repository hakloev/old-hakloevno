import os
from settings import BASE_DIR
from django.contrib.messages import constants as messages

DEBUG = True
TEMPLATE_DEBUG = DEBUG

COMPRESS_ENABLED = not DEBUG # Set to True in prod

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
)

ALLOWED_HOSTS = ['*']

SECRET_KEY = ''

ADMINS = (
    ('you', 'you@domain.no'),
)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'dev@domain.no'
SERVER_EMAIL = 'dev-error@domain.no'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/path/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/path/'
