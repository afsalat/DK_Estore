from django.shortcuts import render
from cart import models as  user


def billing(request):
    
    return render(request, 'checkout.html')


def log_billing(request, uname):
    
    if request.method == "POST":
        
        first_name = request.POST['firstname']
        last_name = request.POST['lastname ']
        email = request.POST['email']
        phone = request.POST['phone']
        addr_1 = request.POST['addr1']
        addr_2 =  request.POST['addr2']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        pin = request.POST['pin']

        person = user.cart.objects.get(person_id=uname)




    return render(request, 'checkout.html', {'uname':uname})
