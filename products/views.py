from django.views import generic
from .models import Pieza, TipoDePieza
from django.http import JsonResponse


# Create your views here.
class HomepageView(generic.ListView):
    template_name = "homepage.html"
    context_object_name = "piezas"

    def get_queryset(self):
        queryset = Pieza.objects.all()

        autora = self.request.GET.get("autora")
        if autora:
            queryset = queryset.filter(autora=autora)

        tipo_id = self.request.GET.get("tipo")
        if tipo_id:
            queryset = queryset.filter(tipo_id=tipo_id)

        sort_by = self.request.GET.get("sort")
        if sort_by == "mayor_precio":
            queryset = queryset.order_by("-precio")
        if sort_by == "menor_precio":
            queryset = queryset.order_by("precio")
        if sort_by == "mas_reciente":
            queryset = queryset.order_by("-fecha_de_publicacion")
        if sort_by == "mas_antiguo":
            queryset = queryset.order_by("fecha_de_publicacion")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipos_de_pieza"] = TipoDePieza.objects.all()
        context["autoras"] = Pieza.AUTHORS
        return context


class DetailView(generic.DetailView):
    model = Pieza
    template_name = "details.html"


class CartView(generic.ListView):
    template_name = "carrito.html"
    context_object_name = "piezas"

    def get_queryset(self):
        shopping_cart_list = self.request.GET.get("shopping-cart")
        if shopping_cart_list:
            return Pieza.objects.filter(id__in=shopping_cart_list)
        return Pieza.objects.none()


def stock_view(request, product_id):
    if request.method == "GET":
        try:
            pieza = Pieza.objects.get(id=product_id)
            data = {"id": pieza.id, "titulo": pieza.titulo, "stock": pieza.stock}
            return JsonResponse(data)
        except Pieza.DoesNotExist:
            return JsonResponse({"error": "Producto no encontrado"}, status=404)
