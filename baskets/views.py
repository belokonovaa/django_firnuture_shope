from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

from baskets.models import Basket
from products.models import Product


def basket_add(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user, product=product)

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])


def basket_change(request, product_slug):
    ...


def basket_delete(request, basket_id):

    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(reverse('user:users_basket'))
