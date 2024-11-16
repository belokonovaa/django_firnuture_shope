from django.shortcuts import render

from products.models import Product


def catalog(request):

    products = Product.objects.all()

    context = {
        'title': 'Home - Каталог',
        'products': products,
    }

    return render(request, 'products/catalog.html', context)


def product(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product.html', context)
