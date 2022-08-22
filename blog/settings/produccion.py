from .base import *


DEBUG = True

CSRF_TRUSTED_ORIGINS = ['https://camaracomerciovillaangela.herokuapp.com/'] 

ALLOWED_HOSTS = ['camaracomerciovillaangela.herokuapp.com']

DATABASES = {    
    'default':
        {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dagpccm1e5ucls',
            'USER': 'cqvoeggyjtejfn',
            'PASSWORD': '84730f5c7c2db2fc6a6d1a3377a0c57f31c96f8118c26d676c170da6287512d9',
            'HOST': 'ec2-44-206-137-96.compute-1.amazonaws.com',
            'PORT': 5432,           
            
        },

}


