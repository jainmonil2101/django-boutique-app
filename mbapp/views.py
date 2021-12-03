from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    search = request.GET.get('search') or ''
    products = Product.objects.filter(name__icontains=search).order_by('-sale')
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    params = {
        'products': page_obj,
    }
    return render(request, 'index.html', params)

def single_product(request, product_id):
    one_product = get_object_or_404(Product, id=product_id)
    params = {
        'one_product':one_product,
    }
    return render(request, 'shop-details.html', params)