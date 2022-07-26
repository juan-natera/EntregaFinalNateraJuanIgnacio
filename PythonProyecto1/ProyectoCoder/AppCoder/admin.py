from django.contrib import admin
from  .models import *

# Register your models here.
#registramos los modelos

admin.site.register(Curso)

admin.site.register(Estudiante)

admin.site.register(Profesor)

admin.site.register(Entregable)

admin.site.register(Avatar)