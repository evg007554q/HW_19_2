from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version
from catalog.services import get_version_list


def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Товары 3 первых товара'
    }
    return render(request, 'catalog/index.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }


def cart_product(request, pk):
    Product_p = Product.objects.get(pk=pk)
    context = {
        'object': Product_p,
        'title': Product_p.name
    }
    return render(request, 'catalog/product.html', context)


class productListView(ListView):
    model = Product
    extra_context = {
        'title': 'Все товары'
    }


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    extra_context = {
        'title': 'Добавление продукта'
    }
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')
    login_url = 'users:login'

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    extra_context = {
        'title': 'Радактирование продукта'
    }
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if not self.object.owner == self.request.user and not self.request.is_superuser:
            raise PermissionDenied
        return self.object

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


class ProductDetailView( DetailView):
    model = Product
    extra_context = {
        'title': 'Детали продукта'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data['version_set'] = get_version_list(self.object.pk)
        return context_data






