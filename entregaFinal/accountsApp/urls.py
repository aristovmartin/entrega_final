from django.urls import path, include
from accountsApp import views

urlpatterns = [
    path('', views.home, name="cuentas"),
    path('registro', views.registro, name="registro"),
    path('inicioSesion', views.login, name="login"),
    path('inicio', views.login, name="volver_blog"),

]
