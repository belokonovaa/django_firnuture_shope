from django.urls import path

from baskets.views import basket_add, basket_change, basket_delete

app_name = 'baskets'

urlpatterns = [
    path('basket_add/', basket_add, name='basket_add'),
    path('basket_change/', basket_change, name='basket_change'),
    path('basket_delete/', basket_delete, name='basket_delete'),
]
