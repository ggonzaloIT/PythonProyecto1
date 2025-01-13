from django.test import TestCase
from .models import Model1, Model2, Model3

class Model1TestCase(TestCase):
    def setUp(self):
        Model1.objects.create(field1="Test1", field2="Test2")

    def test_model1_creation(self):
        model1 = Model1.objects.get(field1="Test1")
        self.assertEqual(model1.field2, "Test2")

class Model2TestCase(TestCase):
    def setUp(self):
        Model2.objects.create(field1="Example1", field2="Example2")

    def test_model2_creation(self):
        model2 = Model2.objects.get(field1="Example1")
        self.assertEqual(model2.field2, "Example2")

class Model3TestCase(TestCase):
    def setUp(self):
        Model3.objects.create(field1="Sample1", field2="Sample2")

    def test_model3_creation(self):
        model3 = Model3.objects.get(field1="Sample1")
        self.assertEqual(model3.field2, "Sample2")