from django.shortcuts import render
from .models import Pieza


# Create your views here.
def homepage(request):
    piezas = Pieza.objects.all()
    return render(request, "homepage.html", {"piezas": piezas})
