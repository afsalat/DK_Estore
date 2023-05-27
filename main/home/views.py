from django.shortcuts import render
from .models import category, featured_product, leatest_product, footer_details

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
        'lxl':footer_detail
        })

def featured_detail(request, id):
        
    respo =  featured_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})

def leatest_detail(request, id):
        
    respo =  leatest_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})
