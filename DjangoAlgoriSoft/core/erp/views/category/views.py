from django.http import JsonResponse
from django.shortcuts import redirect, render
from core.erp.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

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

  #esto es un metodo decorador, que po ejemplo puedo hacer una verificacion antes de ejecutar el dispatch u otra funcion, en este caso, no lo dejo entrar a la pagina (GET) hasta que este logueado
  #@method_decorator(login_required)
  #con este decorador, le quito la proteccion solo en esta vista, para el metodo post, y va aqui pq el dispatch es el que recibe los metodos del request
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args,**kwargs):
     #esta funcion maneja como llegan los metodos de las peticiones
    #  if request.method == 'GET':
    #     return redirect('erp:category_list2')
     return super().dispatch(request, *args, **kwargs)
  
  #puedo editar el metodo post, cuando hago una peticion sin el codigo de seguridad, tirara error
  def post(self, request, *args, **kwargs):
    data = {}
    try:
      data = Category.objects.get(pk=request.POST['id']).toJSON()

    except Exception as e:
       data['error']=str(e)
       
    return JsonResponse(data)

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