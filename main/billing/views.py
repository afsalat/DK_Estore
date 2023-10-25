from django.shortcuts import render
from cart import models as  user
from home import models as glo_user
from .models import order_list


def billing(request):
    
    return render(request, 'checkout.html')


def log_billing(request, uname, st, count, t):

    
    
    if request.method == "POST":
        
        first_name = request.POST['fistname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        addr_1 = request.POST['addr1']
        addr_2 =  request.POST['addr2']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        pin = request.POST['pin']
        payment_method = request.POST['payment']


        if payment_method == 'b' :
            
            order_details = order_list.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                addr_1=addr_1,
                addr_2=addr_2,
                country=country,
                state=state,
                city=city,
                pin=pin
            )

            order_details.save()


            return render(request, 'congratulation.html')
        

        # please set g-pay

        # please set bank







    if uname:
        
        person = glo_user.register.objects.filter(username=uname)
        product = user.cart.objects.filter(person_id=uname)

        for dt in person:
            data = {
                'a1':dt.username,
                'a2':dt.email_id
            }

    else:
        person = " "




    return render(request, 'checkout.html', {'uname':uname,
                                             'p_d':person,
                                             'p':data,
                                             'product':product,
                                             'pr':count,
                                             'st':st,
                                             't':t
                                             })



def after_submit_log_billing(request, uname):



    return render(request, 'congratulation.html', {'uname':uname})
