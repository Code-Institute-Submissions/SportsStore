from django.shortcuts import render, redirect, HttpResponse
import logging

# Create your views here.
logger = logging.getLogger(__name__)


def viewcart(request):
    return render(request, 'cart/cart.html')   # view to return cart


def addtocart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def removefromcart(request):

    item_id = request.POST.get('product_id')

    cart = request.session.get('cart', {})

    del cart[item_id]

    request.session['cart'] = cart
    return redirect('viewcart')