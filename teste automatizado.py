import unittest
from calculadora import calculadora

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora("10 + 6"), 15)

    def test_subtracao(self):
        self.assertEqual(calculadora("10 - 5"), 5)

    def test_multiplicacao(self):
        self.assertEqual(calculadora("10 * 5"), 50)

    def test_divisao(self):
        self.assertEqual(calculadora("10 / 2"), 5)

    def test_divisao_por_zero(self):
        self.assertIsNone(calculadora("10 / 0"))

    def test_operador_invalido(self):
        self.assertIsNone(calculadora("10 % 5"))

    def test_expressao_invalida_somente_um_numero(self):
        self.assertIsNone(calculadora("10 +"))

    def test_expressao_invalida_faltando_operador(self):
        self.assertIsNone(calculadora("10 5"))

    def test_letras_em_vez_de_numeros(self):
        self.assertIsNone(calculadora("a + 5"))

    def test_letras_no_segundo_numero(self):
        self.assertIsNone(calculadora("5 + b"))

    def test_operador_invalido_com_caracteres_especiais(self):
        self.assertIsNone(calculadora("5 & 2"))

    def test_espacos_extras(self):
        self.assertEqual(calculadora(" 10 + 5 "), 15)

    def test_float_com_operador_soma(self):
        self.assertEqual(calculadora("10.5 + 5.3"), 15.8)

    def test_float_com_operador_divisao(self):
        self.assertEqual(calculadora("9.6 / 2"), 4.8)

    def test_float_com_operador_multiplicacao(self):
        self.assertEqual(calculadora("5.5 * 2"), 11)

    def test_float_com_operador_subtracao(self):
        self.assertEqual(calculadora("10.2 - 3.1"), 7.1)

    def test_expressao_muito_grande(self):
        self.assertIsNone(calculadora("10 + 5 + 2"))

    def test_expressao_sem_espacos(self):
        self.assertIsNone(calculadora("10+5"))

    def test_zeros_extras(self):
        self.assertEqual(calculadora("00010 + 0005"), 15)

    def test_numeros_negativos(self):
        self.assertEqual(calculadora("-10 + -5"), -15)

if __name__ == "__main__":
    unittest.main()
