from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

def register_user(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
        
        # Adicionar requisitos de senha
        # Comprimento >= 8
        # Pelo menos uma letra Maiúscula
        # Pelo menos um símbolo especial
        # Pelo menos um número

        elif User.objects.filter(email=email).exists():
            messages.error(request, "O e-mail já está em uso.")
        
        elif User.objects.filter(username=username).exists():
            messages.error(request, "O nome de usuário já está em uso.")
        
        else:
            User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
            messages.success(request, "Usuário registrado com sucesso.")
            return redirect("login_user")
    
    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso.")
            return redirect("mobilizacao:dashboard")
        
        else:
            messages.error(request, "Nome de usuário ou senha incorretos.")

    return render(request, "login.html")


def login_register_user(request):
    active_form = "register" if request.GET.get("registered") == "1" else "login"
    auto_switch_to_login = request.GET.get("registered") == "1"
    is_ajax = request.headers.get("x-requested-with") == "XMLHttpRequest"

    if request.method == "POST":
        auth_action = request.POST.get("auth_action", "login")
        active_form = "register" if auth_action == "register" else "login"

        if active_form == "register":
            first_name = request.POST.get("first_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")

            if password != confirm_password:
                message = "As senhas nao coincidem."
                if is_ajax:
                    return JsonResponse({"success": False, "message": message, "type": "error"}, status=400)
                messages.error(request, message)
            elif User.objects.filter(email=email).exists():
                message = "O e-mail ja esta em uso."
                if is_ajax:
                    return JsonResponse({"success": False, "message": message, "type": "error"}, status=400)
                messages.error(request, message)
            elif User.objects.filter(username=username).exists():
                message = "O nome de usuario ja esta em uso."
                if is_ajax:
                    return JsonResponse({"success": False, "message": message, "type": "error"}, status=400)
                messages.error(request, message)
            else:
                User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
                message = "Usuario registrado com sucesso."
                if is_ajax:
                    return JsonResponse({"success": True, "message": message, "type": "success"})
                messages.success(request, message)
                return redirect(f"{reverse('login_register_user')}?registered=1")

        else:
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login realizado com sucesso.")
                return redirect("mobilizacao:dashboard")

            messages.error(request, "Nome de usuario ou senha incorretos.")

    return render(
        request,
        "loginRegister.html",
        {
            "active_form": active_form,
            "auto_switch_to_login": auto_switch_to_login,
        },
    )


def logout_user(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso.")
    return redirect("login_user")


def teste_page(request): # Apagar depois
    return render(request, "teste.html")
