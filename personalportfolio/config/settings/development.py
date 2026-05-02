"""
Development settings.
Uses SQLite locally for convenience — switch to Postgres via DATABASE_URL when ready.
"""

import dj_database_url
from decouple import config

from .base import *

DEBUG = True

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost,127.0.0.1").split(",")

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL"),
        conn_max_age=600,
    )
}

# Disable password hashing in tests for speed (development only)
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
