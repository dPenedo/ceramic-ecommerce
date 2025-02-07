from django.db.models import Sum
from cart.models import Carrito, CarritoItem


def numero_de_items_del_carrito(request):
    "Obtener la cuenta de elementos totales en el carrito. Usado en la navbar"
    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user).first()
        if carrito:
            count = (
                CarritoItem.objects.filter(carrito=carrito).aggregate(
                    total=Sum("cantidad")
                )["total"]
                or 0
            )
        else:
            count = 0
    else:
        count = 0

    return {"cuenta_carrito": count}
