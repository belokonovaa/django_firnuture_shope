from django.urls import path

from products.views import catalog, product

app_name = 'products'

urlpatterns = [
    path('', catalog, name='index'),
    path('product/<slug:product_slug>/', product, name='product'),
]