from django.db import models
from django.contrib.auth.models import *



# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=250)
    autor = models.CharField(max_length=40)
    fecha = models.DateField()
    foto = models.ImageField(upload_to='blogs',null=True, blank=True)
    
    def __str__(self):
        return self.titulo + " " + self.autor + " " + str(self.fecha)
    
class Perfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='avatares',null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Mensaje(models.Model):
    usuario_origen = User
    usuario_destino = User
    texto = models.CharField(max_length=250)
    

