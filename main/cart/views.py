from django.shortcuts import render


def cart_list(request):
    
    return render(request, 'cart.html')

def log_cart_list(request, uname):
    

    return render(request, 'cart.html',{'uname':uname})