import sys
sys.path.append('../../')
#para ese error, si de la forma anterior no funciona entonces pongo la ruta del proyecto completa
# ejem: 
# sys.path.append('f:/programacion/Proyectos/AdminTrading/Online/Django/app/')

# Traceback (most recent call last):
#   File "f:\programacion\Proyectos\AdminTrading\Online\Django\app\core\list_ope\tests.py", line 3, in <module>
#     from core.list_ope.models import *
# ModuleNotFoundError: No module named 'core.list_ope'

from config.wsgi import *
#Para el problema de: django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
from core.erp.models import *
from datetime import datetime

#Listar (consultar)
#select * from tabla
query=Type.objects.all()

print(query)

#asi inserto los datos con el ORM
#insercion (insertar)
# t=Type()
# t.name='hola'
# t.save()

#insersion de un empleado y la llave foranea de Type
# t=Empleado()
# t.names='Daniel Rojas'
# t.type=Type(id=2) #asi ingreso la llave foranea
# t.dni=12345687
# t.age=20
# t.salary=800000.56
# t.estate=True
# t.save()

#otra froma
# t=Type(name='Prueba 2')
# t.save()

#otra forma
#t=Type(name='Prueba 3').save()

#edicion (actualizar)

# t=Type.objects.get(pk=1) #obtengo el registro a editar, con su id p llave primaria o primary key (puedo utilizar id o pk para obtener el registro)
# t.name='Accionista no' #ya obtenido el registro, simplemente modifico el valor de name, o valores
# t.save()

#eliminacion

#t=Type.objects.get(pk=1) #obtengo el registro
#t.delete() #elimino el registro

#ORM II
# si les pongo el count() me dira cuantos registros me trae
# obj=Type.objects.filter(name__contains='pr') #pido los registros que por "name" contenga 'pr'
# obj=Type.objects.filter(name__icontains='terry') #con "icontains" le digo que no importa si tiene mayusculas o minusculas
# obj=Type.objects.filter(name__startswith='p') #los que inicien con 'p'
# obj=Type.objects.filter(name__endswith='a') #los que termien con 'a'
# obj=Type.objects.filter(name__exact='a') #que sea exactamente igual a lo que ponga,iexact tambien pero sin contar mayuculas y minusculas
# obj=Type.objects.filter(name__in=['viba','hola']) #le paso un arreglo para que me pase los que tienen esos elementos
# obj=Type.objects.filter(name__in=['viba','hola']).count() #le paso un arreglo para que me pase los que tienen esos elementos
# obj=Type.objects.filter(name__in=['viba','hola']).query #esto me trae la consulta que realiza
# obj=Type.objects.filter(name__endswith='a').exclude(pk=5) #con exclude, excluyo lo que quiero que no me traiga

# print(obj[0].name) #a cada objeto o registro, con la notacion de "." puedo acceder al name o id (columnas o valor de ellas)

#puedo iterarlos con un for
# for i in Type.objects.filter(name__endswith='a')[:2]: 
  #si pongo [:2] le digo que me traiga los 2 ultimos
  #[2:3] que inicie en el 2 y termine en el 3
  # print(i.name)

# obj = Empleado.objects.filter(type_id=2) #asi traeria los empleados que tengan el type de 1, ejemplo, si tengo 5 accionistas y los accionistas tengan el id 1, al hacer esta busqueda, me trae a todos los empleados "accionistas" (osea, id=1)
# print(obj)

#en la documentacion de Django, puedo buscar todas las funciones que puede realizar la funcion filter()
