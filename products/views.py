from django.shortcuts import render, get_object_or_404

from products.models import Product


def catalog(request, category_slug):

    if category_slug == 'all':
        products = Product.objects.all()
    else:
        products = get_object_or_404(Product.objects.filter(category__slug=category_slug))

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
