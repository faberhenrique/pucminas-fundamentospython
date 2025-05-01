def ex1():
    """
    This function prompts the user to input a number and determines whether the number is prime.

    It uses the helper function `is_prime` to check if the input number is a prime number.
    The result is printed to the console, indicating whether the number is prime or not.

    Steps:
    1. Prompts the user to input an integer.
    2. Calls the `is_prime` function to evaluate the primality of the number.
    3. Prints the result to the console.

    Note:
    The `is_prime` function must be defined elsewhere in the code for this function to work correctly.
    """
    # Crie uma função que receba um número e diga se ele é primo.
    print("Ex1:Crie uma função que receba um número e diga se ele é primo.")
    num = int(input("Digite um número: "))
    if is_prime(num):
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")


def is_prime(num):
    """
    Determine whether a given number is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors
    other than 1 and itself.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def ex2():

    # Implemente uma função que retorne o fatorial de um número.
    print("EX2:Implemente uma função que retorne o fatorial de um número.")
    num = int(input("Digite um número: "))
    print(f"O fatorial de {num} é {fatorial(num)}.")


def fatorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    The factorial of a number n is defined as:
    - n! = 1, if n is 0 or 1
    - n! = n * (n-1)!, if n > 1

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number.

    Raises:
    ValueError: If n is a negative integer.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


def ex3():

    # Crie uma função que receba uma lista de números e retorne a média.

    print("EX3:Crie uma função que receba uma lista de números e retorne a média.")
    lista = [1, 2, 3, 4, 5]
    print(f"A média da lista {lista} é {media(lista)}.")


def media(lista):
    """
    Calculates the arithmetic mean of a list of numbers.

    Args:
        lista (list): A list of numerical values.

    Returns:
        float: The arithmetic mean of the numbers in the list.
               Returns 0 if the list is empty.
    """
    if len(lista) == 0:
        return 0
    else:
        return sum(lista) / len(lista)


def ex4():

    # Escreva uma função que receba uma string e retorne se ela é um palíndromo.
    print(
        "EX4:Escreva uma função que receba uma string e retorne se ela é um palíndromo."
    )
    string = input("Digite uma string: ")
    if is_palindrome(string):
        print(f"{string} é um palíndromo.")
    else:
        print(f"{string} não é um palíndromo.")


def is_palindrome(s):
    """
    Checks if a given string is a palindrome.

    A palindrome is a word, phrase, or sequence that reads the same backward as forward,
    ignoring case and spaces.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]  # Verifica se a string é igual à sua reversa


def ex5():

    # Crie uma função que receba uma lista e retorne apenas os elementos pares.

    print(
        "EX5:Crie uma função que receba uma lista e retorne apenas os elementos pares."
    )
    lista = [1, 2, 3, 4, 5, 6]
    print(f"Os elementos pares da lista {lista} são {filtrar_pares(lista)}.")


def filtrar_pares(lista):
    """
    Filtra os números pares de uma lista.

    Esta função recebe uma lista de números inteiros e retorna uma nova lista contendo
    apenas os números pares presentes na lista original.

    Args:
        lista (list): Uma lista de números inteiros.

    Returns:
        list: Uma nova lista contendo apenas os números pares da lista original.
    """
    return [x for x in lista if x % 2 == 0]  # Filtra os elementos pares da lista
    # Retorna uma nova lista com os elementos pares


def ex6():

    # Implemente uma função que calcule a área de figuras geométricas (círculo, quadrado, triângulo).

    print(
        "EX6:Implemente uma função que calcule a área de figuras geométricas (círculo, quadrado, triângulo)."
    )
    area = area_figura("círculo", 5)
    print(f"A área do círculo é {area}.")
    area = area_figura("quadrado", 4)
    print(f"A área do quadrado é {area}.")
    area = area_figura("triângulo", 3, 4)
    print(f"A área do triângulo é {area}.")


def area_figura(forma, *args):
    """
    Calcula a área de uma figura geométrica específica.

    Parâmetros:
        forma (str): O tipo de figura geométrica. Pode ser "círculo", "quadrado" ou "triângulo".
        *args: Os parâmetros necessários para calcular a área da figura:
            - Para "círculo": fornecer o raio (float ou int).
            - Para "quadrado": fornecer o lado (float ou int).
            - Para "triângulo": fornecer a base e a altura (float ou int).

    Retorna:
        float: A área da figura geométrica especificada.
        None: Se a forma fornecida for inválida.
    """
    if forma == "círculo":
        raio = args[0]
        return 3.14 * (raio**2)  # Área do círculo
    elif forma == "quadrado":
        lado = args[0]
        return lado**2  # Área do quadrado
    elif forma == "triângulo":
        base, altura = args
        return (base * altura) / 2  # Área do triângulo
    else:
        return None  # Forma inválida


