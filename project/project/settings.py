
"""
Django settings for project project.
Generated by 'django-admin startproject' using Django 4.0.6.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+6hi10f*gk$ss^mb*pq9vuykl57u=q6*fzmsqh$ch#m_aq71tw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
########## django-allauthの設定 ############################
INSTALLED_APPS = [
    'crispy_forms',
    'app1.apps.App1Config',
    'app2.apps.App2Config',
    'app3.apps.App3Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django-allauthの設定 (allauth パッケージは django.contrib.sites を利用したプロジェクトでなければ動かない)
    'django.contrib.sites',
    # django-allauthの設定 (以下３つは、allauthパッケージに含まれるDjangoアプリケーション)
    'allauth',
    'allauth.account',
    # allauth.socialaccount・・・主にgmailなどのソーシャルアカウントによる認証機能に必要なもの
    #                           ※ ソーシャルアカウント認証を使わない場合でもアプリ追加が必須
    'allauth.socialaccount',
]
# ↓↓django-allauthの設定 (Djangoプロジェクトの識別子)
SITE_ID = 1

# django-allauthの設定
AUTHENTICATION_BACKENDS = (
    # 管理サイト用(ユーザー名認証)
    'django.contrib.auth.backends.ModelBackend',
    # メールアドレス・パスワードの両方を用いて認証するために必要
    'allauth.account.auth_backends.AuthenticationBackend'
)

# メールアドレス（とパスワード）で認証する
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# サインアップ（ユーザー登録）の時にユーザー名を尋ねる
ACCOUNT_USERNAME_REQUIRED = True
# サインアップ（ユーザー登録）の時にメールアドレスを尋ねる
ACCOUNT_EMAIL_REQUIRED = True
# メール認証を必須とする(mondatory, option, noneの３種類がある)
#                   mondatory: メール認証必須
#                   option   : メール認証なしでもログインできる
#                   none     : メール認証を行わない
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# メールをコンソール上に出力するための設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ログインURLの設定
LOGIN_URL = '/account/login/'
# ログイン後のリダイレクト先のURL
# LOGIN_REDIRECT_URL = '/index/'
LOGIN_REDIRECT_URL = 'app2:create_condition'
# ログアウト後のリダイレクト先のURL
ACCOUNT_LOGOUT_REDIRECT_URL = '/account/login/'
###########################################################
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # 直下のtemplatesを指定
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

# カスタムユーザーモデル
AUTH_USER_MODEL = 'app1.CustomUser'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [ BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'