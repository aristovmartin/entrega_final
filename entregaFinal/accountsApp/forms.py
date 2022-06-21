from django.contrib.auth.forms import *
from django import forms
from django.contrib.auth.models import *

class UserEditForm(UserCreationForm):
    
    username = forms.CharField()
    email = forms.EmailField(label="Modificar mail", required = False)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput,required = True)
    password2 = forms.CharField(label="Repetir password", widget=forms.PasswordInput, required = True)
    last_name = forms.CharField(required=False)    
    first_name = forms.CharField(required=False)
    foto = forms.ImageField(required=True)    
    class Meta:
        model = User
        fields = ['username','email','password1','password2','last_name','first_name','foto']