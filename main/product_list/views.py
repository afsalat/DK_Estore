from django.shortcuts import render
from home import models as mo
from .models import all_pro_list

# Create your views here.

def product_list(request):
    
    all_pro = all_pro_list.objects.all()

    f_pro = mo.featured_product.objects.all()
    l_pro = mo.leatest_product.objects.all()

    return render(request, 'product_list.html', {'tt1':f_pro,'tt2':l_pro,'ap':all_pro})