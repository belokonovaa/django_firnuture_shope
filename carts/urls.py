from django.urls import path

from carts.views import cart_add, cart_change, cart_delete

app_name = 'carts'

urlpatterns = [
    path('cart_add/', cart_add, name='cart_add'),
    path('cart_change/', cart_change, name='cart_change'),
    path('cart_delete/', cart_delete, name='cart_delete'),
]
