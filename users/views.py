from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout

from users.forms import CreateUserForm, EditProfileForm


def register_view(request):
    params = {}
    form = CreateUserForm()
    params["form"] = form
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
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
