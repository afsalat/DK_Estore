from django.shortcuts import render
from .models import category,featured_product,leatest_product

# Create your views here.

def entry(request):

    cat_list = category.objects.all()

    featured_pro = featured_product.objects.all()

    leatest_pro = leatest_product.objects.all()
    
    return render(request, 'index.html',{'cate':cat_list,'f_pro':featured_pro,'l_pro':leatest_pro})
