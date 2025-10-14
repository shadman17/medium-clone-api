from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="nWkwtH2RPfhCYkH_nfpfLixu81sU-dDNEKNQ1qwSRRt6VbP7s-s",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

CSRF_TRUSTED_ORIGINS = ["http://localhost:8090", "http://127.0.0.1:8090"]
