from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.product.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.tests.views import *
from core.erp.views.client.views import *

app_name='erp'

urlpatterns = [
    #path('uno/',myfirstview,name='vista1'),
    #path('dos/',mysecondview,name='vista2')
    # path('category/list2/',category_list,name='category_list2'),
    path('category/list/',CategoryListView.as_view(),name='category_list'),
    path('category/add/',CategoryCreateView.as_view(),name='category_create'),
    path('category/update/<int:pk>/',CategoryUpdateView.as_view(),name='category_update'),
    path('category/delete/<int:pk>/',CategoryDeleteView.as_view(),name='category_delete'),
    path('category/form/',CategoryFormView.as_view(),name='category_form'),
    #productos
    path('product/list/',ProductListView.as_view(),name='product_list'),
    path('product/add/',ProductCreateView.as_view(),name='product_create'),
    path('product/update/<int:pk>/',ProductUpdateView.as_view(),name='product_update'),
    path('product/delete/<int:pk>/',ProductDeleteView.as_view(),name='product_delete'),
    # client
    path('client/', ClientView.as_view(), name='client'),
    # home
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    # test
    path('test/',TestView.as_view(),name='test')
]
