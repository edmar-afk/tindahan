from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('add_products', views.add_products, name='add_products')
]