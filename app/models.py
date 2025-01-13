from django.db import models

class Model1(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f'<b>Nombre:</b> {self.nombre} - <b>Libro alquilado:</b> {self.descripcion}'

class Model2(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return f'<b>Titulo:</b> {self.titulo} - <b>Fecha de entrada:</b> {self.fecha}'

class Model3(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()

    def __str__(self):
        return f'<b>Autor/a:</b> {self.autor} - <b>Libro/s:</b> {self.contenido}'