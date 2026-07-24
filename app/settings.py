import os
from pathlib import Path

# BASE_DIR ni aniqlash
BASE_DIR = Path(__file__).resolve().parent.parent

# Maxfiy kalit (Production uchun muhit o'zgaruvchisidan olingan afzal)
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-in-production-key!')

# Vercel'da test rejimi
DEBUG=False
# Vercel domenlari va localhost uchun ruxsatlar
ALLOWED_HOSTS = ['*']  # Barcha domenlarga vaqtincha ruxsat berish
# O'rnatilgan ilovalar
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Bu yerga o'zingiz yaratgan app'larni qo'shing (masalan: 'main_app', 'games')
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise — Vercel'da static fayllarni yetkazib berish uchun
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Loyihangizning asosiy URL konfigratsiyasi
# 'myproject' o'rniga o'zingizning loyiha papkangiz nomini yozing!
ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # HTML shablonlar papkasi
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

WSGI_APPLICATION = 'app.wsgi.application'


# Ma'lumotlar bazasi (Boshlanishiga SQLite3)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Parol tekshiruvlari
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


# Tillar va vaqt sozlari
LANGUAGE_CODE = 'uz-uz'  # yoki 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# --- STATIC VA MEDIA FAYLLAR SOZLAMALARI (Vercel uchun eng muhim qismi) ---

STATIC_URL = '/static/'

# Loyihangiz ichidagi static manba papkasi
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# collectstatic buyrug'i barcha static fayllarni yig'adigan joy
STATIC_ROOT = BASE_DIR / 'staticfiles_build' / 'static'

# WhiteNoise yordamida static fayllarni saqlash va keshlar bilan ishlash
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Birlamchi ID maydon turi
DEFAULT_AUTO_FIELD = 'django.db.BigAutoField'

import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')