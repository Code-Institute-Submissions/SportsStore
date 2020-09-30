from django.shortcuts import render

# Create your views here.

def viewappointment(request):
    return render(request, 'appointment/appointment.html')   # view to return appointment