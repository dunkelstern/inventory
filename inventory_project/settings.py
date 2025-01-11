"""
Django settings for inventory_project project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
import asyncio
import socket
from urllib.parse import urlparse
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Externally visible URL of the server
SERVER_URL = os.environ.get('INVENTORY_EXTERNAL_URL', "http://127.0.0.1:8000")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('INVENTORY_SECRET_KEY', uuid4().hex)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('INVENTORY_DEBUG', "FALSE") == "TRUE")

parsed_url = urlparse(SERVER_URL)
ALLOWED_HOSTS: list[str] = [
    '.localhost',
    '127.0.0.1',
    '[::1]',
    parsed_url.hostname,
    socket.gethostbyname('localhost')
]

# Application definition

INSTALLED_APPS = [
    'inventory',
    'nested_admin',
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'inventory_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'inventory_project.wsgi.application'
ASGI_APPLICATION = 'inventory_project.asgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('INVENTORY_DB_HOST', 'localhost'),
        'NAME': os.environ.get('INVENTORY_DB_NAME', 'inventory'),
        'USER': os.environ.get('INVENTORY_DB_USER', 'inventory'),
        'PASSWORD': os.environ.get('INVENTORY_DB_PASSWORD', 'inventory')
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGES = [
    ("de", _("German")),
    ("en", _("English")),
]

LANGUAGE_CODE = os.environ.get('INVENTORY_LANGUAGE', 'en-us')

TIME_ZONE = os.environ.get('INVENTORY_TIMEZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('INVENTORY_STATIC_FILES', os.path.join(BASE_DIR, 'static'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('INVENTORY_MEDIA_FILES', os.path.join(BASE_DIR, 'media'))
SERVE_MEDIA_FILES = True

# Default page size for paginated content
PAGE_SIZE = int(os.environ.get('INVENTORY_PAGE_SIZE', "25"))
