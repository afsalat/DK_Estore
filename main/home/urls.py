from django.urls import path
from . import views

urlpatterns = [

    path('', views.entry , name='home'),
    path('featured_detail/<int:id>', views.featured_detail, name='featured_detail'),
    path('leatest_detail/<int:id>', views.leatest_detail, name='leatest_detail'),

    path('logged/<str:uname>', views.entry_auth , name='_home'),
    path('logged/log_featured_detail/<int:id><str:uname>', views.log_featured_detail, name='logged_featured_detail'),
    path('logged/log_leatest_detail/<int:id><str:uname>', views.log_leatest_detail, name='logged_leatest_detail'),

    path('logged/', views.registeration, name="logged"),
    path('re-log/<str:wr>', views.re_registration, name="log_error"),

]
