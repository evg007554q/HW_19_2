
from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product, Category
def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title':'Товары 3 первых товара'
    }
    return render(request, 'catalog/index.html', context)

# def categories(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title':'Категории'
#     }
#     return render(request, 'catalog/category_list.html', context)

class CategoryListView(ListView):
    model = Category
    extra_context = {
         'title':'Категории'
    }



def  cart_product(request, pk):
    Product_p= Product.objects.get(pk=pk)
    context = {
        'object': Product_p,
        'title':Product_p.name
    }
    return render(request, 'catalog/product.html',context)

# def products(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title':'Все товары'
#     }
#     return render(request, 'catalog/products.html',context)

class productListView(ListView):
    model = Product
    extra_context = {
        'title': 'Все товары'
    }
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(category_id=self.kwargs.get('pk') )
    #     return queryset
    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #
    #     category_item = Category.objects.get(pk=self.kwargs.get('pk'))
    #     context_data['category_pk'] = category_item.pk,
    #     context_data['title'] = f'Продукты категории {category_item.name}',
    #
    #     return context_data

def contacts(request):
    return render(request, 'catalog/contacts.html')

