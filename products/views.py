from django.views import generic
from .models import Pieza, TipoDePieza


# Create your views here.
class HomepageView(generic.ListView):
    template_name = "homepage.html"
    context_object_name = "piezas"

    def get_queryset(self):
        return Pieza.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipos_de_pieza"] = TipoDePieza.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Pieza
    template_name = "details.html"
