"""
Django settings for news project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7ppie(-_=%d58=3av^&n@1#cuj1p$qmc47%=)e4co7d!pcs38-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'simpleapp.apps.SimpleappConfig',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    "django_apscheduler",
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        'TIMEOUT': 30
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACKS_LATE = True
SITE_URL = 'http://127.0.0.1:8000'
LOGIN_REDIRECT_URL = "/news"

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mendatory'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "Lokboshh@yandex.ru"
EMAIL_HOST_PASSWORD = "ymwkdxlhavnkfqpg"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "Lokboshh@yandex.ru"
SERVER_EMAIL = "Lokboshh@yandex.ru"

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'basic.middlewares.TimezoneMiddleware'
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR,'locale')
] 
LANGUAGE_CODE = 'ru'
LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

ROOT_URLCONF = 'news.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` обязательно нужен этот процессор
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'news.wsgi.application'

LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'filters': {
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},
    },
    'formatters': {
        'format_debug': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },

        'format_warning_mail': {
            'format': '{asctime} {levelname} {message} {pathname} ',
            'style': '{',
        },

        'format_general_security_info': {
            'format': '{asctime} {levelname} {message} {module} ',
            'style': '{',
        },

        'format_error_critical': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info} ',
            'style': '{',
        },
    },

    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_debug',
        },

        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_warning_mail',
        },

        'console_gen_sec_info': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'format_general_security_info',
            'filename': 'general.log',
        },

        'console_error_critical': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_error_critical',
        },

        'errors_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'format_error_critical',
            'filename': 'errors.log',
        },

        'security_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'format_general_security_info',
            'filename': 'security.log',
        },

        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'format_warning_mail',
        },
    },


    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_gen_sec_info', 'console_error_critical', ],
            'level': 'INFO',
            'propagate': True,
        },

        'django.request': {
            'handlers': ['errors_file', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },

        'django.server': {
            'handlers': ['errors_file', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },

        'django.template': {
            'handlers': ['errors_file', ],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.db.backends': {
            'handlers': ['errors_file' ],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.security': {
            'handlers': ['security_file', ],
            'level': 'INFO',
            'propagate': False,
        },
    }
}       
      

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'Ochirov2004',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/



TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS = [
    BASE_DIR / "static"
]

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'
APSCHEDULER_RUN_NOW_TIMEOUT = 25
