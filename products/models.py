from django.db import models


class TipoDePieza(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.descripcion:
            self.descripcion = self.nombre
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Pieza(models.Model):
    AUTHORS = {"AGV": "Ariadna Gorostegui Valenti", "VC": "Veronica Cepeda"}
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = models.FloatField()
    tipo = models.ForeignKey(TipoDePieza, on_delete=models.CASCADE)
    autora = models.CharField(max_length=3, choices=AUTHORS)
    imagen = models.ImageField(upload_to="piezas", blank=True)
    fecha_de_publicacion = models.DateTimeField("Fecha de publicación")
    stock = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.titulo} - {self.tipo} de {self.autora}"

    def complete_name(self):
        return self.AUTHORS[self.autora]
