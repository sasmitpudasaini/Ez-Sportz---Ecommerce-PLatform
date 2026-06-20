"""
Django settings for config project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--ll^1q!2pn-)o^2!)(z+872q258flkw17uy@dek3a57^k*(%hu"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    # 1. Default Django Apps
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for allauth

    # 2. Third-party Apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # 3. Your Local Apps
    'users',
    'products',
    'cart',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware', # Required for allauth
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # FINAL FIX: This tells Django to look in the root templates folder
        "DIRS": [BASE_DIR / 'templates'], 
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript)
STATIC_URL = "static/"

# Media files (Product Images)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authentication Configuration
AUTH_USER_MODEL = 'users.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Allauth Settings
ACCOUNT_LOGIN_METHODS = {'username', 'email'}
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_FIELDS = ['email', 'username', 'password1', 'password2']
ACCOUNT_LOGOUT_ON_GET = True

# Where to go after login/logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

JAZZMIN_SETTINGS = {
    "site_title": "Ez Sportz Admin",
    "site_header": "Ez Sportz HQ",
    "site_brand": "EZ SPORTZ",
    "site_logo": None,  # You can add a path to a trophy or whistle logo here
    "welcome_sign": "Welcome to the Command Center. Lead the team.",
    "copyright": "Ez Sportz Ltd 2026",
    "search_model": ["cart.Order"],
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user-ninja", # Using ninja as a nod to elite athletes
        "auth.Group": "fas fa-users",
        "cart.Order": "fas fa-trophy",    # Changed from cart to trophy
        "cart.OrderItem": "fas fa-tshirt", # Changed to jersey icon
        "products.Product": "fas fa-running", # Changed from microchip to running icon
    },
    # Prioritizing the "Locker Room" (products) and "Orders"
    "order_with_respect_to": ["products", "cart", "auth"], 
}

JAZZMIN_UI_TWEAKS = {
    # "darkly" is great, but "flatly" or "lux" with custom colors also works.
    # Sticking with darkly to maintain that black gear look.
    "theme": "darkly", 
    "dark_mode_theme": "darkly",
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-danger", # This gives you that Ez Sportz Red accent
    "accent": "accent-danger",       # Highlights buttons/links in red
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-danger", # Red highlights on the sidebar menu
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme_cls": "darkly",
    "dark_mode_theme": "darkly",
}

# settings.py

# This sends emails to your terminal/console instead of a real server
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'