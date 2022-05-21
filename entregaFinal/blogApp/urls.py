from django.urls import path
from blogApp import views

urlpatterns = [
    path('', views.home, name="inicio"),
    path('about', views.about_me, name="about"),

]
