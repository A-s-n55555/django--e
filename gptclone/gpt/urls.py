# gpt/urls.py

from django.urls import path
from . import views

app_name = 'gpt'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list, name='product_list'),
    path('category_list/', views.category_list, name='category_list'),
    path('category_detail/<int:pk>/', views.category_detail, name='category_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
