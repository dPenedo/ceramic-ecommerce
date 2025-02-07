from users.models import Usuario

from django.contrib import admin
from cart.models import Carrito, CarritoItem


@admin.action(description="Eliminar usuarios seleccionados y sus objetos relacionados")
def eliminar_usuarios(modeladmin, request, queryset):
    for usuario in queryset:
        # Eliminar objetos relacionados manualmente
        CarritoItem.objects.filter(
            carrito__usuario=usuario
        ).delete()  # Eliminar items del carrito
        Carrito.objects.filter(usuario=usuario).delete()  # Eliminar carritos
        usuario.delete()  # Eliminar el usuario


class UsuarioAdmin(admin.ModelAdmin):
    actions = [eliminar_usuarios]


admin.site.register(Usuario, UsuarioAdmin)
