from django.urls import path
from core.erp.views.category.views import *

app_name='erp'

urlpatterns = [
    #path('uno/',myfirstview,name='vista1'),
    #path('dos/',mysecondview,name='vista2')
    path('category/list/',CategoryListView.as_view(),name='category_list'),
    path('category/list2/',category_list,name='category_list2')
]
