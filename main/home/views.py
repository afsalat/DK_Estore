from django.shortcuts import render
from .models import category

# Create your views here.

def entry(request):

    cat_list = category.objects.all()
    
    return render(request, 'index.html',{'cate':cat_list})
