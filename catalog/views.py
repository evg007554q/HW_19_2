from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version


def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title':'Товары 3 первых товара'
    }
    return render(request, 'catalog/index.html', context)



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

class productListView(ListView):
    model = Product
    extra_context = {
        'title': 'Все товары'
    }

def contacts(request):
    return render(request, 'catalog/contacts.html')

class ProductCreateView(CreateView):
    model = Product
    extra_context = {
        'title': 'Добавление продукта'
    }
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    model = Product
    extra_context = {
        'title': 'Радактирование продукта'
    }
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')
    # def det_success_url(self):
    #     return reverse('product:product_update', args=[self.kwargs.get('pk')] )
    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        # context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        # context_data =
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)