from django.contrib.auth.forms import User, UserCreationForm, UserChangeForm
from .models import Usuario
from django import forms


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

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
