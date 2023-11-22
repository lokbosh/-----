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
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
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
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
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
    'formatters':{
        'verbose':{
            'format':'{levelname} {asctime} {module} {message}',
            'style':'{',
        },
        'with_path_and_exc_info': {
            'format': '{levelname} {asctime} {pathname} {exc_info} {message}',
            'style': '{',
        },
    
        
    },
    'filters':{
        'require_debug_true': {
            "()": 'django.utils.log.RequireDebugTrue',
        },
        
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        
    },
    'handlers':{
        'console':{
            'level':'DEBUG',
            'filters':['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file_general':{
            'level':'INFO',
            'filters':['require_debug_false'],
            'class': 'logging.FileHandler',
            'file_name':'general.log',
            'formatter':'verbose',
        },
        'file_errors':{
            'level':'ERROR',
            'class':'logging.FileHandlder',
            'file_name':'errors.log',
            'formatter':'with_path_and_exc_info',
        },
        'file_security':{
            'level':'INFO',
            'class':'logging.FileHandler',
            'filter':['require_debug_true'],
            'formatter':'verbose'
        },
        'mail_admins':{
            'level':'ERROR',
            'class':'django.utils.log.AdminEmailHandler',
            'filters':['require_debug_false'],
            'include_html': True,
            
        }
        
    },
    'loggers':{
        'django': {
            'handlers': ['console', 'file_general'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'file_errors'],
            'level': 'ERROR',
        },
        'django.server': {
            'handlers': ['mail_admins', 'file_errors'],
            'level': 'ERROR',
        },
        'django.template': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
        },
        'django.db.backends': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'INFO',
        },
    },
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

LANGUAGE_CODE = 'en-us'

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
