"""
Development settings.
Uses SQLite locally for convenience — switch to Postgres via DATABASE_URL when ready.
"""

from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost,127.0.0.1").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Disable password hashing in tests for speed (development only)
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
