from django import forms

from .models import User


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("phone_number",)
