from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "screen_size",
            "cpu_cache",
            "ram",
            "memory_capacity",
            "battery_description",
            "count",
            "image",
            "price",
        ]


class AddToCartForm(forms.Form):
    count = forms.IntegerField(min_value=1)
