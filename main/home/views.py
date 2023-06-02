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


def entry_auth(request, id):

    cat_list = category.objects.all()

    featured_pro = featured_product.objects.all()

    leatest_pro = leatest_product.objects.all()

    footer_detail = footer_details.objects.all()

    # if id:
    #     vk = register.objects.get(id=id)

 
    return render(request, 'index.html',{
        'cate':cat_list,
        'f_pro':featured_pro,
        'l_pro':leatest_pro,
        'lxl':footer_detail,
        # 'acn':acc_name,
        })



def featured_detail(request, id):
        
    respo =  featured_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})



def leatest_detail(request, id):
        
    respo =  leatest_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})



def registeration(request):

    if request.method == "POST":
        user_name = request.POST['username']
        email__id = request.POST['email']
        pass_word = request.POST['password']
        # re_password = request.POST['repassword']
        statuss = "logged"
        customer = register.objects.create(username=user_name,email_id=email__id,password=pass_word,status=statuss)
        customer.save()

        idd = register.objects.filter(username=user_name)
        
        cat_list = category.objects.all()
        
        featured_pro = featured_product.objects.all()
        
        leatest_pro = leatest_product.objects.all()
        
        footer_detail = footer_details.objects.all()

        return render(request,'index.html',{
            'cate':cat_list,
            'f_pro':featured_pro,
            'l_pro':leatest_pro,
            'lxl':footer_detail,
            'id':idd,
            })

        
    return render(request, 'sign-up_in.html')
