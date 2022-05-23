from django.urls import path, include
from blogApp import views

urlpatterns = [
    path('', views.main, name="inicio"),
    path('about', views.about_me, name="about"),
    path('blog/<id>', views.pagina_blog, name="pagina_blog"),
    path('crearBlog', views.crear_blog, name="crear_blog"),
    path('editarBlog/<id>', views.editar_blog, name="editar_blog"),
    path('borrarBlog/<id>', views.eliminar_blog, name="eliminar_blog"),
    path('mensajes', include('messagesApp.urls'), name="mensajes"),

]
