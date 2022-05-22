from django.contrib import admin
from .models import *

admin.site.register(Blog)

admin.site.register(Usuario)

admin.site.register(Mensaje)

# superUsuario: martin password:martin123