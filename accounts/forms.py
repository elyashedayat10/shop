from django import forms

from .models import User


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("phone_number",)


class OtpCodeForm(forms.Form):
    code = forms.CharField(max_length=6)
