from django.shortcuts import render
from django.http import HttpResponse
from core.erp.models import *

def miPrimeraVista(request):
   
   return render(request, 'home.html')

def vista2(request):
  data = {
     'name': 'yoiner',
    'categorias':Category.objects.all(),
    'productos': Product.objects.all()
    }
  return render(request,'second.html',data)
