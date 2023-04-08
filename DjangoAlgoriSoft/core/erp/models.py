from django.db import models
from datetime import datetime

class Type(models.Model):
  name = models.CharField(max_length=150,verbose_name='Nombre',unique=True)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Tipo'
    verbose_name_plural = 'Tipos'
    ordering = ['id']

class Category(models.Model):
  name = models.CharField(max_length=150,verbose_name='Nombre')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
    ordering = ['id']

class Employee(models.Model):
  #se crea una tabla intermedia, con los 2 ids, pero si necesito ponerle más valores, entonces mejor creo la taba manual
  categ = models.ManyToManyField(Category)
  #CASCADE: borrar todo
  #SET_NULL poner en nulo ese valor junto a null=True
  #PROTECT no dejaria borrar un registro de type si hay algun registro con esa relación
  type=models.ForeignKey(Type,on_delete=models.CASCADE)
  #es para un input, el TextField para comentarios
  names = models.CharField(max_length=150,verbose_name='Nombres')
  #unique es para que sea unico
  dni = models.CharField(max_length=10,unique=True,verbose_name='Dni')
  #fecha de registro
  date_joined = models.DateField(default=datetime.now,verbose_name='Fecha de registro')
  date_created = models.DateField(auto_now_add=True)
  date_updated = models.DateField(auto_now=True)
  age = models.PositiveIntegerField(default=0)
  salary = models.DecimalField(default=0.00,max_digits=9, decimal_places=2)
  state = models.BooleanField(default=True)
  #gender = models.CharField(max_length=50)
  avatar =  models.ImageField(upload_to='avatar/%Y/%m/%d', null=True,blank=True)
  cvitae =  models.FileField(upload_to='cvitae/%Y/%m/%d', null=True,blank=True)

  def __str__(self):
    return self.names
  
  class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    #db_table = 'empleado'
    ordering = ['id']