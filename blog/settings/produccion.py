from .base import *


DEBUG = True

CSRF_TRUSTED_ORIGINS = ['https://camaracomerciovillaangela.herokuapp.com/'] 

ALLOWED_HOSTS = ['camaracomerciovillaangela.herokuapp.com']

DATABASES = {    
    'postgresql':
        {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dagpccm1e5ucls',
            'USER': 'cqvoeggyjtejfn',
            'PASSWORD': '84730f5c7c2db2fc6a6d1a3377a0c57f31c96f8118c26d676c170da6287512d9',
            'HOST': 'ec2-44-206-137-96.compute-1.amazonaws.com',
            'PORT': 5432,           
            
        },
    'default':
        {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd41iq1opootdjr',
            'USER': 'oagprslwacopuy',
            'PASSWORD': '84730f5c7c2db2fc6a6d1a3377a0c57f31c96f8118c26d676c170da6287512d9',
            'HOST': 'bc502c76413bf9190c32b0bf2605eea2b3dafe3b456522bec6876c5b8acc7ce6',
            'PORT': 5432,           
            
        },

}


