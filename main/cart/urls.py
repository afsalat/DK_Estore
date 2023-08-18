from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_list, name="cart"),
    path('<str:uname>', views.log_cart_list, name="log_cart"),
    path('<str:types>/<int:id>/<str:uname>/', views.add_to_cart, name="add_to_cart"),
    path('<int:id>/<str:uname>', views.delete, name="delete"),
    path('<str:uname>/<int:pro_price>/', views.after_count, name="after_name")
]
