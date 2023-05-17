from django.shortcuts import render
from .models import category,product

# Create your views here.

def entry(request):

    cat_list = category.objects.all()

    pro_list = product.objects.all()
    
    return render(request, 'index.html',{'cate':cat_list,'pro':pro_list})
