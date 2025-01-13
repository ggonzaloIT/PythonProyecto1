from django.contrib import admin
from .models import Persona, Libro, Autor

admin.site.register(Persona)
admin.site.register(Libro)
admin.site.register(Autor)