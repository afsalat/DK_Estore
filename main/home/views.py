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
    
    if uname:
        vk = uname
    else:
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

def log_featured_detail(request, id, uname):
        
    respo =  featured_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo,'uname':uname})



def leatest_detail(request, id):
        
    respo =  leatest_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo})

def log_leatest_detail(request, id, uname):
        
    respo =  leatest_product.objects.get(id=id)

    return render(request, 'detail.html',{'res':respo,'uname':uname})



def registeration(request):
    
    cat_li = category.objects.all()
        
    featured_p = featured_product.objects.all()
        
    leatest_p = leatest_product.objects.all()
        
    footer_deta = footer_details.objects.all()

    
    try:
        if request.method=='POST':
            if request.POST['email']:
                username = request.POST['username']
                email_id = request.POST['email']
                password = request.POST['password']
                re_password = request.POST['repassword']
                
                if password == re_password:
                    
                    if register.objects.filter(username=username):

                        wr = {
                            'class':'er',
                            'message':' Username already exist try another one !'
                            }
                        
                        return render(request, 'sign-up_in.html', {'wr':wr})
                    

                    elif register.objects.filter(email_id=email_id):
                            wr = {
                                'class':'er',
                                'message':' Email ID already exist try another one !'
                                }
                            
                            return render(request, 'sign-up_in.html', {'wr':wr})


                    else:
                            
                            status = "logged"
                            customer = register.objects.create(username=username,email_id=email_id,password=password,status=status)
                            customer.save()
                            
                            idd = register.objects.filter(username=username)
                
                            for i in idd:
                                id = i.id
                                name=i.username
                                
                            return render(request,'index.html',{
                                'cate':cat_li,
                                'f_pro':featured_p,
                                'l_pro':leatest_p,
                                'lxl':footer_deta,
                                'id':id,
                                'uname':name
                                })
                else:

                    wr = {
                        'class':'er',
                        'message':' Password is not matching !'
                    }

                    return render(request, 'sign-up_in.html', {'wr':wr})

                                

                
    except:
            if request.method=='POST':
                if request.POST['lemail']:
                    email_i_d = request.POST['lemail']
                    password = request.POST['lpassword']
                    
                    if register.objects.filter(email_id=email_i_d) and register.objects.filter(password=password):
                        
                        mr = register.objects.filter(email_id=email_i_d)
                        for i in mr:
                            idd = i.id

                        mer = register.objects.get(id=idd)
                        mer.status = "logged"
                        mer.save()
                        
                        n = register.objects.filter(email_id=email_i_d)
                        
                        for i in n:
                            name = i.username
                    
                        return render(request,'index.html',{
                            'cate':cat_li,
                            'f_pro':featured_p,
                            'l_pro':leatest_p,'lxl':footer_deta,
                            'uname':name
                        })
                
                    else:
                        wr = {
                            'class':'er',
                            'message':' Invalid Email or Password please try again !'
                        }
                        
                        return render(request, 'sign-up_in.html', {'wr':wr})            
        


    return render(request, 'sign-up_in.html')


def re_registration(request, wr):

    cat_li = category.objects.all()
        
    featured_p = featured_product.objects.all()
        
    leatest_p = leatest_product.objects.all()
        
    footer_deta = footer_details.objects.all()

    
    try:
        if request.method=='POST':
            if request.POST['email']:
                username = request.POST['username']
                email_id = request.POST['email']
                password = request.POST['password']
                re_password = request.POST['repassword']

                if password == re_password:
                    
                    if register.objects.filter(username=username):

                        wr = {
                            'class':'er',
                            'message':' Username already exist try another one !'
                            }
                        
                        return render(request, 'sign-up_in.html', {'wr':wr})
                    

                    elif register.objects.filter(email_id=email_id):
                            wr = {
                                'class':'er',
                                'message':' Email ID already exist try another one !'
                                }
                            
                            return render(request, 'sign-up_in.html', {'wr':wr})


                    else:
                            
                            status = "logged"
                            customer = register.objects.create(username=username,email_id=email_id,password=password,status=status)
                            customer.save()
                            
                            idd = register.objects.filter(username=username)
                
                            for i in idd:
                                id = i.id
                                name=i.username
                                
                            return render(request,'index.html',{
                                'cate':cat_li,
                                'f_pro':featured_p,
                                'l_pro':leatest_p,
                                'lxl':footer_deta,
                                'id':id,
                                'uname':name
                                })
                else:

                    wr = {
                        'class':'er',
                        'message':' Password is not matching !'
                    }

                    return render(request, 'sign-up_in.html', {'wr':wr})


                                

                
    except:
            if request.method=='POST':
                if request.POST['lemail']:
                    email_i_d = request.POST['lemail']
                    password = request.POST['lpassword']
                    
                    if register.objects.filter(email_id=email_i_d) and register.objects.filter(password=password):
                        
                        mr = register.objects.filter(email_id=email_i_d)
                        for i in mr:
                            idd = i.id

                        mer = register.objects.get(id=idd)
                        mer.status = "logged"
                        mer.save()
                        
                        n = register.objects.filter(email_id=email_i_d)
                        
                        for i in n:
                            name = i.username
                    
                        return render(request,'index.html',{
                            'cate':cat_li,
                            'f_pro':featured_p,
                            'l_pro':leatest_p,'lxl':footer_deta,
                            'uname':name
                        })
                
                    else:
                        wr = {
                            'class':'er',
                            'message':' Invalid Email or Password please try again !'
                        }
                        
                        return render(request, 'sign-up_in.html', {'wr':wr})

    return render(request, 'sign-up_in.html', {'wr':wr})
