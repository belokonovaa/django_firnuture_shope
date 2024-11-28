from django.urls import path

from main.views import IndexView, AboutView, DeliveryView, InformationView
app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('delivery/', DeliveryView.as_view(), name='delivery'),
    path('information/', InformationView.as_view(), name='info'),
]
