from django.shortcuts import render
from home import models as mo

# Create your views here.

def product_list(request):

    f_pro = mo.featured_product.objects.all()
    l_pro = mo.leatest_product.objects.all()

    t_pro = f_pro , l_pro

    return render(request, 'product_list.html', {'tt':t_pro})