from django.db import models

from config import settings


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование продукта')
    description = models.CharField(max_length=250, verbose_name='описание продукта', null=True, blank=True)
    image = models.ImageField(upload_to='image_Product/', verbose_name='изображение', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория', null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='цена', null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', null=True, blank=True)
    last_modified_date = models.DateTimeField(auto_now_add=True, verbose_name='дата последнего изменения', null=True,
                                              blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Создатель')

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование категории')
    description = models.CharField(max_length=250, verbose_name='описание категории', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    version_number = models.CharField(max_length=10, verbose_name='номер версии')
    name = models.CharField(max_length=100, verbose_name='наименование версии')

    сurrent_version = models.BooleanField(default=False, verbose_name='признак текущей версии')


    def __str__(self):
        return f'{self.name} ({self.version_number})'
    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('name',)
