import unittest
from io import StringIO
from unittest.mock import patch

import ListasExercicio.listaEx1 as listaEx1


class TestListaEx1(unittest.TestCase):

    @patch("builtins.input", side_effect=["John", "25"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_1(self, mock_stdout, mock_input):
        listaEx1.exec_1()
        self.assertIn("Hello, John! You are 25 years old.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["10", "5"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_2(self, mock_stdout, mock_input):
        listaEx1.exec_2()
        output = mock_stdout.getvalue()
        self.assertIn("Sum: 15.0", output)
        self.assertIn("Subtraction: 5.0", output)
        self.assertIn("Multiplication: 50.0", output)
        self.assertIn("Division: 2.0", output)

    @patch("builtins.input", side_effect=["4"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_3_even(self, mock_stdout, mock_input):
        listaEx1.exec_3()
        self.assertIn("4 is even.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["5"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_3_odd(self, mock_stdout, mock_input):
        listaEx1.exec_3()
        self.assertIn("5 is odd.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["10", "20"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_4(self, mock_stdout, mock_input):
        listaEx1.exec_4()
        self.assertIn("20.0 is greater than 10.0.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["5"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_5(self, mock_stdout, mock_input):
        listaEx1.exec_5()
        output = mock_stdout.getvalue()
        self.assertIn("5 x 1 = 5", output)
        self.assertIn("5 x 10 = 50", output)

    @patch("builtins.input", side_effect=["0"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_6(self, mock_stdout, mock_input):
        listaEx1.exec_6()
        self.assertIn("0.0°C is equal to 32.0°F.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["15"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_7(self, mock_stdout, mock_input):
        listaEx1.exec_7()
        self.assertIn("15 is a multiple of both 3 and 5.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["70", "1.75"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_8(self, mock_stdout, mock_input):
        listaEx1.exec_8()
        self.assertIn("Your IMC is 22.86.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["2020"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_9(self, mock_stdout, mock_input):
        listaEx1.exec_9()
        self.assertIn("2020 is a leap year.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["10", "20", "30"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_10(self, mock_stdout, mock_input):
        listaEx1.exec_10()
        self.assertIn("The largest number is 30.0.", mock_stdout.getvalue())
        self.assertIn("The smallest number is 10.0.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["1234"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_11(self, mock_stdout, mock_input):
        listaEx1.exec_11()
        self.assertNotIn("Incorrect password.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["7", "8", "9", "10"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_12(self, mock_stdout, mock_input):
        listaEx1.exec_12()
        self.assertIn("Passed with an average of 8.50.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["5"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_13(self, mock_stdout, mock_input):
        listaEx1.exec_13()
        self.assertIn("The sum from 1 to 5 is 15.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["1", "10"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_14(self, mock_stdout, mock_input):
        listaEx1.exec_14()
        self.assertIn(
            "There are 5 even numbers between 1 and 10.", mock_stdout.getvalue()
        )

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exec_15(self, mock_stdout, mock_input):
        listaEx1.exec_15()
        self.assertIn("1 3 5 7 9 11 13 15 17 19", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
