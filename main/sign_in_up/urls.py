from django.urls import path
from . import views

urlpatterns = [
    path('',views.registeration,name="sign-up")
]
