from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

# Access environment variables
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Or your preferred database engine
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST", "localhost"),  # default to localhost if not set
        'PORT': os.getenv("DB_PORT", "5432"),       # default PostgreSQL port
    }
}