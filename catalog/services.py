from django.conf import settings
from django.core.cache import cache

from catalog.models import Category, Version


def get_version_list(product_pk):
    if settings.CACHES_ENABLE:
        key = f'version_list_{product_pk}'
        version_list = cache.get(key)
        if version_list is None:
            version_list = Version.objects.filter(product__pk=product_pk)
            cache.set(key, version_list)

    else:
        version_list = Version.objects.filter(product__pk=product_pk)

    return version_list

def get_categories():
    if settings.CACHES_ENABLE:
        key = 'CategoryCACHES'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = Category.objects.all()
            cache.set(key, cache_data)

        return cache_data
    else:
        categories = Category.objects.all()

    return categories