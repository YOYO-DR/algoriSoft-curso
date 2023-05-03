from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from core.erp.forms import TestForm
from core.erp.models import Product

class TestView(TemplateView):
    template_name='tests.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required) 
    def dispatch(self, request, *args,**kwargs):
     return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
      data={}
      try:
        action = request.POST['action']
        if action == 'search_product_id':
          data=[]
          for i in Product.objects.filter(cat_id=request.POST['id']):
             data.append({'id':i.id, 'name':i.name})
        else:
          data['error']='Ha ocurrido un error'
      except Exception as e:
         data['error']=str(e)
         #recordar que como voy a retornar un arreglo o coleccion, el JsonResponse debe tener el safe en False
      return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Selects anidados | Django'
        context['form']=TestForm()
        return context
    