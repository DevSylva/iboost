from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse



# Create your views here.
def register(request):
    if request.user.is_authenticated and request.method == "GET":
        return redirect("core:dashboard")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("core:home")
        else:
            messages.error(request, form.errors)
            print(form.errors)
    form = SignUpForm()
    return render(request, "register.html", {"form": form})


def loginView(request):
    if request.user.is_authenticated and request.method == "GET":
        return redirect("core:dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("core:dashboard")
                
            else:
                messages.error(request, "User does not exit")
        else:
            messages.error(request, form.errors.as_ul())
            print(form.errors)
            return redirect("account:login")

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@login_required(login_url="account:login")
def changePassword(request):
    password_form = PasswordChangeForm(request.user)

    if request.method == "POST":
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)

            messages.success(request, "Your password has been updated")
            return redirect(reverse("core:dashboard"))

    return render(request, "change-password.html", {"password_form": password_form} )

def log_out(request):
    logout(request)
    return redirect("account:login")