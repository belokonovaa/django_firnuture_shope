from django.http import JsonResponse
from django.template.loader import render_to_string

from baskets.models import Basket
from baskets.utils import get_user_baskets

from products.models import Product


def basket_add(request):

    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user, product=product)

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)

    user_basket = get_user_baskets(request)

    basket_items_html = render_to_string(
        'baskets/includes/included_basket.html', {'baskets': user_basket}, request=request)

    response_data = {
        'message': 'Товар добавлен в корзину',
        'cart_items_html': basket_items_html,
    }
    return JsonResponse(response_data)


def basket_change(request, product_slug):
    ...


def basket_delete(request):

    basket_id = request.POST.get('cart_id')
    basket = Basket.objects.get(id=basket_id)
    quantity = basket.quantity
    basket.delete()

    user_basket = get_user_baskets(request)

    basket_items_html = render_to_string(
        'baskets/includes/included_basket.html', {'baskets': user_basket}, request=request)

    response_data = {
        'message': 'Товар удален из корзины',
        'cart_items_html': basket_items_html,
        'quantity_deleted': quantity,
    }

    return JsonResponse(response_data)
