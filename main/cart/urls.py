from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_list, name="cart"),
    path('<str:uname>', views.log_cart_list, name="log_cart"),
]
