from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View
from django.views.generic.edit import FormMixin
from accounts.mixins import AdminMixin

from .forms import ProductForm, AddToCartForm
from .models import Product


# products admin views
class ProductsListAdmin(AdminMixin, ListView):
    model = Product
    template_name = "products/product_list_panel.html"
    context_object_name = "product_list"


class ProductAdminDetailView(AdminMixin, DetailView):
    model = Product
    template_name = "products/product_detail_panel.html"
    context_object_name = "product"


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
    form_class = ProductForm


class ProductUpdateView(AdminMixin, UpdateView):
    model = Product
    template_name = "products/update.html"
    SuccessMessageMixin = "updated successfully"
    form_class = ProductForm
    context_object_name = "product"

    def get_success_url(self):
        return reverse("products:detail_admin", kwargs={"slug": self.object.slug})


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'product_list'


class ProductDetailView(FormMixin, DetailView):
    model = Product
    template_name = 'products/detail.html'
    form_class = AddToCartForm
