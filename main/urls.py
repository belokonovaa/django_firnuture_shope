from django.urls import path

from main.views import index, about, delivery, information

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('delivery/', delivery, name='delivery'),
    path('information/', information, name='info'),
]
