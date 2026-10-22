from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Production: set DJANGO_SECRET_KEY, DJANGO_DEBUG=0 and DJANGO_ALLOWED_HOSTS in the
# environment. The fallbacks below keep local development working but are NOT safe
# for a public site. (Turning DEBUG off also needs static files served by the web
# server or WhiteNoise.)
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-gravel-calculator-pro-change-in-production-xyz123',
)

DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'

ALLOWED_HOSTS = [h.strip() for h in os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',') if h.strip()]

CSRF_TRUSTED_ORIGINS = [
    'https://gravelyardcalculator.com',
    'https://www.gravelyardcalculator.com',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'ckeditor',
    'ckeditor_uploader',
    'calculator',
    'blog',
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gravel_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gravel_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = 'blog_images/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': '100%',
        'extraPlugins': 'codesnippet',
    },
}

LOGIN_URL = '/admin/login/'

SILENCED_SYSTEM_CHECKS = ['ckeditor.W001']

# Trust the X-Forwarded-Proto header from the reverse proxy/load balancer so
# request.scheme, request.is_secure(), and request.build_absolute_uri() report
# "https" correctly (fixes canonical/og:url/sitemap showing http://).
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Cookie/HTTPS hardening, off by default so local development keeps working.
# Set DJANGO_SECURE=1 in production (behind HTTPS).
if os.environ.get('DJANGO_SECURE', '0') == '1':
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000

# Contact form notifications. With no EMAIL_HOST set, messages are still saved in
# the admin (Contact Messages) and the email is printed to the console.
CONTACT_NOTIFY_EMAIL = os.environ.get('CONTACT_NOTIFY_EMAIL', '')
if os.environ.get('EMAIL_HOST'):
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '1') == '1'
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
