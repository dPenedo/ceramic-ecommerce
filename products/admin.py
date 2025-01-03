from django.contrib import admin
from .models import Product, TypeOfProduct

# Register your models here.

# class ProductsAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Product)
admin.site.register(TypeOfProduct)
