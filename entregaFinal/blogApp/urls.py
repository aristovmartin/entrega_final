from django.urls import path, include
from blogApp import views

urlpatterns = [
    path('', views.main, name="inicio"),
    path('about', views.about_me, name="about"),
    path('blog/<id>', views.pagina_blog, name="pagina_blog"),
    path('crearBlog', views.crear_blog, name="crear_blog"),
    path('editarBlog/<id>', views.editar_blog, name="editar_blog"),
    path('borrarBlog/<id>', views.eliminar_blog, name="eliminar_blog"),
    path('mensajes',views.mensajes, name="mensajes"),
    path('enviarMensajes',views.enviar_mensajes, name="enviar_mensajes"),
    path('accounts/',include('accountsApp.urls'), name="cuentas"),
    path('borrarFoto/<id>',views.borrar_foto, name="borrar_foto_blog"),

]
