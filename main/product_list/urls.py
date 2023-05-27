from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list),
    path('pro_detail/<int:id>', views.product_detail, name='pro_detail'),
    path('f_detail/<int:id>', views.f_detail, name='f_detail'),
    path('l_detail/<int:id>', views.l_detail, name='l_detail'),


]
