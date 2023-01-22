"""Main app settings  """
from pathlib import Path
import os
from allauth.account import app_settings as allauth_settings
from django.conf import settings


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

NPM_BIN_PATH = '/home/gitpod/.nvm/versions/node/v16.13.0/bin/npm'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1yu+4-7yj3ieek*gnas6b1%pc^_pzv=qsy_7i+6$25-le!e$0f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tailwind',
    'theme',

    'home',
    'piggyaccount',
    'django_browser_reload',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'profiles',
    # otp authentication
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    # Enable two-factor auth.
    'allauth_2fa',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',  # for otp
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Reset login flow middleware. If this middleware is included, the login
    # flow is reset if another page is loaded between login and successfully
    # entering two-factor credentials.
    'allauth_2fa.middleware.AllauthTwoFactorMiddleware',
]

ROOT_URLCONF = 'piggybank.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]


# Set the allauth adapter to be the 2FA adapter.
ACCOUNT_ADAPTER = 'allauth_2fa.adapter.OTPAdapter'


TEMPLATE_EXTENSION = getattr(
    settings, "ALLAUTH_2FA_TEMPLATE_EXTENSION", allauth_settings.TEMPLATE_EXTENSION
)

ALWAYS_REVEAL_BACKUP_TOKENS = bool(
    getattr(settings, "ALLAUTH_2FA_ALWAYS_REVEAL_BACKUP_TOKENS", True)
)

REMOVE_SUCCESS_URL = getattr(
    settings, "ALLAUTH_2FA_REMOVE_SUCCESS_URL", "two-factor-setup"
)

SETUP_SUCCESS_URL = getattr(
    settings, "ALLAUTH_2FA_SETUP_SUCCESS_URL", "two-factor-backup-tokens"
)


WSGI_APPLICATION = 'piggybank.wsgi.application'


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
