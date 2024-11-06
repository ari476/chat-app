from .base import *
import os
import dj_database_url

ALLOWED_HOSTS = ['chat-project-cai2.onrender.com']

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

SECRET_KEY = os.environ.get("SECRET_KEY")

databases_url = os.environ.get("DATABASE_URL")

DATABASES["default"] = dj_database_url.parse(databases_url)

# set DJANGO_SETTINGS_MODULE="myproject.settings.production in server
