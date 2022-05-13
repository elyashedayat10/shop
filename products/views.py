from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from accounts.mixins import AdminMixin

from .models import Product


# products admin views
class ProductsListAdmin(AdminMixin, ListView):
    model = Product
    template_name = "products/product_list_panel.html"
    context_object_name = 'product_list'


class ProductDetailView(AdminMixin, DetailView):
    model = Product
    template_name = "products/product_detail_panel.html"
    context_object_name = 'product'


class ProductDeleteView(AdminMixin, View):
    def get(self, request, slug):
        product_obj = get_object_or_404(Product, slug=slug)
        product_obj.delete()
        messages.success(request, "", "success")
        return redirect("products:list_admin")


class ProductCreateView(AdminMixin, SuccessMessageMixin, CreateView):
    model = Product
    success_url = reverse_lazy("products:list_admin")
    template_name = "products/create.html"
    SuccessMessageMixin = "created successfully"


class ProductUpdateView(AdminMixin, UpdateView):
    model = Product
    template_name = "products/update.html"
    SuccessMessageMixin = "updated successfully"

    def get_success_url(self):
        return reverse("products:detail_admin", args=[self.kwargs.get("slug")])
