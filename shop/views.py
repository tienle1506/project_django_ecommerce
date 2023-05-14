from django.shortcuts import render
from .models import Category, Product
from cart.forms import CartAddProductForm
# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'products': products, 'categories': categories})

def product_detail(request, id, slug):
    product = Product.objects.get(id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                         'cart_product_form': cart_product_form})
