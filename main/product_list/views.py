from django.shortcuts import render
from home import models as pro
from cart import models as user
from .models import all_pro_list

# Create your views here.

def product_list(request):
    
    all_pro = all_pro_list.objects.all()

    f_pro = pro.featured_product.objects.all()
    l_pro = pro.leatest_product.objects.all()


    return render(request, 'product_list.html', {'t_1':f_pro,'t_2':l_pro,'t_3':all_pro})


def product_list_log(request, uname):
    
    all_pro = all_pro_list.objects.all()

    f_pro = pro.featured_product.objects.all()
    l_pro = pro.leatest_product.objects.all()

    id_ = pro.register.objects.filter(username=uname)
    for i in id_:
        uname = i.username


    return render(request, 'product_list.html', {'t_1':f_pro,'t_2':l_pro,'t_3':all_pro,'uname':uname})


# ------------------------------


def product_detail(request, id):

    respo =  all_pro_list.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})


def log_product_detail(request, id, uname):

    respo =  all_pro_list.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo,'id':id,'uname':uname})


def add_to_cart(request, id, uname):

    try:

        pro = all_pro_list.objects.filter(id=id)


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

        
    except:
        print("GGGGGGGGGGGGGGGGGGGGGGG")
        
    return render(request, 'cart.html',{'id':id,'uname':uname})
# ------------------------------


def f_detail(request, id):

    respo = pro.featured_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})


def log_f_detail(request, id, uname):

    respo = pro.featured_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo,'uname':uname})


# ------------------------------


def l_detail(request, id):

    respo =  pro.leatest_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})


def log_l_detail(request, id, uname):

    respo =  pro.leatest_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo,'uname':uname})