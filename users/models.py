from django.db import models
from django.contrib.auth.models import AbstractUser
from cart.models import Carrito
from products.models import Pieza

# Create your models here.


class Usuario(AbstractUser):
    nombre = models.CharField(max_length=50, blank=False, null=True)
    apellido = models.CharField(max_length=50, blank=False, null=True)
    pais = models.CharField(max_length=50, blank=False, null=True)
    provincia = models.CharField(max_length=50, blank=False, null=True)
    ciudad = models.CharField(max_length=50, blank=False, null=True)
    domicilio = models.CharField(max_length=50, blank=False, null=True)
    codigo_postal = models.CharField(max_length=8, blank=False, null=True)
    telefono = models.CharField(max_length=15, blank=False, null=True)
    fecha_de_registro = models.DateTimeField(
        "Fecha de registro", auto_now_add=True, blank=False, null=True
    )

    def __str__(self):
        return self.username
