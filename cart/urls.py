from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewcart, name='viewcart'),
    path('add/<item_id>/', views.addtocart, name='addtocart'),
    path('remove', views.removefromcart, name='removefromcart'),
]