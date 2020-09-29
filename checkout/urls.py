from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkoutsuccess/<order_number>', views.checkoutsuccess, name='checkoutsuccess'),
]