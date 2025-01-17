from django.contrib.auth.forms import User, UserCreationForm, UserChangeForm
from .models import Usuario
from django import forms


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label="Nombre de cuenta")
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    pais = forms.CharField(required=True)
    provincia = forms.CharField(required=True)
    ciudad = forms.CharField(required=True)
    domicilio = forms.CharField(required=True)
    codigo_postal = forms.CharField(required=True)
    telefono = forms.CharField()

    class Meta:
        model = Usuario
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
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
            "first_name",
            "last_name",
            "email",
            "pais",
            "provincia",
            "ciudad",
            "domicilio",
            "codigo_postal",
            "telefono",
        )
        # exclude = ()
