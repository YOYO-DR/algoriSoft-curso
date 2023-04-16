from django.db import models
from datetime import datetime
from core.erp.choices import gender_choices
from django.forms import model_to_dict

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return f'Nombre: {self.name}'
    def toJSON(self):
      #podria crear el diccionario manual pero donde tenga muchos atributos seria mala practica, ya django tiene una funcion para ello
      #puedo pasarle un arreglo en el parametro exclude con el nombre de los campos que no quiera que se retornen
      item = model_to_dict(self)
      return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']


# class Type(models.Model):
#   name = models.CharField(max_length=150,verbose_name='Nombre',unique=True)

#   def __str__(self):
#     return self.name
  
#   class Meta:
#     verbose_name = 'Tipo'
#     verbose_name_plural = 'Tipos'
#     ordering = ['id']

# class Category(models.Model):
#   name = models.CharField(max_length=150,verbose_name='Nombre')

#   def __str__(self):
#     return self.name
  
#   class Meta:
#     verbose_name = 'Categoria'
#     verbose_name_plural = 'Categorias'
#     ordering = ['id']

# class Employee(models.Model):
#   #se crea una tabla intermedia, con los 2 ids, pero si necesito ponerle más valores, entonces mejor creo la taba manual
#   categ = models.ManyToManyField(Category)
#   #CASCADE: borrar todo
#   #SET_NULL poner en nulo ese valor junto a null=True
#   #PROTECT no dejaria borrar un registro de type si hay algun registro con esa relación
#   type=models.ForeignKey(Type,on_delete=models.CASCADE)
#   #es para un input, el TextField para comentarios
#   names = models.CharField(max_length=150,verbose_name='Nombres')
#   #unique es para que sea unico
#   dni = models.CharField(max_length=10,unique=True,verbose_name='Dni')
#   #fecha de registro
#   date_joined = models.DateField(default=datetime.now,verbose_name='Fecha de registro')
#   date_created = models.DateField(auto_now_add=True)
#   date_updated = models.DateField(auto_now=True)
#   age = models.PositiveIntegerField(default=0)
#   salary = models.DecimalField(default=0.00,max_digits=9, decimal_places=2)
#   state = models.BooleanField(default=True)
#   #gender = models.CharField(max_length=50)
#   avatar =  models.ImageField(upload_to='avatar/%Y/%m/%d', null=True,blank=True)
#   cvitae =  models.FileField(upload_to='cvitae/%Y/%m/%d', null=True,blank=True)

#   def __str__(self):
#     return self.names
  
#   class Meta:
#     verbose_name = 'Empleado'
#     verbose_name_plural = 'Empleados'
#     #db_table = 'empleado'
#     ordering = ['id']
