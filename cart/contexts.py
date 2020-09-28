from decimal import Decimal
from django.conf import settings

def cartcontents(request):

    cartitems = []
    total = 0
    productcount = 0

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