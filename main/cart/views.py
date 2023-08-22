from django.shortcuts import redirect, render
from product_list import models as general
from home import models as home_pro
from cart import models as user




def cart_list(request):
    
    return render(request, 'cart.html')


def log_cart_list(request, uname):

    items = user.cart.objects.filter(person_id=uname)
    


    return render(request, 'cart.html',{'uname':uname, 'pr':items})


def after_count(request, uname, pro_price):
        
    items = user.cart.objects.filter(person_id=uname)

        
    if request.method == 'POST':
        ct = request.POST['count']
        

        aa = user.cart.objects.get(pro_price=pro_price)
        aa.count = ct
        aa.save()


    return render(request, 'cart.html',{'uname':uname, 'pr':items})


def add_to_cart(request, types, id, uname):

# problem is : the addtional product add at the time change the already added product countity
# created a new data field

    if  user.cart.objects.filter(pro_type=types):

        aa = user.cart.objects.get(sec_id=id)
        aa.count = aa.count+1
        aa.save()




    else:

        if general.all_pro_list.objects.filter(pro_type=types):
        
            pro = general.all_pro_list.objects.filter(id=id)
        
        elif home_pro.featured_product.objects.filter(pro_type=types):

            pro = home_pro.featured_product.objects.filter(id=id)
            
        elif home_pro.leatest_product.objects.filter(pro_type=types):

            pro = home_pro.leatest_product.objects.filter(id=id)

        for i in pro:
            pro_name = i.pro_name
            pro_desc = i.pro_desc
            pro_cate = i.pro_cate
            pro_img = i.pro_img
            pro_sizes = i.pro_sizes
            pro_colors = i.pro_colors
            pro_price = i.pro_price
            pro_stock = i.pro_stock
            pro_type = i.pro_type
            
            
        ms =  user.cart.objects.create(
            pro_name=pro_name,
            pro_desc=pro_desc,
            pro_cate=pro_cate,
            pro_img=pro_img,
            pro_sizes=pro_sizes,
            pro_colors=pro_colors,
            pro_price=pro_price,
            pro_stock=pro_stock,
            person_id=uname,
            pro_type=pro_type,
            sec_id = id

            )
        
        ms.save()



    items = user.cart.objects.filter(person_id=uname)

    if request.method == 'POST':
        ct = request.POST['count']

        for ii in items:
            uid = ii.id

        aa = user.cart.objects.get(id=uid)
        aa.count = ct
        aa.save()

        
    return render(request, 'cart.html',{'uname':uname,'pr':items})

def delete(request, id, uname):


    if id:
        items = user.cart.objects.filter(id=id)
        items.delete()
        
        items = user.cart.objects.filter(person_id=uname)

    if request.method == 'POST':
        
        ct = request.POST['count']

        for ii in items:
            uid = ii.id

        aa = user.cart.objects.get(id=uid)
        aa.count = ct
        aa.save()


    return render(request, 'cart.html',{'uname':uname,'pr':items})

