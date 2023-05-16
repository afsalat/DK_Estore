from django.shortcuts import render

# Create your views here.

def entry(request):
    
    return render(request, 'index.html')