from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def viewcart(request):
    return render(request, 'cart/cart.html')   # view to return cart


def addtocart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get ('redirect_url')
    cart = request.session.get('cart', {})
    
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect (redirect_url)



def removefromcart(request, item_id):

    cart = request.session.get('cart', {})

    cart.pop(item_id)

    request.session['cart'] = cart
    return HttpResponse(status=200)