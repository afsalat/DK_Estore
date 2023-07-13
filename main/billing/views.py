from django.shortcuts import render

def billing(request):
    
    return render(request, 'checkout.html')


def log_billing(request, uname):


    return render(request, 'checkout.html', {'uname':uname})
