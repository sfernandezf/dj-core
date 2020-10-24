from split_settings.tools import include


INSTALLED_APPS = [
    "users.apps.UsersConfig",
]


include(
    "base.py",
    "rest.py",
    "storage.py",
    "auth.py",
    "email.py",
    "swagger.py",
)
