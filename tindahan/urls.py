from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('products', views.products, name='products'),
    path('add_products', views.add_products, name='add_products'),
    path('profile', views.profile, name='profile'),
    path('user-login', views.login_user, name='user-login'),
    path('register', views.register, name='register'),
    path('history', views.history, name='history'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('<int:status_updateID>/statuschange/', views.status_update, name='statuschange'),
    path('profilepic', views.update_profile, name='profilepic'),
]