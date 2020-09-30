from django.shortcuts import render

# Create your views here.

def viewabout(request):
    return render(request, 'about/about.html')   # view to return about
