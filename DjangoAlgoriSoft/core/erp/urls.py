from django.urls import path
from core.erp.views import *

app_name='erp'

urlpatterns = [
    path('uno/',myfirstview,name='vista1'),
    path('dos/',mysecondview,name='vista2')
]
