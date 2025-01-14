from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    usuario = models.OneToOneField(
        User, blank=False, null=True, on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=8)
    telefono = models.CharField(max_length=15)
    fecha_de_registro = models.DateTimeField("Fecha de registro", auto_now_add=True)

    def __str__(self):
        return self.usuario.username
