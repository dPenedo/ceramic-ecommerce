from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout
from django.utils.html import json

from cart.models import Carrito, CarritoItem
from products.models import Pieza
from users.forms import CreateUserForm, EditProfileForm


def register_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            print(f" request.POST =>{request.POST}")

            if "conservar_carrito" in request.POST:
                print("conservar_carrito está en request.POST")

            if (
                "conservar_carrito" in request.POST
                and request.POST["conservar_carrito"] == "on"
            ):
                print("Se seleccionó conservar carrito")
            else:
                print("No se seleccionó conservar carrito")

            # Verificar si se seleccionó la opción de conservar el carrito
            if (
                "conservar_carrito" in request.POST
                and request.POST["conservar_carrito"] == "on"
            ):
                carrito_data = request.POST.get(
                    "carrito_data"
                )  # Obtener el carrito del formulario
                print(
                    f"Carrito data recibido: {carrito_data}"
                )  # Verifica los datos recibidos
                if carrito_data:
                    try:
                        # Decodificar los datos del carrito del localStorage
                        carrito_data = json.loads(carrito_data)
                        print(
                            f"Carrito data decodificado: {carrito_data}"
                        )  # Verifica los datos decodificados
                        # Crear el carrito para el usuario
                        carrito = Carrito.objects.create(usuario=user)
                        print(f"Carrito creado para el usuario: {carrito}")
                        for item in carrito_data:
                            pieza = Pieza.objects.get(
                                id=item["id"]
                            )  # Obtener la pieza por ID
                            CarritoItem.objects.create(
                                carrito=carrito, pieza=pieza, cantidad=item["amount"]
                            )
                            print(f"Carrito item creado: {item}")
                        print("Carrito almacenado correctamente.")
                    except Exception as e:
                        print(f"Error al guardar el carrito: {e}")

            return redirect("/")  # Redirigir al inicio después de registrar al usuario
        else:
            return render(
                request,
                "cuenta/registro.html",
                {"form": form, "error": "Formulario inválido"},
            )
    else:
        form = CreateUserForm()
    return render(request, "cuenta/registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "cuenta/login.html", {"form": form})


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "cuenta/edit-profile.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
