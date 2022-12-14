from .base import *

DATABASES={
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME' : 'bloginfo',
        'USER':'root',
        'PASSWORD' : 'root',
        'HOST' : 'localhost',
        'PORT': '3306'

    }
}