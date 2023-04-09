from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
from core.erp.models import *
def myfirstview(request):
  data = {
    'name':'Yoiner',
    'categories':Category.objects.all()
  }
  return render(request,'index.html',data)

def mysecondview(request):
  data = {
    'name':'Yoiner',
    'products':Product.objects.all()
  }
  return render(request,'second.html',data)