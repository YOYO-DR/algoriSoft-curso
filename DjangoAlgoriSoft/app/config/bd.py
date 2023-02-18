import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}
MYSQL = {
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_django_curso',
        'USER':'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT':'3306'
    }
    
}
