from django.urls import path

from products.views import CatalogView, ProductView

app_name = 'products'

urlpatterns = [
    path('search/', CatalogView.as_view(), name='search'),
    path('<slug:category_slug>/', CatalogView.as_view(), name='index'),
    path('product/<slug:product_slug>/', ProductView.as_view(), name='product'),
]