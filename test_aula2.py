import unittest
from unittest.mock import patch, MagicMock
from aula2 import buscar_clima, buscar_qualidade_ar, buscar_dados_pais

class TestAula2(unittest.TestCase):

    @patch('aula2.requests.get')
    def test_buscar_clima_success(self, mock_get):
        # Mocking a successful API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"location": {"name": "Belo Horizonte"}, "current": {"temp_c": 25}}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = buscar_clima("Belo Horizonte")
        self.assertIsNotNone(result)
        self.assertEqual(result["location"]["name"], "Belo Horizonte")
        self.assertIn("current", result)


    @patch('aula2.requests.get')
    def test_buscar_qualidade_ar_success(self, mock_get):
        # Mocking a successful API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": {"city": "Sao Paulo", "state": "Sao Paulo", "country": "Brazil"}}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = buscar_qualidade_ar("Sao Paulo", "Sao Paulo", "Brazil")
        self.assertIsNotNone(result)
        self.assertEqual(result["data"]["city"], "Sao Paulo")
        self.assertIn("data", result)

    @patch('aula2.requests.get')
    def test_buscar_dados_pais_success(self, mock_get):
        # Mocking a successful API response
        mock_response = MagicMock()
        mock_response.json.return_value = [{"name": {"common": "Brazil"}, "region": "Americas"}]
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = buscar_dados_pais("Brazil")
        self.assertIsNotNone(result)
        self.assertEqual(result[0]["name"]["common"], "Brazil")
        self.assertIn("region", result[0])

if __name__ == "__main__":
    unittest.main()