from django.urls import path

from .views import (BrandCreateView, BrandDeleteView, BrandListView,
                    BrandUpdateView)

app_name = "brands"
urlpatterns = [
    path("list/", BrandListView.as_view(), name="list"),
    path("create/", BrandCreateView.as_view(), name="create"),
    path("update/<slug:slug>/", BrandUpdateView.as_view(), name="update"),
    path("delete/<slug:slug>/", BrandDeleteView.as_view(), name="delete"),
]
