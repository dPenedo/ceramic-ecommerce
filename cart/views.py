from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Carrito, CarritoItem, Pieza


class AddToCart(LoginRequiredMixin, View):
    """Añadir una pieza al carrito de la base de datos"""

    def post(self, request, pieza_id):
        pieza = get_object_or_404(Pieza, id=pieza_id)

        if pieza.stock > 0:
            carrito, created = Carrito.objects.get_or_create(usuario=request.user)
            cartItem, created = CarritoItem.objects.get_or_create(
                carrito=carrito, pieza=pieza
            )

            if not created and cartItem.cantidad < pieza.stock:
                cartItem.cantidad += 1
                cartItem.save()
                print(f"Sumado {pieza}")
            elif created:
                cartItem.cantidad = 1
                cartItem.save()
                print(f"Sumado {pieza}")
            else:
                print("no queda stock")
                return redirect(request.META.get("HTTP_REFERER"))

            return redirect(
                request.META.get("HTTP_REFERER")
            )  # Redirige a la página anterior
        else:
            print("no hay stock")
            return redirect(request.META.get("HTTP_REFERER"))


class RemoveFromCart(LoginRequiredMixin, View):
    """Eliminar una pieza del carrito de la base de datos"""

    def post(self, request, pieza_id):
        carrito = get_object_or_404(Carrito, usuario=request.user)
        carrito_item = get_object_or_404(
            CarritoItem, carrito=carrito, pieza__id=pieza_id
        )
        print(f"carrito item -> {carrito_item}")
        print(f"carrito item cantidad -> {carrito_item.cantidad}")
        if carrito_item.cantidad > 1:
            carrito_item.cantidad -= 1
            carrito_item.save()

        else:
            carrito_item.delete()
        return redirect(request.META.get("HTTP_REFERER"))


def obtener_cantidad_en_carrito(request, pieza_id):
    """Obtener la cantidad de una pieza en el carrito de la base de datos, para no exceder el stock. Usado en el Details"""

    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user).first()
        if carrito:
            return (
                CarritoItem.objects.filter(
                    carrito=carrito, pieza_id=pieza_id
                ).aggregate(total=Sum("cantidad"))["total"]
                or 0
            )
    return 0


class DatabaseCartView(LoginRequiredMixin, generic.ListView):
    """ "Obtiene la lista de elementos en el carrito de la base de datos"""

    template_name = "carrito.html"
    context_object_name = "piezas"

    def get_queryset(self):
        carrito = Carrito.objects.filter(usuario=self.request.user).first()
        if carrito:
            print(CarritoItem.objects.filter(carrito=carrito))
            return CarritoItem.objects.filter(carrito=carrito)
        return Carrito.objects.none()


class LocalStorageCartView(generic.ListView):
    """Obtiene la lista de elementos en el carrito de la url que genera el carrito-page.js"""

    template_name = "carrito.html"
    context_object_name = "piezaslocal"

    def get_queryset(self):
        shopping_cart_list = self.request.GET.getlist("shopping-cart")
        if shopping_cart_list:
            try:
                shopping_cart_list = [int(pid) for pid in shopping_cart_list]
                return Pieza.objects.filter(id__in=shopping_cart_list)
            except ValueError:
                return Pieza.objects.none()
        return Pieza.objects.none()
