from django.shortcuts import redirect, render
from product_list import models as general
from home import models as home_pro
from cart import models as user



def cart_list(request):
    
    return render(request, 'cart.html')

def log_cart_list(request, uname):

    person = user.cart.objects.filter(person_id=uname)

    if request.method == 'POST':
        ct = request.POST['count']

        for ii in person:
            uid = ii.id

        aa = user.cart.objects.get(id=uid)
        aa.count = ct
        aa.save()

    if person:
        for x in person:
            price = x.pro_price
            count = x.count
            total = price * count
            tt = total

    return render(request, 'cart.html',{'uname':uname, 'pr':person, 'total':tt})


def add_to_cart(request, types, id, uname):

    if general.all_pro_list.objects.filter(pro_type=types):
    
        pro = general.all_pro_list.objects.filter(id=id)
    
    elif home_pro.featured_product.objects.filter(pro_type=types):

        pro = home_pro.featured_product.objects.filter(pro_type=types)

    elif home_pro.leatest_product.objects.filter(pro_type=types):

        pro = home_pro.leatest_product.objects.filter(pro_type=types)

    for i in pro:
        pro_name = i.pro_name
        pro_desc = i.pro_desc
        pro_cate = i.pro_cate
        pro_img = i.pro_img
        pro_sizes = i.pro_sizes
        pro_colors = i.pro_colors
        pro_price = i.pro_price
        pro_stock = i.pro_stock
        
        
    ms =  user.cart.objects.create(
        pro_name=pro_name,
        pro_desc=pro_desc,
        pro_cate=pro_cate,
        pro_img=pro_img,
        pro_sizes=pro_sizes,
        pro_colors=pro_colors,
        pro_price=pro_price,
        pro_stock=pro_stock,
        person_id=uname
        )
    
    ms.save()

    dlt = user.cart.objects.filter(person_id=uname)

    if request.method == 'POST':
        ct = request.POST['count']

        for ii in dlt:
            uid = ii.id

        aa = user.cart.objects.get(id=uid)
        aa.count = ct
        aa.save()

        for x in dlt:
            price = x.pro_price
            count = x.count
            total = price * count

        
    return render(request, 'cart.html',{'uname':uname,'pr':dlt,'total':total})

def delete(request, id, uname):


    if id:
        dlt = user.cart.objects.filter(id=id)
        dlt.delete()
        
        dlt = user.cart.objects.filter(person_id=uname)

    if request.method == 'POST':
        
        ct = request.POST['count']

        for ii in dlt:
            uid = ii.id

        aa = user.cart.objects.get(id=uid)
        aa.count = ct
        aa.save()

        for x in dlt:
            price = x.pro_price
            count = x.count
            total = price * count


    return render(request, 'cart.html',{'uname':uname,'pr':dlt})

