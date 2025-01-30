from django.contrib import admin
from .models import Persona, Libro, Autor, BlogPost

admin.site.register(Persona)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(BlogPost)