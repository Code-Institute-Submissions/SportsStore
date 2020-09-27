from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def allproducts(request):

    products = Product.objects.all()
    query = None


    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(requests, "You have not entered a valid search")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
        'search': query,
    }

    return render(request, 'products/products.html', context)   # view to return products page including sorts&search queries



def productdetail(request, product_id):

    product = get_object_or_404( Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/productdetail.html', context)   # view to return individual products