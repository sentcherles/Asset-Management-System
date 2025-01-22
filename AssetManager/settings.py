from pathlib import Path
import os
from django.conf import settings
from django.conf.urls.static import static

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-@a+l1z+-b4qd_jcbr$h2h%654@@78y1+0)np(6hswdw%+wzqjk'

DEBUG = True

ALLOWED_HOSTS = ['*']
ALLOWED_IPS = ['127.0.0.1', '::1', '*']

INSTALLED_APPS = [
    'Assets.apps.AssetsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Assets.middleware.LoginRequiredMiddleware',
    'Assets.middleware.RedirectAuthenticatedMiddleware',
]

ROOT_URLCONF = 'AssetManager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Assets', 'website')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': True,
        },
    },
]

WSGI_APPLICATION = 'AssetManager.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Drephere$default',
        'USER': 'Drephere',
        'PASSWORD': 'Xajsasjda1',
        'HOST': 'Drephere.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = '/home/Drephere/AssetManagementSystem/staticfiles'


MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/Drephere/AssetManagementSystem/media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/verification/'
LOGOUT_REDIRECT_URL = '/register/'

SITE_URL = 'https://Drephere.pythonanywhere.com'
