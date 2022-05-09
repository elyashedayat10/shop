from django import forms
from django.shortcuts import render

from .models import Profile


# Create your views here.
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'full_name',
            'email',
            'image',
            'card_number',
            'national_code',
            'receive_blog',
        )

        labels = {
            'full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'image': 'تصویر پروفایل',
            'card_number': 'شماره کارت',
            'national_code': 'شماره ملی',
            'receive_blog': 'دربافت خبرنامه',
        }
