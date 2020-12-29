EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")

EMAIL_HOST = env("EMAIL_HOST", default="email-smtp.us-east-1.amazonaws.com")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)

EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="no-reply@lighthousetech.io")
DEFAULT_REPLY_TO = env("DEFAULT_REPLY_TO", default="support@lighthousetech.io")
