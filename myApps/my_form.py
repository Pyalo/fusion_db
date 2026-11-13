from django import forms

from myApps.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'category', 'cost', 'price', 'for_sale', 'pic']
