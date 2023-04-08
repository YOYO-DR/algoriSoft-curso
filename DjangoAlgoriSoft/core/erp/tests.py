from config.wsgi import *
from core.erp.models import *

#ORM I
#LISTAR

# select * from tabla
# query=Type.objects.all()
# print(query)

#Insertar
#tipo 1
# t=Type()
# t.name='Prueba'
# t.save()
# tipo 2
#t=Type(name='prueba 2').save()

#Actualizar

#me traigo el objeto y modifico lo que quiera
# t=Type.objects.get(id=1)
# t.name='Accionista actu'
# t.save()

#eliminacion
#con un try except puedo controlar los errores
#obtengo el objeto
# t=Type.objects.get(id=1)
# t.delete()

# ORM II
# for i in range(5):
#   Type(name=input('Ingresa el tipo: ')).save()
