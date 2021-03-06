import os

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
ADMIN_MEDIA_PREFIX = '/admin_media/'
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'demo.db'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_NAME
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'lettuce.django',
    'qhonuskan_votes',
    'app')

INTERNAL_IPS = ('127.0.0.1',)

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware')

ROOT_URLCONF = 'demo.urls'

SECRET_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcd'

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request')

STATIC_ROOT = os.path.join(PROJECT_PATH, "sitestatic/")

STATIC_URL = "/static/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder")

TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)