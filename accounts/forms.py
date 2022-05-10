from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.validators import ValidationError
from .models import User


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("phone_number",)

    def clean(self):
        clean_data = super(UserCreateForm, self).clean()
        password = clean_data['password']
        password_confirm = clean_data['password_confirm']
        if (password and password_confirm) and (password_confirm != password_confirm):
            raise ValidationError('unmatched password')
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you can change password using <a href=\"../password/\">this form</a>.")

    class Meta:
        model = User
        fields = (
            'phone_number',
            'password',
        )


class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("phone_number",)


class AuthForm(AdminForm):
    class Meta:
        model = User
        fields = ('phone_number',)

    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields.pop('password')
        self.fields.pop('password_confirm')


class OtpCodeForm(forms.Form):
    code = forms.CharField(max_length=6)
