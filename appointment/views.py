from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def viewappointment(request):
    return render(request, 'appointment/appointment.html')   # view to return appointment

