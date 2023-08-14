from django.shortcuts import render

from catalog.models import Product, Category
def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title':'Товары 3 первых товара'
    }
    return render(request, 'catalog/index.html', context)

def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title':'Категории'
    }
    return render(request, 'catalog/categories.html', context)

def  cart_product(request, pk):
    Product_p= Product.objects.get(pk=pk)
    context = {
        'object': Product_p,
        'title':Product_p.name
    }
    return render(request, 'catalog/product.html',context)

def products(request):
    context = {
        'object_list': Product.objects.all(),
        'title':'Все товары'
    }
    return render(request, 'catalog/products.html',context)



def contacts(request):
    return render(request, 'catalog/contacts.html')

