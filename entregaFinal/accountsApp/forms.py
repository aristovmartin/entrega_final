from django.contrib.auth.forms import *
from django import forms
from django.contrib.auth.models import *

class UserEditForm(UserCreationForm):
    
    username = forms.CharField()
    email = forms.EmailField(label="Modificar mail")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir password", widget=forms.PasswordInput)
    last_name = forms.CharField()    
    first_name = forms.CharField()    
    class Meta:
        model = User
        fields = ['username','email','password1','password2','last_name','first_name']