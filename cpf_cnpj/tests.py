from django.test import TestCase, Client
from .utils import generate_cpf, calculate_cpf_check_digits, generate_cnpj, calculate_cnpj_check_digits

class CpfCnpjUtilsTests(TestCase):
    def test_generate_cpf_unmasked(self):
        cpf = generate_cpf(mask=False)
        self.assertRegex(cpf, r'^\d{11}$')
        base_digits = list(map(int, cpf[:9]))
        d1, d2 = calculate_cpf_check_digits(base_digits)
        self.assertEqual(cpf[-2:], f"{d1}{d2}")

    def test_generate_cpf_masked(self):
        cpf = generate_cpf(mask=True)
        self.assertRegex(cpf, r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

    def test_generate_cnpj_unmasked(self):
        cnpj = generate_cnpj(mask=False)
        self.assertRegex(cnpj, r'^\d{14}$')
        base_digits = list(map(int, cnpj[:12]))
        d1, d2 = calculate_cnpj_check_digits(base_digits)
        self.assertEqual(cnpj[-2:], f"{d1}{d2}")

    def test_generate_cnpj_masked(self):
        cnpj = generate_cnpj(mask=True)
        self.assertRegex(cnpj, r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$')

class CpfCnpjViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_generate_cpf_view_defaults(self):
        response = self.client.get('/api/cpf/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('cpf', data)
        self.assertRegex(data['cpf'], r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

    def test_generate_cnpj_view_unmasked(self):
        response = self.client.get('/api/cnpj/?mask=false')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('cnpj', data)
        self.assertRegex(data['cnpj'], r'^\d{14}$')
