from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    return render(request, "accounts/login.html", {"form": form})
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)  # or CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate the user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticated_user = authenticate(username=username, password=raw_password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect("/")
    else:
        form = CustomUserCreationForm()  # or CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/login/")