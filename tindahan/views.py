from django.shortcuts import render
from .models import Products
# Create your views here.

def homepage(request):
    products = Products.objects.all()
    
    context = {
        'products' : products
    }
    return render(request, 'base.html', context)


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