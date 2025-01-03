from django.db import models


class TypeOfProduct(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = self.title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    AUTHORS = {
        "AGV": "Ariadna Gorostegui Valenti",
        "VC": "Veronica Cepeda"
    }
    title = models.CharField(max_length=100)
    price = models.FloatField()
    type = models.ForeignKey(TypeOfProduct, on_delete=models.CASCADE)
    author = models.CharField(max_length=3, choices=AUTHORS)

    def __str__(self):
        return f"{self.title} - {self.type} de {self.author}"

    def complete_name(self):
        return self.AUTHORS[self.author]
