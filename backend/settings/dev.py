from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
# Use a Sqlite database by default
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': location('db.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
DEBUG_TOOLBAR_PATCH_SETTINGS = False

RAVEN_CONFIG = {}


THUMBNAIL_DEBUG = True