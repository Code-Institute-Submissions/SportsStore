from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allproducts, name='products'),
    path('<product_id>', views.productdetail, name='productdetail'),
]
