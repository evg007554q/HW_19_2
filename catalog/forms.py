from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        exclude = ('owner',)
        # fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        stop_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for sword in stop_word:
            if sword in cleaned_data:
                raise forms.ValidationError(f'Нельзя добавлять это слово - {sword}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        stop_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for sword in stop_word:
            if sword in cleaned_data:
                raise forms.ValidationError(f'Нельзя добавлять это слово - {sword}')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
