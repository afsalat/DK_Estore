from .models import register
from django.shortcuts import render,redirect
from django.contrib import messages



def registeration(request):

    if request.method == "POST":
        username = request.POST['username']
        email_id = request.POST['email']
        password = request.POST['password']
        # re_password = request.POST['repassword']
        status = "logged"
        customer = register.objects.create(username=username,email_id=email_id,password=password,status=status)
        customer.save()

    
        

    return render(request, 'sign-up_in.html')