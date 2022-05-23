from django.shortcuts import render
from blogApp.models import *
from blogApp.forms import *
# Create your views here.

def main_mensajes(request):
    return render(request,'mensajes.html')
