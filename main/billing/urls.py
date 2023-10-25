from django.urls import path
from . import views

urlpatterns = [
    path('',views.billing),
    path('<str:uname>/<int:st>/<int:count>/<int:t>/', views.log_billing),
    path('<str:uname>/', views.after_submit_log_billing)

]
