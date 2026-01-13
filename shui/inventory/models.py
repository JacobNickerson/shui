from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name