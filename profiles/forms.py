from django import forms
from django.shortcuts import render

from .models import Profile


# Create your views here.
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "full_name",
            "email",
            "image",
            "receive_blog",
        )
