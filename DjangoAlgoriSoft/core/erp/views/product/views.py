from django.http import JsonResponse
from django.urls import reverse_lazy
from core.erp.models import *
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.views.decorators.csrf import csrf_exempt
from core.erp.forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ProductListView(ListView):
  model = Product
  template_name= 'product/list.html'

  @method_decorator(csrf_exempt)
  @method_decorator(login_required)
  def dispatch(self, request, *args,**kwargs):
     return super().dispatch(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    try:
      action = request.POST['action']
      if action == 'searchdata':
        data = []
        for i in Product.objects.all():
          data.append(i.toJSON())
      else:
        data['error']='Ha ocurrido un error'
    except Exception as e:
       data['error']=str(e)
    return JsonResponse(data,safe=False)

  def get_queryset(self):
     return Product.objects.all()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title']='Listado de Productos'
    context['create_url']=reverse_lazy('erp:product_create')
    context['list_url']=reverse_lazy('erp:product_list')
    context['entity']='Productos'
    return context

class ProductCreateView(CreateView):
  model = Product
  form_class = ProductForm
  template_name = 'product/create.html'
  success_url = reverse_lazy('erp:product_list')

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
  

  def post(self, request,*args, **kwargs): #lo descomento pq vamos  a utilizar ajax
    data = {}
    try:
      # print(request.POST)
      # print(request.FILES)
      # aqui solo llega los datos tipo inputs
      print(request.POST)
      # aqui los datos tipo archivos
      print(request.FILES)
      # ya aqui confirmo que si llego la imagen
      action=request.POST['action']
      if action=='add':
        form=self.get_form()
        data = form.save()
      else:
        data['error']='No ha ingresado a ninguna opción'
    except Exception as e:
       data['error']=str(e)
       
    return JsonResponse(data)

  def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['title']='Creación de un producto'
     context['entity']='Productos'
     context['m_confirm']='el producto'
     context['list_url']=reverse_lazy('erp:product_list')
     context['action']='add'
     return context

class ProductUpdateView(UpdateView):
  model = Product
  form_class = ProductForm
  template_name = 'product/create.html'
  success_url = reverse_lazy('erp:product_list')

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super().dispatch(request, *args, **kwargs)

  def post(self, request,*args, **kwargs):
    data = {}
    try:
      action=request.POST['action']
      if action=='edit':
        form=self.get_form()
        data = form.save()
      else:
        data['error']='No ha ingresado a ninguna opción'
    except Exception as e:
       data['error']=str(e)
       
    return JsonResponse(data)

  def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['title']='Edición de un producto'
     context['entity']='Productos'
     context['m_confirm']='el producto'
     context['list_url']=reverse_lazy('erp:product_list')
     context['action']='edit'
     return context

class ProductDeleteView(DeleteView):
  model = Product
  template_name = 'product/delete.html'
  success_url = reverse_lazy('erp:product_list')

  @method_decorator(login_required)
  def dispatch(self,request, *args, **kwargs):
    self.object = self.get_object()
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    data = {}
    try:
      self.object.delete()
    except Exception as e:
      data['error']=str(e)
    return JsonResponse(data)

  def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['title']='Eliminación de un producto'
     context['entity']='Productos'
     context['list_url']=reverse_lazy('erp:product_list')
     return context
