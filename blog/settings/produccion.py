from .base import *


DEBUG = True

CSRF_TRUSTED_ORIGINS = ['https://camaracomerciovillaangela.herokuapp.com/'] 

ALLOWED_HOSTS = ['camaracomerciovillaangela.herokuapp.com']

DATABASES = {   
    
    'default':
        {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd41iq1opootdjr',
            'USER': 'oagprslwacopuy',
            'PASSWORD': 'bc502c76413bf9190c32b0bf2605eea2b3dafe3b456522bec6876c5b8acc7ce6',
            'HOST': 'ec2-44-195-100-240.compute-1.amazonaws.com',
            'PORT': 5432,           
            
        },

}

#email smtp:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp-mail.outlook.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER= os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


