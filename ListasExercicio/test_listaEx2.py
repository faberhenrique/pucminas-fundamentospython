import unittest

from listaEx2 import (area_figura, calculadora, calculate_days_passed,
                      contar_vogais, criar_dicionario, decimal_para_binario,
                      exibir_nomes_ordenados, fatorial, filtrar_pares,
                      is_palindrome, is_prime, media)


class TestListaEx2(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))

    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(3), 6)

    def test_media(self):
        self.assertEqual(media([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(media([]), 0)
        self.assertEqual(media([10, 20, 30]), 20.0)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("ana"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))

    def test_filtrar_pares(self):
        self.assertEqual(filtrar_pares([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filtrar_pares([1, 3, 5]), [])
        self.assertEqual(filtrar_pares([]), [])

    def test_area_figura(self):
        self.assertAlmostEqual(area_figura("círculo", 5), 78.5)
        self.assertEqual(area_figura("quadrado", 4), 16)
        self.assertEqual(area_figura("triângulo", 3, 4), 6.0)
        self.assertIsNone(area_figura("hexágono", 5))

    def test_calculate_days_passed(self):
        self.assertEqual(calculate_days_passed("01/01/2023"), 1)
        self.assertEqual(calculate_days_passed("31/12/2023"), 365)
        self.assertEqual(calculate_days_passed("29/02/2024"), 60)  # Leap year

    def test_calculadora(self):
        self.assertEqual(calculadora("soma", 5, 3), 8)
        self.assertEqual(calculadora("subtracao", 10, 4), 6)
        self.assertEqual(calculadora("multiplicacao", 2, 3), 6)
        self.assertEqual(calculadora("divisao", 10, 2), 5.0)
        self.assertIsNone(calculadora("modulo", 10, 2))

    def test_exibir_nomes_ordenados(self):
        nomes = ["Carlos", "Ana", "Bruno", "Diana"]
        exibir_nomes_ordenados(nomes)
        self.assertEqual(nomes, ["Ana", "Bruno", "Carlos", "Diana"])

    def test_decimal_para_binario(self):
        self.assertEqual(decimal_para_binario(10), "1010")
        self.assertEqual(decimal_para_binario(0), "0")
        self.assertEqual(decimal_para_binario(255), "11111111")

    def test_contar_vogais(self):
        self.assertEqual(contar_vogais("hello"), 2)
        self.assertEqual(contar_vogais("aeiou"), 5)
        self.assertEqual(contar_vogais("bcdfg"), 0)

    def test_criar_dicionario(self):
        chaves = ["nome", "idade", "cidade"]
        valores = ["Carlos", 30, "São Paulo"]
        self.assertEqual(
            criar_dicionario(chaves, valores),
            {"nome": "Carlos", "idade": 30, "cidade": "São Paulo"},
        )
        with self.assertRaises(ValueError):
            criar_dicionario(["a", "b"], [1])


if __name__ == "__main__":
    unittest.main()
