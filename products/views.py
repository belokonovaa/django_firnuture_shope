from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from products.models import Product


def catalog(request, category_slug):

    page = request.GET.get('page', 1)

    if category_slug == 'all':
        products = Product.objects.all()
    else:
        products = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Home - Каталог',
        'products': current_page,
        'slug_url': category_slug,
    }

    return render(request, 'products/catalog.html', context)


def product(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product.html', context)
