from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('home', views.home, name='home'),
    path('checkout', views.checkout, name='Checkout'),
]