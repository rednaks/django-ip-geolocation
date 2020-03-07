"""Django settings."""
# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
from tests.backend_mock import BackendMock

# import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'tests.urls'

INSTALLED_APPS = [
]

MIDDLEWARE = [
    'django_ip_geolocation.middleware.IpGeolocationMiddleware',
]


IP_GEOLOCATION_SETTINGS = {
    'BACKEND': BackendMock,
    'BACKEND_API_KEY': '',
    'BACKEND_EXTRA_PARAMS': {},
    'BACKEND_USERNAME': '',
    'RESPONSE_HEADER': 'X-IP-Geolocation',
    'ENABLE_REQUEST_HOOK': True,
    'ENABLE_RESPONSE_HOOK': True,
    'ENABLE_COOKIE': False,
    'FORCE_IP_ADDR': None,
}

SITE_ID = 1
