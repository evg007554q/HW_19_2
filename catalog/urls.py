from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, CategoryListView, productListView, cart_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('admin/', admin.site.urls),
    path('products/', productListView.as_view(), name='products'),
    path('<int:pk>/product/', cart_product, name='cart_product'),
]
  # + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
