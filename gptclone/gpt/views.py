from django.shortcuts import render,redirect
from .models import Category, Product

def index(request):
    products = Product.objects.all()
    return render(request, 'gpt/index.html', {'products': products})

def checkout(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    total_price = sum([product.price for product in products])
    return render(request, 'gpt/checkout.html', {'total_price': total_price})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'gpt/product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'gpt/product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'gpt/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'gpt/category_detail.html', {'category': category, 'products': products})

def cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        request.session.setdefault('cart', [])
        request.session['cart'].append(product.id)
        return redirect('gpt:index')
    else:
        cart = request.session.get('cart', [])
        products = Product.objects.filter(id__in=cart)
        return render(request, 'gpt/cart.html', {'products': products})