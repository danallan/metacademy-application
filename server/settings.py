# Copy this file to app_server/settings.py and adjust to your specification (it should work fine out of the box)

# Django settings for django_agfk project.
import os
import config


SETTINGS_PATH = os.path.realpath(os.path.dirname(__file__))
CLIENT_SERVER_PATH = SETTINGS_PATH
AGFK_PATH = os.path.realpath(os.path.join(SETTINGS_PATH,'../'))


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': config.DJANGO_DB_FILE,                 # Or path to database file if using sqlite3.
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
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(CLIENT_SERVER_PATH, 'static/media')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    ('css',os.path.join(CLIENT_SERVER_PATH, 'static/css')),
    ('images',os.path.join(CLIENT_SERVER_PATH, 'static/images')),
    ('fonts',os.path.join(CLIENT_SERVER_PATH, 'static/fonts')),
    ('javascript',os.path.join(CLIENT_SERVER_PATH, 'static/javascript')),
    ('lib',os.path.join(CLIENT_SERVER_PATH, 'static/lib')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(CLIENT_SERVER_PATH,'static/html/'),
    os.path.join(CLIENT_SERVER_PATH,'static/html/underscore-templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_bleach',
    'apps.maps',
    'apps.exercises',
    'apps.research',
    'south',
    'compressor',
    'lazysignup',
    'reversion',
    'tinymce',
)

# context processors
TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.tz",
                               "django.contrib.messages.context_processors.messages")

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filters': ['require_debug_false'],
            'filename': os.path.join(config.LOG_PATH, 'django.log')
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}


AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'lazysignup.backends.LazySignupBackend',
)

# Bleach settings
# Which HTML tags are allowed
BLEACH_ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'em', 'strong', 'a', 'span', 'img']

# Which HTML attributes are allowed
BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style', 'src', 'alt', 'width', 'height']

# Which CSS properties are allowed in 'style' attributes
BLEACH_ALLOWED_STYLES = [ 'font-family', 'font-weight', 
    'text-decoration', 'font-variant']

# Strip unknown tags if True, replace with HTML escaped characters if False
BLEACH_STRIP_TAGS = False

# Strip comments, or leave them in.
BLEACH_STRIP_COMMENTS = True

# default URL to redirect to after login
LOGIN_REDIRECT_URL = '/user'

INTERNAL_IPS = ("127.0.0.1",)

SERVER = 'http://'+ str(config.SERVER_IP) + ":" + str(config.SERVER_PORT)

# TinyMCE configuration
TINYMCE_JS_URL = os.path.join(STATIC_URL, "javascript/lib/tinymce-4.0.26/tinymce.min.js")

TINYMCE_JS_ROOT = os.path.join(CLIENT_SERVER_PATH, "static/javascript/lib/tinymce-4.0.26")

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'modern',
    'add_unload_trigger': False,
    'schema': 'html5',
    'statusbar': False,
    'plugins': 'advlist,autolink,autoresize,code,image,link',
}

# Compressor support in current django-tinymce does not work for TinyMCE 4 :(
TINYMCE_COMPRESSOR = False

# Add FQDN host of the server this is running on in production below
#ALLOWED_HOSTS = ['.domain.tld', 'host.amazonaws.com', '123.123.123.123']

from settings_local import *
