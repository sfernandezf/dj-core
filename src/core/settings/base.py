"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
"""
import os
import sys
import environ


# PROJECT DIRECTORY
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# APPS_DIR = os.path.join(BASE_DIR, 'apps')
# Workaround for project directory
# sys.path.insert(0, APPS_DIR)


# ENVIRONMENT
# django-environ (https://django-environ.readthedocs.io/en/latest/)
env = environ.Env()
env_file = (
    os.path.join(BASE_DIR, ".env")
    if os.path.exists(os.path.join(BASE_DIR, ".env"))
    else None
)
environ.Env.read_env(env_file)
ENVIRONMENT = env("ENVIRONMENT", default="local")


# DJANGO SECURITY
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOST", default=[])
if ENVIRONMENT == "local":
    ALLOWED_HOSTS += ["127.0.0.1", "localhost"]


# DATABASE
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {"default": env.db()}

# DJANGO URLS
ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"
APPEND_SLASH = True

# DJANGO MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# DJANGO TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# DJANGO INTERNALIZATION
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
