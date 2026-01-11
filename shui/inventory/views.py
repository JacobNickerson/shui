from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product, Brand, Category

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
    #template_name = "inventory/brand_form.html"

class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]
    success_url = reverse_lazy("product-list")

# TODO: Update views