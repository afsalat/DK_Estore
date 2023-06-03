from django.urls import path
from . import views

urlpatterns = [

    path('', views.product_list, name="pro_li"),
    path('logged/<int:id>', views.product_list_log, name="pro_li_log"),

    path('pro_detail/<int:id>', views.product_detail, name='pro_detail'),
    path('logged/pro_detail/<int:id>', views.product_detail, name='logged_pro_detail'),

    path('f_detail/<int:id>', views.f_detail, name='f_detail'),
    path('logged/f_detail/<int:id>', views.f_detail, name='logged_f_detail'),

    path('l_detail/<int:id>', views.l_detail, name='l_detail'),
    path('logged/l_detail/<int:id>', views.l_detail, name='logged_l_detail'),

]
