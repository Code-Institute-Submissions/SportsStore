from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your Cart is Empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HWm7zIK2eXI7ATXGsk3QPPOcxeiWh0cxdEtDsRGjrjRm4tAuCdUJzMxgnhe55Mgnlf4spNTtYNfNwu4fhyarHXs00eVnXcqwE',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
