from django.urls import path
from . import views

urlpatterns = [
    path('',views.entry ,name='home'),
    path('featured_detail/<int:id>', views.featured_detail, name='featured_detail'),
    path('leatest_detail/<int:id>', views.leatest_detail, name='leatest_detail'),

]
