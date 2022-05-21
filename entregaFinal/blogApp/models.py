from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=250)
    autor = models.CharField(max_length=40)
    fecha = models.DateField()
    #falta ver como poner imagen
    
    def __str__(self):
        return self.titulo + " " + self.autor + " " + str(self.fecha)
    
class Usuario(models.Model):
    email = models.EmailField()
    contrasena = models.CharField(max_length=20)
    nombre_usuario = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_usuario + " " + self.email