def ex7():

    # Crie uma função que receba uma data `dd/mm/aaaa` e retorne quantos dias se passaram desde o início do ano.

    print(
        "EX7:Crie uma função que receba uma data `dd/mm/aaaa` e retorne quantos dias se passaram desde o início do ano."
    )
    data = input("Digite uma data no formato dd/mm/aaaa: ")
    calculate_days_passed(data)


def calculate_days_passed(data):
    """
    Calculate the number of days that have passed since the beginning of the year
    for a given date in the format "DD/MM/YYYY".

    Args:
        data (str): A string representing the date in the format "DD/MM/YYYY".

    Returns:
        int: The number of days that have passed since the start of the year.

    Notes:
        - The function accounts for leap years when calculating the number of days.
        - Leap years are determined by the following rules:
          * A year is a leap year if it is divisible by 4 and not divisible by 100,
            or if it is divisible by 400.
    """
    dia, mes, ano = map(int, data.split("/"))
    dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias_no_mes[1] = 29  # Ano bissexto
    dias_passados = sum(dias_no_mes[: mes - 1]) + dia
    print(f"Desde o início do ano, passaram-se {dias_passados} dias.")
    # Retorna o número de dias passados desde o início do ano


def ex8():

    # Simule uma calculadora com funções para cada operação básica.
    print("EX8:Simule uma calculadora com funções para cada operação básica.")
    op = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = calculadora(op, num1, num2)
    if resultado is not None:
        print(f"O resultado da {op} é: {resultado}")
    else:
        print("Operação inválida.")


def calculadora(op, num1, num2):
    """
    Realiza uma operação matemática entre dois números.

    Parâmetros:
    op (str): A operação a ser realizada. Pode ser "soma", "subtracao", "multiplicacao" ou "divisao".
    num1 (float): O primeiro número.
    num2 (float): O segundo número.

    Retorna:
    float: O resultado da operação matemática.
    None: Caso a operação fornecida seja inválida.

    Exemplo:
    >>> calculadora("soma", 5, 3)
    8
    >>> calculadora("divisao", 10, 2)
    5.0
    """
    if op == "soma":
        return num1 + num2
    elif op == "subtracao":
        return num1 - num2
    elif op == "multiplicacao":
        return num1 * num2
    elif op == "divisao":
        return num1 / num2
    else:
        return None  # Operação inválida


def ex9():

    # Leia nomes em uma lista e exiba-os em ordem alfabética.

    print("EX9:Leia nomes em uma lista e exiba-os em ordem alfabética.")
    nomes = ["Carlos", "Ana", "Bruno", "Diana"]
    exibir_nomes_ordenados(nomes)


def exibir_nomes_ordenados(nomes):
    """
    Ordena e exibe uma lista de nomes em ordem alfabética.

    Args:
        nomes (list of str): Lista de nomes a ser ordenada e exibida.

    Returns:
        None: Esta função não retorna nenhum valor, apenas exibe os nomes ordenados.
    """
    nomes.sort()  # Ordena a lista em ordem alfabética
    print("Nomes em ordem alfabética:")
    for nome in nomes:
        print(nome)  # Exibe os nomes em ordem alfabética


def ex10():

    # Crie uma função que converta um número decimal para binário (sem usar `bin()`).

    print(
        "EX10:Crie uma função que converta um número decimal para binário (sem usar `bin()`)."
    )
    num = int(input("Digite um número decimal: "))
    binario = decimal_para_binario(num)
    print(f"O número {num} em binário é: {binario}")


def decimal_para_binario(num):
    """
    Converte um número decimal para sua representação binária.

    Args:
        num (int): O número decimal a ser convertido.

    Returns:
        str: A representação binária do número como uma string.
             Retorna "0" se o número fornecido for 0.

    Exemplo:
        >>> decimal_para_binario(10)
        '1010'
        >>> decimal_para_binario(0)
        '0'
    """
    if num == 0:
        return "0"
    binario = ""
    while num > 0:
        binario = str(num % 2) + binario
        num //= 2
    return binario  # Retorna o número em binário como uma string


