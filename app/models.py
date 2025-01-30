from django.db import models
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='', blank=True, null=True)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return f'<b>Nombre:</b> {self.nombre} - <b>Libro alquilado:</b> {self.descripcion}'


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return f'<b>Titulo:</b> {self.titulo} - <b>Fecha de entrada:</b> {self.fecha}'

class Autor(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return f'<b>Autor/a:</b> {self.autor} - <b>Libro/s:</b> {self.contenido}'