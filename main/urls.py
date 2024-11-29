from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import IndexView, AboutView, DeliveryView, InformationView
app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', cache_page(60 * 5)(AboutView.as_view()), name='about'),
    path('delivery/', cache_page(60 * 5)(DeliveryView.as_view()), name='delivery'),
    path('information/', cache_page(60 * 5)(InformationView.as_view()), name='info'),
]
