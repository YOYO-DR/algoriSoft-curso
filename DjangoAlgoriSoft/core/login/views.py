from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

class LoginFormView(LoginView):
  #no le ponemos el form_class porque si inspeccionamos el LoginView ya viene con el form_class del AuthenticationForm
  template_name = 'login.html'

  def dispatch(self, request, *args, **kwargs):
    #si ya esta autenticado, lo redirecciono a la vista de category_list
    if request.user.is_authenticated:
      return redirect('erp:category_list')
    #de lo contrario, que entre normal al login
    return super().dispatch(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Iniciar sesión'
    return context
  
class LoginFormView2(FormView):
  #la vista formview debe recibir el form_class si o si, en este caso le pasamos el formulario de autenticación
  form_class = AuthenticationForm
  template_name = 'login.html'
  #si el formulario sale exitoso, lo redirecciono a la vista de las categorias
  success_url = reverse_lazy('erp:category_form')

  def dispatch(self, request, *args, **kwargs):
    #y pues modifico el metodo dispatch para que solo pueda entrar si no esta logueado
    if request.user.is_authenticated:
      return redirect('erp:category_list')
    return super().dispatch(request, *args, **kwargs)

  #recordar que el formview trabaja con estas funciones, dorm_valid y form_invalid
  #si el metodo es exitoso, inicio sesión con la funcion login
  def form_valid(self, form):
    #en el self viene el request, y en el form, para obtener el usuario que se esta logueando, utilizamos su funcion de get_user para obtenerlo del form
    login(self.request, form.get_user())
    #y lo redireccionamos con un HttpResponseRedirect y le paso la ruta de exito
    return HttpResponseRedirect(self.success_url)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Iniciar sesión'
    return context
