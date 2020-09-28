from django.shortcuts import render

# Create your views here.


def viewcart(request):
    return render(request, 'cart/cart.html')   # view to return cart
