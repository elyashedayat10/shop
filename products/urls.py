from django.urls import path

from .views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductsListAdmin,
    ProductUpdateView,
)

app_name = "products"
urlpatterns = [
    path("list_admin/", ProductsListAdmin, name="list_admin"),
    path("admin/<slug:slug>/", ProductDetailView.as_view(), name="detail_admin"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("update/<slug:slug>/", ProductUpdateView.as_view(), name="update"),
    path("delete/<slug:slug>/", ProductDeleteView.as_view(), name="delete"),
]
