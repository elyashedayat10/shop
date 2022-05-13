from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'screen_size',
            'cpu_cache',
            'ram',
            'memory_capacity',
            'battery_description',
            'count',

        ]
