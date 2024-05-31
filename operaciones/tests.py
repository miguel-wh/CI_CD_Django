from django.test import TestCase
from django.urls import reverse

class OperacionesTests(TestCase):
    def test_sumar(self):
        response = self.client.get(reverse('sumar'), {'a': 1, 'b': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'resultado': 3})

    def test_sumar_parametros_invalidos(self):
        response = self.client.get(reverse('sumar'), {'a': 'uno', 'b': 2})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Los parámetros deben ser números enteros'})

        response = self.client.get(reverse('sumar'), {'a': 1, 'b': 'dos'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Los parámetros deben ser números enteros'})

        response = self.client.get(reverse('sumar'), {'a': 'uno', 'b': 'dos'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Los parámetros deben ser números enteros'})


    def test_es_par(self):
        response = self.client.get(reverse('detectar_par'), {'a': "2"})
        self.assertEqual(response.json(), {'resultado': True})

