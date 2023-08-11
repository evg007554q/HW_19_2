from django.contrib import admin

from catalog.models import Product, Category

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price')
    list_filter =  ('category',)
    search_fields = ('name','description')

@admin.register(Category)
class ProductCategory(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name','description')