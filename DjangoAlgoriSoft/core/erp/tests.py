#lo ejecuto aqui porque esto no lo ejecuto con el manage.py
from dotenv import load_dotenv
load_dotenv('./.env')

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
#el __contains es que traigo los objetos que por su columna dicha (en este caso, name) que contenga el 'pre'
# obj=Type.objects.filter(name__contains='terry')
#con __icontains es para que ignore las mayusculas y minusculas
# obj=Type.objects.filter(name__icontains='terry')
#que inicie con lo que le pase
# obj=Type.objects.filter(name__startswith='p')
# que termine con lo que le pase
# obj=Type.objects.filter(name__endswith='p')
# que sea exactamente igual, si le pongo iexact, ignorara las mayusculas y minusculas
# obj=Type.objects.filter(name__exact='presidente')
# me trae los objetos que tengas almenos uno de los valores que le pase en un arreglo
# obj=Type.objects.filter(name__in=['viba','hola','yoiner'])
# puedo contar los objetos que lleguen
# obj=Type.objects.filter(name__in=['viba','hola','yoiner']).count()
# con query me trae la consulta sql la cual estoy ejecutando
# obj=Type.objects.filter(name__contains='pr').query
# puedo excluir
# obj=Type.objects.filter(name__endswith='a').exclude(id=5)
# puedo iterarlos

# esto traeria todos los empleados que tengan cierto id
# Employee.objects.filter(type_id=1)

# for i in Type.objects.filter(name__endswith='a'):
  # print(i.name)
