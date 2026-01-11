from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "category", "brand", "short_description", "long_description", "updated_at")
    search_fields = ("name", "sku")