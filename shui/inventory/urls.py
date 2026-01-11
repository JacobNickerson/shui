from django.contrib import admin
from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    BrandCreateView,
    CategoryCreateView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("add/", ProductCreateView.as_view(), name="product-add"),
    # path("<int:pk>/edit/", ProductUpdateView.as_view(), name="product-edit"),
    # path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
    # path("brands/add/", BrandCreateView.as_view(), name="brand-add"),
    # path("categories/add/", CategoryCreateView.as_view(), name="category-add"),
]