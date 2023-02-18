from django.db import models
from datetime import datetime

class Type(models.Model): #1 a 1
  name=models.CharField(max_length=150,verbose_name='Nombre')

  def __str__(self):
    return self.name
   
  class Meta:
    verbose_name='Tipo'
    verbose_name_plural='Tipos'
    ordering=['id']#como quiere que se ordene

class Category(models.Model):#muchos a muchos
  name=models.CharField(max_length=150,verbose_name='Categoria')

  def __str__(self):
    return self.name
   
  class Meta:
    verbose_name='Categorias'
    verbose_name_plural='Categorias'
    ordering=['id']#como quiere que se ordene

class Empleado(models.Model):
  categ = models.ManyToManyField(Category) #asi le digo que la relacion estre Empleado y CAtegory es de muchos a muchos y va a crear una tabla intermedia para ello
  #si esta relacion de muchos a muchos quiero ponerle mas atributos, ya puedo crear aparte la clase de esa tabla, utilizando las foreingKeys más los atributos a ponerles
  type=models.ForeignKey(Type, on_delete=models.CASCADE) #1 a 1
  #asi lo relaciono con la otra tabla
  #con on_delete le digo que hacer si se llega a eleminar la clase "Type", CASCADE significa que borre todos los registros que dependan de esa clase type,y es obligatorio
  #SET_NULL, null=True (con esto le digo que si se borra se vuelvan valores nulos y que pueda aceptar esos valores)
  #con PROTECT le digo que no puede borrar esa tabla o elemento de esa tabla pq otra tabla lo necesita
  
  names=models.CharField(max_length=150,verbose_name='Nombres',default='Sin nombres')
  #names=models.TextField()
  #diferencia entre CharField y TExtField es que al charfield toca especificarle el maximo de caracteres, al textfield no
  #verbose_name es como un alias cuando se vaya a mostrar

  dni=models.CharField(max_length=10,unique=True,verbose_name='Dni') #unique= es para que sea unico
  date_joined=models.DateField(default=datetime.now,verbose_name='Fecha de registro')
  #DateField es para fechas
  #default es para poner un valor por defecto si no se ingresa alguno

  date_creation=models.DateTimeField(auto_now=True)#auto_now es para que se ingrese la fecha actual del registro y no se modifique mas
  date_update=models.DateTimeField(auto_now_add=True)#auto_now_add es para que cada vez que se ingrese un registro, se modifique con la fecha actual
  age=models.PositiveIntegerField(default=0) 
  #IntegerField valores enteros
  #PositiveIntegerField valores enteros positivos (y contrario con Negative)
  salary=models.DecimalField(default=0.00,max_digits=9,decimal_places=2)
  #max_digits para un maximo de digitos
  #decimal_places para un el maximo de decimales 
  estate=models.BooleanField(default=True) #para valores booleanos
  #gender = models.CharField(max_length=50)
  avatar=models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)#para imagenes, en upload_to le especifico la carpeta donde se guarde, el nombre y los "/" es que le digo que se guarde en modo de fecha en ese modo (y/m/d)
  cvitae=models.FileField(upload_to='cvitae/%Y/%m/%d',null=True,blank=True) #para guardar archivos, el null y blank en True significa que este campo puede estar vacio si se desea asi

  def __str__(self): #para mostrar una representacion de la clase o tabla
    #por ejemplo en las consultas, retornaria excencialmente esto, el nombre, ya con la notacion del punto, miro los demas valores
    return self.names #para retornar los nombres
  
  class Meta:
    verbose_name='Empleado'
    verbose_name_plural='Empleados'
    db_table='empleado' #nombre de la tabla
    ordering=['id']#como quiere que se ordene

    #luego de acabar el modelo, hay que ponerlo en la parte de INSTALLED_APPS en el archivo settings.py de configuracion con el nombre de la carpeta (en este caso, core.erp), debe ponerse igual que como esta en el archivo apps.py en el atributo name

    #al hacer el makemigrations para registrar este modelo, se registra y queda listo para hacer la migration o creacion de la tabla en la bd

#si no le especificamos a Django el ID de la tabla, el mismo crea el id

#si agrego una columna el me va a decir que le ponga un valor ´por defecto para no afectar si ya existen datos y le pongo 1, luego el valor

#si comento una tabla y aplico mikemigrations y luego migrate, borra esa tabla