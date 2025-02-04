from django.core.checks import messages
from django.http import HttpResponse, request
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Carrito, CarritoItem, Pieza


class AddToCart(LoginRequiredMixin, View):
    def post(self, request, pieza_id):
        pieza = get_object_or_404(Pieza, id=pieza_id)

        if pieza.stock > 0:
            carrito, created = Carrito.objects.get_or_create(usuario=request.user)
            cartItem, created = CarritoItem.objects.get_or_create(
                carrito=carrito, pieza=pieza
            )

            # WARN: No debería agotar el stock, porque no compra!!
            if not created and cartItem.cantidad < pieza.stock:
                cartItem.cantidad += 1
                cartItem.save()
                pieza.stock -= 1
                pieza.save()
                print(f"Sumado {pieza}")
            elif created:
                cartItem.cantidad = 1
                cartItem.save()
                pieza.stock -= 1
                pieza.save()
                print(f"Sumado {pieza}")
            else:
                # Si no hay suficiente stock, muestra un mensaje de error
                print("no queda stock")
                return redirect(request.META.get("HTTP_REFERER"))

            return redirect(
                request.META.get("HTTP_REFERER")
            )  # Redirige a la página anterior
        else:
            # Si no hay stock, muestra un mensaje de error
            print("no hay stock")
            return redirect(request.META.get("HTTP_REFERER"))


class RemoveFromCart(LoginRequiredMixin, View):
    def post(self, request, pieza_id):
        carrito_item = get_object_or_404(
            CarritoItem,
            pieza_id=pieza_id,
            carrito__usuario=request.user,  # Cambiado aquí?
        )
        carrito_item.delete()
        return redirect("/")


class DatabaseCartView(LoginRequiredMixin, generic.ListView):
    template_name = "carrito.html"
    context_object_name = "piezas"

    def get_queryset(self):
        carrito = Carrito.objects.filter(usuario=self.request.user).first()
        if carrito:
            print("databasss")
            print(CarritoItem.objects.filter(carrito=carrito))
            return CarritoItem.objects.filter(carrito=carrito)
        return Carrito.objects.none()


class LocalStorageCartView(generic.ListView):
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
