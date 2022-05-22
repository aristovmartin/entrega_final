from django.urls import path
from blogApp import views

urlpatterns = [
    path('', views.main, name="inicio"),
    path('about', views.about_me, name="about"),
    path('blog/<id>', views.pagina_blog, name="pagina_blog"),

]
