from django.shortcuts import redirect, render
from core.erp.models import *
from django.views.generic import ListView

def category_list(request):
    data={
        'title':'Listado de Categorias',
        'categories':Category.objects.all()
    }
    return render(request, 'category/list.html',data)

class CategoryListView(ListView):
  model = Category
  #el objecto que tiene las categorias se llama object_list
  template_name= 'category/list.html'

  def dispatch(self, request, *args,**kwargs):
     #esta funcion maneja como llegan los metodos de las peticiones
    #  if request.method == 'GET':
    #     return redirect('erp:category_list2')
     return super().dispatch(request, *args, **kwargs)

  def get_queryset(self):
     #esta funcion es la que hace la consulta la cual se guarda en el object_list, puedo modificarla tambien
     #puedo hasta aplicar filtros para mostrar
     #return Category.objects.filter(name__startswith='B')
     return Category.objects.all()

  def get_context_data(self, **kwargs):
    #con super traigo los datos que ya tiene la clase y agrego lo que quiera
    context = super().get_context_data(**kwargs)
    context['title']='Listado de Categorias'
    #puedo modificar esa clave la cual tiene el object_list
    #context['object_list'] = Product.objects.all()
    return context

#es mejor trabajar con las vistas pq al trabajar con funciones, es dificil hacer mantenimiento y más cuando se trabaja con los metodos post, get etc, para eso, las clases ya tiene una forma mas ordenada y limpia para trabajar