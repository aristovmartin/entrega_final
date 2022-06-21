from django import forms

class UsuarioForm(forms.Form):
    email = forms.EmailField()
    contrasena = forms.CharField(max_length=20)
    nombre_usuario = forms.CharField(max_length=30)
    
class BlogForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=250)
    foto = forms.ImageField(required=True)
    
class MensajeForm(forms.Form):
    usuario_origen = forms.CharField(max_length=50)
    usuario_destino = forms.CharField(max_length=50)
    texto = forms.CharField(max_length=250)
