from django.contrib import admin
from django.utils.html import format_html

from .models import Brand, Category, Location, Product

admin.site.site_header = "Shui Inventory Management"
admin.site.site_title = "Shui Inventory Admin"
admin.site.index_title = "Administration"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "image_thumbnail",
        "name",
        "sku",
        "category",
        "brand",
        "description",
        "qty",
        "location",
        "source",
        "updated_at",
    )
    search_fields = ("name", "sku", "category__name", "brand__name", "location", "source")
    autocomplete_fields = ("category", "brand")
    readonly_fields = ("image_preview",)
    fields = (
        "name",
        "sku",
        "image",
        "image_preview",
        "category",
        "brand",
        "location",
        "source",
        "description",
        "qty"
    )

    list_filter = ("name", "sku", "category", "brand", "location", "source")

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 50px; width: auto;" />',
                obj.image.url,
            )
        return "-"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 300px;" />',
                obj.image.url,
            )
        return "No image"

    image_thumbnail.short_description = "Image"


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
