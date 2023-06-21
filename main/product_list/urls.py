from django.urls import path
from . import views

urlpatterns = [

    # main common 
    path('', views.product_list, name="pro_li"),
    path('<str:uname>', views.product_list_log, name="pro_li_log"),
    # path('logged/more_products/<str:uname>', views.product_list_log, name="pro_li_log"),

    # unknowning users
    path('pro_detail/<int:id>', views.product_detail, name='pro_detail'),
    path('f_detail/<int:id>', views.f_detail, name='logged_f_detail'),
    path('l_detail/<int:id>', views.l_detail, name='logged_l_detail'),

    # sign-up or sign-in users
    path('log_pro_detail/<int:id><str:uname>', views.log_product_detail, name='logged_pro_detail'),
    path('log_f_detail/<int:id><str:uname>', views.log_f_detail, name='f_detail'),
    path('log_l_detail/<int:id><str:uname>', views.log_l_detail, name='l_detail'),

]
