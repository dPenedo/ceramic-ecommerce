from django.db.models import query
from django.views import generic
from .models import Pieza, TipoDePieza


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

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipos_de_pieza"] = TipoDePieza.objects.all()
        context["autoras"] = Pieza.AUTHORS
        return context


class DetailView(generic.DetailView):
    model = Pieza
    template_name = "details.html"
