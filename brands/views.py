from django.shortcuts import redirect, get_object_or_404
from .models import Brand
from django.views.generic import ListView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from braces.views import StaffuserRequiredMixin
from django.contrib import messages


# Create your views here.
class BrandListView(StaffuserRequiredMixin, ListView):
    model = Brand
    template_name = 'brands/list.html'
    context_object_name = 'brand_list'


class BrandCreateView(StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    model = Brand
    fields = ('name', 'image')
    success_url = reverse_lazy('brands:list')
    success_message = 'brand created successfully'
    template_name = 'brands/create.html'


class BrandUpdateView(StaffuserRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Brand
    fields = ('name', 'image')
    success_url = reverse_lazy('brands:list')
    success_message = 'brand updated successfully'
    template_name = 'brands/update.html'


class BrandDeleteView(StaffuserRequiredMixin, View):
    def get(self, *args, **kwargs):
        brand = get_object_or_404(Brand, slug=kwargs.get('slug'))
        brand.delete()
        messages.success(self.request, 'brand deleted successfully', 'success')
        return redirect('brands:list')
