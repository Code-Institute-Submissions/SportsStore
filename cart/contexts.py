from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cartcontents(request):

    cartitems = []
    total = 0
    productcount = 0
    cart = request.session.get('cart', {})


    for item_id, quantity in cart.items():
        product = get_object_or_404 (Product, pk=item_id)
        total += quantity * product.price
        productcount += quantity
        cartitems.append ({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREEDELIVERY:
        delivery = total * Decimal(settings.STANDARDDELIVERY / 100)
        free_delivery_delta = settings.FREEDELIVERY - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'cartitems': cartitems,
        'total': total,
        'productcount': productcount,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'freedelivery': settings.FREEDELIVERY,
        'grand_total': grand_total,
    }

    return context