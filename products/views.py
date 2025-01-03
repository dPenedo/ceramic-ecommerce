from django.shortcuts import render
from .models import Product


# Create your views here.
def homepage(request):
    products = Product.objects.all()
    return render(request, "homepage.html", {'products': products})
