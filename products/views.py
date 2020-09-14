from django.shortcuts import render
from .models import Product

# Create your views here.


def allproducts(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)   # view to return products page including sorts&search queries