# -*- coding: utf-8 -*-
# Django settings for vbuchi project.

import os.path

from settings import *

DEBUG = False

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'vhotsyk_pycon',                      # Or path to database file if using sqlite3.
        'USER': 'vhotsyk',                      # Not used with sqlite3.
        'PASSWORD': '1FHjgr65',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Zurich'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qekr3^p8gj%3%9(p0#xm8k2om16*#k%2&amp;8rk*bq-es0t6uj^o$'

FORCE_SCRIPT_NAME = ''
