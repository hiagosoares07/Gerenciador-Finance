from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login_user"),
    path("users/register/", views.register_user, name="register_user"),
    path("users/login/", views.login_user, name="login_user"),
    path("users/loginregister/", views.login_register_user, name="login_register_user"),
    path("users/logout/", views.logout_user, name="logout_user"),
    # path("users/teste/", views.teste_page, name="teste_page"), # apagar isso depois
]
