from django.urls import path

from products.views import catalog, product

app_name = 'products'

urlpatterns = [
    path('search/', catalog, name='search'),
    path('<slug:category_slug>/', catalog, name='index'),
    path('product/<slug:product_slug>/', product, name='product'),
]