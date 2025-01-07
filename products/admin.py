from django.contrib import admin
from .models import Pieza, TipoDePieza

# Register your models here.

# class ProductsAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Pieza)
admin.site.register(TipoDePieza)
