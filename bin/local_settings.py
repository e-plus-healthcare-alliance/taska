# Docker local settings
import os


STATIC_ROOT = '/workflow-management/collected/'
MEDIA_ROOT = '/workflow-management/collectedmedia/'

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', True)
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'admin@example.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'password_here')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', "admin@example.com")

WEBPAGE_URL = os.environ.get('PUBLIC_IP', 'example.com')

SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME', 'taska')

EMAIL_URL = os.environ.get('EMAIL_URL', WEBPAGE_URL)
ALLOWED_HOSTS = [
]

BASE_URL = os.environ.get('BASE_DIR', '')+'/'

# I dont like this here very much but i cant make it work with nginx otherwise... on a subdirectory at least
FORCE_SCRIPT_NAME = os.environ.get('BASE_DIR', '')+'/'

RAVEN_URL = os.environ.get('RAVEN_URL', 'empty')

WKHTMLTOPDF_CMD = '/usr/local/bin/wkhtmltopdf'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

