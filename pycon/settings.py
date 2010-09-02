# Django settings for inbucha project.
import os
PROJECT_DIR = os.path.dirname(__file__)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Volodymyr Hotsyk', 'gotsyk@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pycon.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

ugettext = lambda s: s # dummy ugettext function, as django's docs say

LANGUAGES = (
    ('en-us', ugettext('English')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_DIR + '/static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Save thumbnail images to a directory directly off MEDIA_ROOT, still
# keeping the relative directory structure of the source image.
# Result: MEDIA_ROOT + 'thumbs/photos/1_jpg_150x150_q85.jpg'
THUMBNAIL_BASEDIR = 'thumbs'

# Save thumbnail images to a sub-directory relative to the source image.
# Result: MEDIA_ROOT + 'photos/_thumbs/1_jpg_150x150_q85.jpg'
THUMBNAIL_SUBDIR = '_thumbs'

# Prepend thumnail filenames with the specified prefix.
# Result: MEDIA_ROOT + 'photos/__1_jpg_150x150_q85.jpg'
THUMBNAIL_PREFIX = '__'

THUMBNAIL_EXTENSION = 'png'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!u^%)37r%z^m$foduqunjq9110f1%oe%zf$z1s(98q36_t5n3@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'jogging.middleware.LoggingMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    PROJECT_DIR + '/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'sorl.thumbnail',
    'south',
    'jogging',
    'core',
)

EMAIL_FROM = 'do-not-reply@ua.pycon.org'

RECAPTCHA_PUBLIC_KEY = '6LfQxbwSAAAAAPCZZSoEvgD1NdxjYm_ROfFCmae-'
RECAPTCHA_PRIVATE_KEY = '6LfQxbwSAAAAAKBLJ3Qo36kC9djqTy5K0hJ-QMvQ'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile/'

from local_settings import *
from logging_settings import *

