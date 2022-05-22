from django import forms

class UsuarioForm(forms.Form):
    email = forms.EmailField()
    contrasena = forms.CharField(max_length=20)
    nombre_usuario = forms.CharField(max_length=30)
    
class BlogForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=250)
    autor = forms.CharField(max_length=40)
    fecha = forms.DateField()
    
class MensajeForm(forms.Form):
    id_usuario_origen = forms.IntegerField()
    id_usuario_destino = forms.IntegerField()
    texto = forms.CharField(max_length=250)
