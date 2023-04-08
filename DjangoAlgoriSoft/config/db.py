import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLITE={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3')
    }
}

MYSQL = {
  'default':{
  'ENGINE':'django.db.backends.mysql',
  'NAME':'db_django_curso', #nombre de la base de datos
  'USER':'root',
  'PASSWORD':'root',
  'HOST':'127.0.0.1', #servidor local o también puede ser 'localhost'
  'PORT':'3306'
  }
}
