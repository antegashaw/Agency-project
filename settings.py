import os
from pathlib import Path

# 1. Base Directory (ይህ በመደበኛነት ያለውን ተጠቀም)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 2. Security (ይህ ለሙከራ ነው)
SECRET_KEY = 'django-insecure-your-key-here' # ያንተን ኦሪጅናል ቁልፍ ተጠቀምበት
DEBUG = True
ALLOWED_HOSTS = ['*']

# 3. Installed Apps (ያንተ አፕሊኬሽን 'registration' መሆኑን አረጋግጥ)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration', # እዚህ ጋር መኖሩን አረጋግጥ
]

# 4. Middleware (ይህ በመደበኛነት ያለውን ተጠቀም)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 5. Templates (ይህንን ክፍል አረጋግጥ)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # templates ፎልደር ካለህ
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

# 6. Database (ይህ በመደበኛነት ያለውን ተጠቀም)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 7. Static Files (ይህንን ክፍል ብቻ አስገባ)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'registration/static')]