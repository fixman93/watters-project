
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..', x)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ekb^5devfb*6scogrzibmur4z!v==0+iui7k0@6u6u8m6%d(i_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'rest_framework',
    'rest_framework.authtoken',
    'custom_user',
    'djoser',

    'apps.api',
    'apps.core',
    'apps.catalogue',
    'apps.dress_room',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': location('db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_ROOT = location("static/media")
STATIC_URL = '/static/'
STATIC_ROOT = location('static')
STATICFILES_DIRS = (
    location('project_static/'),
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.tz",
                               "django.contrib.messages.context_processors.messages",

                               'django.core.context_processors.request',)

TEMPLATE_DIRS = (
    location('templates'),
)

APPEND_SLASH = True

AUTH_USER_MODEL = 'core.User'

# Amazon SES
EMAIL_SUBJECT_PREFIX = '[Watters] '
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'AKIAJXQLJT32R7SQUROQ'
EMAIL_HOST_PASSWORD = 'AnXcB8qvUuZBpFex7gt23b3cyojISWrjU+rAezdfKSJF'
EMAIL_USE_TLS = True
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
DEFAULT_FROM_EMAIL = 'anthony@modcocreative.com'

#Grappelli
GRAPPELLI_ADMIN_TITLE = "Watters"
GRAPPELLI_CLEAN_INPUT_TYPES = False

#REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

DJOSER = {
    'LOGIN_AFTER_REGISTRATION': True,  #required by satellizer.js
}