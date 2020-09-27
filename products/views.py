from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def allproducts(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)   # view to return products page including sorts&search queries



def productdetail(request, product_id):

    product = get_object_or_404( Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/productdetail.html', context)   # view to return individual products