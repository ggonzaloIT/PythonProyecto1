from django.test import TestCase
from .models import Persona, Libro, Autor

class PersonaTestCase(TestCase):
    def setUp(self):
        Persona.objects.create(field1="Test1", field2="Test2")

    def test_Persona_creation(self):
        persona = Persona.objects.get(field1="Test1")
        self.assertEqual(persona.field2, "Test2")

class LibroTestCase(TestCase):
    def setUp(self):
        Libro.objects.create(field1="Example1", field2="Example2")

    def test_Libro_creation(self):
        libro = Libro.objects.get(field1="Example1")
        self.assertEqual(libro.field2, "Example2")

class AutorTestCase(TestCase):
    def setUp(self):
        Autor.objects.create(field1="Sample1", field2="Sample2")

    def test_Autor_creation(self):
        autor = Autor.objects.get(field1="Sample1")
        self.assertEqual(autor.field2, "Sample2")