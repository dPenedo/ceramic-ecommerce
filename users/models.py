from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser debe tener is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
    username = None

    email = models.EmailField("email address", unique=True, blank=False, null=False)

    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    pais = models.CharField(max_length=50, blank=False, null=False)
    provincia = models.CharField(max_length=50, blank=False, null=False)
    ciudad = models.CharField(max_length=50, blank=False, null=False)
    domicilio = models.CharField(max_length=50, blank=False, null=False)
    codigo_postal = models.CharField(max_length=8, blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    fecha_de_registro = models.DateTimeField(
        "Fecha de registro", auto_now_add=True, blank=False, null=False
    )

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre", "apellido"]

    def __str__(self):
        return self.nombre if self.nombre else "no tiene nombre"
