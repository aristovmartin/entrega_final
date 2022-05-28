from django.urls import path
from accountsApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="cuentas"),
    path('register', views.registro, name="registro"),
    path('login', views.login, name="login"),
    path('logout', LogoutView.as_view(template_name='accountsApp/logout.html'), name="logout"),
    path('inicio', views.login, name="volver_blog"),

]
