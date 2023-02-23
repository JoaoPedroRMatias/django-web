from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Product 

def index(request):
    produto = Product.objects.all()
    context = {
        'title': 'Bem vindo a loja do Sonic Judeu!',
        'produto': produto,
    }
    return render(request, 'index.html', context) 

def contact(request):
    return render(request, 'contact.html')

def produto(request, pk):
    # prod = Product.objects.get(id=pk)
    prod = get_object_or_404(Product, id=pk)

    context = {
        'produto': prod,
    }

    return render(request, 'produto.html', context)

