from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Brand, Category, Product


class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "sku"]
    template_name = "inventory/product_form.html"
    success_url = reverse_lazy("product-list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "sku"]
    template_name = "inventory/product_form.html"
    success_url = reverse_lazy("product-list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "inventory/product_confirm_delete.html"
    success_url = reverse_lazy("product-list")


class BrandCreateView(CreateView):
    model = Brand
    fields = ["name"]
    success_url = reverse_lazy("product-list")


class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]
    success_url = reverse_lazy("product-list")
