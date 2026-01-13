from django.contrib import admin
from .models import Product, Brand, Category, Location

admin.site.site_header = "Shui Inventory Management"
admin.site.site_title = "Shui Inventory Admin"
admin.site.index_title = "Administration"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "category", "brand", "description", "location", "source", "updated_at")
    search_fields = ("name", "sku", "category", "brand", "location", "source")
    autocomplete_fields = ("category", "brand", "location")

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Location)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)