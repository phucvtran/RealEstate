"""
Django settings for btre project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os, json
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0u3_f-^f+xzh80gtn_3z(ho=^k1_i2g-78*07@xu*tdsn9w7^^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'realtors.apps.RealtorsConfig',
    'listings.apps.ListingsConfig',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'btre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'btre.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btredb',
        'USER': 'postgres',
        'PASSWORD': '0112',
        'HOST': 'localhost'

    }
}

def readfile(filename):
    with open(filename) as f:
        data = json.load(f)
        f.close()
        return data

# def init():
#     global for_sale_data
#     for_sale_data = readfile('forsalelisting.json')
#     global for_rent_data
#     for_rent_data = readfile('forrentlisting.json')

for_rent_data = readfile('forrentlisting.json')
for_sale_data = readfile('forsalelisting.json')
#search_data = {}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT=os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'btre/static')
]

# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# # Email
# EMAIL_HOST = 'smtpout.secureserver.net'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'tran@pullova.com'
# EMAIL_HOST_PASSWORD = 'Seattle2018'
# EMAIL_USE_TLS = True

REALTOR_API_KEY = config('REALTOR_API_KEY', default='')
GOOGLE_MAP_API_KEY = config('GOOGLE_MAP_API_KEY', default='')
REALTOR_API_HOST = config ('REALTOR_API_HOST', default='')
REALTOR_API_FORSALE_URL = config ('REALTOR_API_FORSALE_URL', default ='')
REALTOR_API_FORRENT_URL = config ('REALTOR_API_FORRENT_URL', default ='')
REALTOR_API_SALE_LIMIT = config ('REALTOR_API_SALE_LIMIT', default ='')
REALTOR_API_RENT_LIMIT = config ('REALTOR_API_RENT_LIMIT', default ='')
REALTOR_API_DEFAULT_CITY = config('REALTOR_API_DEFAULT_CITY', default ='')
REALTOR_API_DEFAULT_STATE = config('REALTOR_API_DEFAULT_STATE', default ='')

try:
    from .local_settings import *
except ImportError:
    pass