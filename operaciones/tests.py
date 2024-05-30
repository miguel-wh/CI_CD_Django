from django.test import TestCase
from django.urls import reverse

class OperacionesTests(TestCase):
    """
    def test_sumar(self):
        response = self.client.get(reverse('sumar'), {'a': 1, 'b': "d"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'resultado': 3})

    def test_restar(self):
        response = self.client.get(reverse('restar'), {'a': 5, 'b': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'resultado': 2})

    def test_multiplicar(self):
        response = self.client.get(reverse('multiplicar'), {'a': 2, 'b': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'resultado': 6})

    def test_dividir(self):
        response = self.client.get(reverse('dividir'), {'a': 10, 'b': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'resultado': 5})

        response = self.client.get(reverse('dividir'), {'a': 10, 'b': 0})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'No se puede dividir por cero'})
    
    """
    def test_par(self):
        response = self.client.get(reverse('detectar_par'), {'a': "2"})
        self.assertEqual(response.json(), {'resultado': True})

