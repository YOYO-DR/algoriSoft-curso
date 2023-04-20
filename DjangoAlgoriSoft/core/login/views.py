from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
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