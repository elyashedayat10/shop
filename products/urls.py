from django.urls import path

from .views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductsListAdmin,
    ProductUpdateView,
    ProductListView,
    ProductAdminDetailView,
)

app_name = "products"
urlpatterns = [
    path("list_admin/", ProductsListAdmin.as_view(), name="list_admin"),
    path("list/", ProductListView.as_view(), name="list"),
    path("admin/<slug:slug>/", ProductAdminDetailView.as_view(), name="detail_admin"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("update/<slug:slug>/", ProductUpdateView.as_view(), name="update"),
    path("delete/<slug:slug>/", ProductDeleteView.as_view(), name="delete"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),

]
