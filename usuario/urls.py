from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("logout/", views.sair, name="logout"),
    path("usuario/cadastro/", views.registration, name="registration"),

    path("perfil/", views.perfil, name="perfil"),
]