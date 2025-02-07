from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
from django import forms


class CreateUserForm(UserCreationForm):
    nombre = forms.CharField(required=True, label="Nombre")
    apellido = forms.CharField(required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")
    pais = forms.CharField(required=True)
    provincia = forms.CharField(required=True)
    ciudad = forms.CharField(required=True)
    domicilio = forms.CharField(required=True)
    codigo_postal = forms.CharField(required=True)
    telefono = forms.CharField()

    class Meta:
        model = Usuario
        fields = (
            "email",
            "nombre",
            "apellido",
            "pais",
            "provincia",
            "ciudad",
            "domicilio",
            "codigo_postal",
            "telefono",
            "password1",
            "password2",
        )


class EditProfileForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = (
            "nombre",
            "apellido",
            "email",
            "pais",
            "provincia",
            "ciudad",
            "domicilio",
            "codigo_postal",
            "telefono",
        )
        exclude = ("password",)