def ex11():

    # Conte quantas vogais existem em um texto digitado.

    print("EX11:Conte quantas vogais existem em um texto digitado.")
    texto = input("Digite um texto: ")
    vogais = contar_vogais(texto)
    print(f"O texto contém {vogais} vogais.")


def contar_vogais(texto):
    """
    Conta o número de vogais em uma string fornecida.

    Args:
        texto (str): A string na qual as vogais serão contadas.

    Returns:
        int: O número de vogais encontradas na string.
    """
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador  # Retorna o número de vogais encontradas no texto


def ex12():

    # Transforme duas listas em um dicionário (chaves e valores).

    print("EX12:Transforme duas listas em um dicionário (chaves e valores).")
    chaves = ["nome", "idade", "cidade"]
    valores = ["Carlos", 30, "São Paulo"]
    dicionario = criar_dicionario(chaves, valores)
    print(dicionario)


def criar_dicionario(chaves, valores):
    """
    Cria um dicionário a partir de duas listas: uma de chaves e outra de valores.

    Args:
        chaves (list): Lista contendo as chaves do dicionário.
        valores (list): Lista contendo os valores correspondentes às chaves.

    Returns:
        dict: Um dicionário onde cada chave da lista `chaves` está associada ao
        valor correspondente na lista `valores`.

    Raises:
        ValueError: Se as listas `chaves` e `valores` não tiverem o mesmo tamanho.
    """
    if len(chaves) != len(valores):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    dicionario = {}
    for i in range(len(chaves)):
        dicionario[chaves[i]] = valores[i]
    return dicionario  # Retorna o dicionário criado a partir das listas


def ex13():

    # Crie uma lista de dicionários representando produtos (nome, preço, estoque).

    print(
        "EX13:Crie uma lista de dicionários representando produtos (nome, preço, estoque)."
    )
    produtos = [
        {"nome": "Produto A", "preco": 10.0, "estoque": 5},
        {"nome": "Produto B", "preco": 20.0, "estoque": 10},
        {"nome": "Produto C", "preco": 15.0, "estoque": 8},
    ]
    for produto in produtos:
        print(
            f"Nome: {produto['nome']}, Preço: {produto['preco']}, Estoque: {produto['estoque']}"
        )


def ex14():

    # Verifique se um arquivo existe no diretório atual usando `os.path.exists()`.

    print(
        "EX14:Verifique se um arquivo existe no diretório atual usando `os.path.exists()`."
    )
    import os

    arquivo = input("Digite o nome do arquivo: ")
    if os.path.exists(arquivo):
        print(f"O arquivo '{arquivo}' existe.")
    else:
        print(f"O arquivo '{arquivo}' não existe.")


def ex15():
    """
    Implements a registration system using a dictionary to store user information.

    The function allows users to input their name, age, and city, and stores this
    information in a dictionary. The registration process continues until the user
    types 'sair' to exit. Once the registration is complete, the function displays
    all registered users and their details.

    The dictionary structure is as follows:
    {
        "name": {
            "idade": int,
            "cidade": str
        }
    }

    Steps:
    1. Prompt the user to enter their name, age, and city.
    2. Store the information in a dictionary with the name as the key.
    3. Allow the user to exit the registration process by typing 'sair'.
    4. Display all registered users and their details after exiting.

    Note:
    - The function assumes that the user inputs valid data for age (integer).
    - The input for 'nome' is case-insensitive when checking for the exit condition.

    Example:
        Input:
            Digite o nome (ou 'sair' para encerrar): John
            Digite a idade: 25
            Digite a cidade: New York
            Digite o nome (ou 'sair' para encerrar): sair
        Output:
            Cadastro de John realizado com sucesso!
            Cadastro encerrado.
            Nome: John, Idade: 25, Cidade: New York
    """

    # Implemente um sistema de cadastro com dicionário: nome, idade e cidade.

    print(
        "EX15:Implemente um sistema de cadastro com dicionário: nome, idade e cidade."
    )
    cadastro = {}
    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        idade = int(input("Digite a idade: "))
        cidade = input("Digite a cidade: ")
        cadastro[nome] = {"idade": idade, "cidade": cidade}
        print(f"Cadastro de {nome} realizado com sucesso!")
    print("Cadastro encerrado.")
    for nome, info in cadastro.items():
        print(f"Nome: {nome}, Idade: {info['idade']}, Cidade: {info['cidade']}")
