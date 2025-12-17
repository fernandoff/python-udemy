from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

def products_list(request):
    products = Product.objects.all().order_by('created_at')
    return render(request, 'products/products_list.html', {'products':products})

def product_page(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'products/product_page.html', {'product':product})

@login_required(login_url='/users/login')
def product_new(request):
    return render(request, 'products/product_new.html')