from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry , name='home'),
    path('logged/<str:uname>', views.entry_auth , name='_home'),
    path('featured_detail/<int:id>', views.featured_detail, name='featured_detail'),
    path('leatest_detail/<int:id>', views.leatest_detail, name='leatest_detail'),
    path('logged/', views.registeration, name="logged"),
    path('logged/featured_detail/<int:id>', views.featured_detail, name='logged_featured_detail'),
    path('logged/leatest_detail/<int:id>', views.leatest_detail, name='logged_leatest_detail'),
    # path('logged/sign-up_in/', views.registeration, name="logged_sign-up"),
]
