# DJANGO APPLICATIONS
# Application definition
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # Third Party
    "rest_framework",
    "rest_framework.authtoken",
    "rest_auth",
    "rest_auth.registration",
    "rest_framework_simplejwt.token_blacklist",
    "drf_yasg",
    "timezone_field",

    # Own Application
    "apps.auth.apps.AuthConfig",
    "apps.users.apps.UsersConfig",

    # Third party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]
