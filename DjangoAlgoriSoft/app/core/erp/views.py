from django.shortcuts import render
from django.http import HttpResponse
from core.erp.models import *

def miPrimeraVista(request):
  return HttpResponse('<h1>Mi primera vista</h1>')

def vista2(request):
  data = {
    'productos':Product.objects.all()
    }
  return render(request, 'index.html', data)

def vista3(request):
  data = {
    'categorias':Category.objects.all()
  }
  return render(request,'second.html',data)