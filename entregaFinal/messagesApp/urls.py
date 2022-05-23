from django.urls import path
from messagesApp import views

urlpatterns = [
    path('', views.main_mensajes, name="mensajes"),

]
