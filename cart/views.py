from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Pieza


# Create your views here.
class AddToCart(LoginRequiredMixin, View):
    def post(self, request, pieza_id):
        pass


class LocalStorageCartView(generic.ListView):
    template_name = "carrito.html"
    context_object_name = "piezas"

    def get_queryset(self):
        shopping_cart_list = self.request.GET.getlist("shopping-cart")
        if shopping_cart_list:
            try:
                shopping_cart_list = [int(pid) for pid in shopping_cart_list]
                return Pieza.objects.filter(id__in=shopping_cart_list)
            except ValueError:
                return Pieza.objects.none()
        return Pieza.objects.none()
