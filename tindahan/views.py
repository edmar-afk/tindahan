from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Products, Orders, Profile
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='user-login')
def homepage(request):
    return render(request, 'homepage.html')



@login_required(login_url='user-login')
def products(request):
    products = Products.objects.all()
    context = {
        'lists' : products
    }
    if request.method == 'POST':
        order_name = request.POST['orderName']
        prices = request.POST['prices']
        room = request.POST['room']
        studName = request.POST['studName']
        status = request.POST['status']
        new_order = Orders(oname=order_name, quantity=prices, location=room, custname_id=studName, status=status)
        new_order.save()
        
        
    return render(request, 'product.html', context)


@login_required(login_url='user-login')
def add_products(request):
    
    if request.method == 'POST':
        pname = request.POST['pname']
        status = request.POST['status']
        foodType = request.POST['foodType']
        productPic = request.FILES['productPic']
        price = request.POST['price']
       
        new_product = Products(name=pname, status=status, type=foodType, pic=productPic, price=price)
        new_product.save()
        
    return render(request, 'add_product.html')



@login_required(login_url='user-login')
def profile(request):
    profile = Profile.objects.all()
    
    context = {
        'profile' : profile
    }
    return render(request, 'profile.html', context)


@login_required(login_url='user-login')
def register(request):
    if request.method == "POST":
        first_name = request.POST['full_name']
        last_name = request.POST['mobile']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(last_name=last_name).exists():
                messages.info(request, 'Mobile Number already taken.')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                profile_obj = Profile.objects.create(user = user )
                profile_obj.save()
    
                return redirect('user-login')
        else:
            messages.info(request, 'Password not match.')
            return redirect('register')
        

    return render(request, 'signup.html')



@login_required(login_url='user-login')
def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password) 
        if user is not None:
            auth.login(request, user)
            return redirect("homepage")
        else:
            messages.info(request, "Invalid USERNAME or PASSWORD")
            return redirect("user-login")
    else:    
        return render(request, 'login.html')
    
    
    
@login_required(login_url='user-login')
def history(request):
    history = Orders.objects.filter(custname=request.user).order_by('-id')
    
    context = {
        'history' : history
    }
    
    return render(request, 'history.html', context)



def status_update(request, status_updateID): 

    status_change = request.POST.get('status')
    
    update_status = Orders.objects.get(id=status_updateID)
    update_status.status = status_change
    update_status.save()
    
    return HttpResponseRedirect(reverse('history'))


def add_profile(request):
    
    if request.method == 'POST':
        pp = request.FILES['profile_p']
      
        new_pp = Profile(profile_pic=pp)
        new_pp.save()
    context = {
        'profile' : profile
    }
    return HttpResponseRedirect(reverse('profile'))



def update_profile(request):
    
    if request.method == 'POST':
        user = request.POST['user']
        created_at = request.POST['created_at']
        pic_change = request.FILES['profile_p']
        
        new_pic = Profile(user=user, created_at=created_at, profile_pic=pic_change )
        new_pic.save()
        
    
    context = {
        'profile' : profile
    }
    return HttpResponseRedirect(reverse('profile'))