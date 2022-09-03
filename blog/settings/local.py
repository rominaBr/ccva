from .base import *


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default':
        {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ccva2',
            'USER': 'postgres',
            'PASSWORD': 'romi',
            'HOST': 'localhost',
            'PORT': '5432',           
            
        },

}

DATABASE_ROUTER = ['database_routers.auth_router.AuthRouter']

#email smtp:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp-mail.outlook.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER= config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


