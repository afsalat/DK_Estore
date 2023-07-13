from django.urls import path
from . import views

urlpatterns = [
    path('',views.billing),
    path('<str:uname>', views.log_billing)

]
