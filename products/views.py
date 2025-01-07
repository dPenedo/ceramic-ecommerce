from django.views import generic
from .models import Pieza


# Create your views here.
class HomepageView(generic.ListView):
    template_name = "homepage.html"
    context_object_name = "piezas"

    def get_queryset(self):
        return Pieza.objects.all()


class DetailView(generic.DetailView):
    model = Pieza
    template_name = "details.html"
