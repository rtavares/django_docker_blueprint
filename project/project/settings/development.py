from .base import *   # noqa: F403  # Exceptional situation. 'Import star' should be avoided

DEBUG = True
RUN_MODE = 'Development'

ALLOWED_HOSTS = ['*']

# Real credentials should never be committed.
# Should be acquired from environment variables or local config file set on the host server.
# TODO: Create a separeted set ef onv vars to DEV and PRD
DATABASE_NAME = os.environ.get('DATABASE_NAME')  # noqa: F405
DATABASE_USER = os.environ.get('DATABASE_USER')  # noqa: F405
DATABASE_PASS = os.environ.get('DATABASE_PASS')  # noqa: F405
DATABASE_HOST = os.environ.get('DATABASE_HOST')  # noqa: F405
DATABASE_PORT = os.environ.get('DATABASE_PORT')  # noqa: F405

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

USE_SQLITE = False  # Fallback to use Sqlite as DB

INSTALLED_APPS += ['debug_toolbar', ]    # noqa: F405

if USE_SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': DATABASE_NAME + '.sqlite',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASS,
            'HOST': DATABASE_HOST,
            'PORT': DATABASE_PORT,
        }
    }

STATIC_ROOT = os.path.join(BASE_DIR, '../../', 'static')  # noqa: F405

MEDIA_ROOT = os.path.join(BASE_DIR, '../', 'media')  # noqa F405
