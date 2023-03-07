from django.urls import path
from core.erp.views import *

app_name='erp'

urlpatterns = [
  path('uno/',miPrimeraVista),
  path('dos/',vista2),
  # path('tres/',vista3,name='vista3')
]
