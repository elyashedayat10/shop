from braces.views import StaffuserRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View

from .models import Brand


# Create your views here.
class BrandListView(StaffuserRequiredMixin, ListView):
    model = Brand
    template_name = "brands/list.html"
    context_object_name = "brand_list"


class BrandCreateView(StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    model = Brand
    fields = ("name", "image")
    success_url = reverse_lazy("brands:list")
    success_message = "brand created successfully"
    template_name = "brands/create.html"


class BrandUpdateView(StaffuserRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Brand
    fields = ("name", "image")
    success_url = reverse_lazy("brands:list")
    success_message = "brand updated successfully"
    template_name = "brands/update.html"


class BrandDeleteView(StaffuserRequiredMixin, View):
    def get(self, *args, **kwargs):
        brand = get_object_or_404(Brand, slug=kwargs.get("slug"))
        brand.delete()
        messages.success(self.request, "brand deleted successfully", "success")
        return redirect("brands:list")
