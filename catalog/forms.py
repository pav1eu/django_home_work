from django import forms
from catalog.models import Product
from django.conf import settings

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']

    def clean_name(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get('name')
        for word in settings.BAD_WORDS:
            if word.lower() in name.lower():
                raise forms.ValidationError(f"Имя содержит запрещённое слово: '{word}'")
        return cleaned_data

    def clean_description(self):
        cleaned_data = super().clean()
        description = self.cleaned_data.get('description')
        for word in settings.BAD_WORDS:
            if word.lower() in description.lower():
                raise forms.ValidationError(f"Описание содержит запрещённое слово: '{word}'")
        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price


    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Блаблабла'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })


