from django.shortcuts import redirect, render, HttpResponse
from .models import category, featured_product, leatest_product, footer_details,register

# Create your views here.

def entry(request):

    cat_list = category.objects.all()

    featured_pro = featured_product.objects.all()

    leatest_pro = leatest_product.objects.all()

    footer_detail = footer_details.objects.all()

    
    return render(request, 'index.html',{
        'cate':cat_list,
        'f_pro':featured_pro,
        'l_pro':leatest_pro,
        'lxl':footer_detail,
        })


def entry_auth(request, uname):

    cat_list = category.objects.all()

    featured_pro = featured_product.objects.all()

    leatest_pro = leatest_product.objects.all()

    footer_detail = footer_details.objects.all()

    vk = register.objects.filter(username=uname)

 
    return render(request, 'index.html',{
        'cate':cat_list,
        'f_pro':featured_pro,
        'l_pro':leatest_pro,
        'lxl':footer_detail,
        'uname':vk,
        })



def featured_detail(request, id):
        
    respo =  featured_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})



def leatest_detail(request, id):
        
    respo =  leatest_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})



def registeration(request):

    if request.method == "POST":
        username = request.POST['username']
        email_id = request.POST['email']
        password = request.POST['password']
        # re_password = request.POST['repassword']
        status = "logged"
        customer = register.objects.create(username=username,email_id=email_id,password=password,status=status)
        customer.save()

        idd = register.objects.filter(username=username)

        for i in idd:
            id=i.id
            name=i.username
        
        cat_list = category.objects.all()
        
        featured_pro = featured_product.objects.all()
        
        leatest_pro = leatest_product.objects.all()
        
        footer_detail = footer_details.objects.all()

        return render(request,'index.html',{
            'cate':cat_list,
            'f_pro':featured_pro,
            'l_pro':leatest_pro,
            'lxl':footer_detail,
            'id':id,
            'uname':name,
            })

        
    return render(request, 'sign-up_in.html')
