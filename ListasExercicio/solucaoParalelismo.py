"""
Crawler de APIs concorrente com Threading
Simula a coleta de dados de 10 cidades em uma API pública de clima usando threading.Thread.
"""

import os
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import requests

# Lista de cidades para consulta
cidades = [
    "Mendes",
    "da Rosa dos Dourados",
    "Duarte do Oeste",
    "Nunes do Campo",
    "Almeida da Prata",
    "da Cunha dos Dourados",
    "Fernandes Alegre",
    "Moraes do Galho",
    "Porto do Oeste",
    "da Mota do Oeste",
    "Souza do Sul",
    "Campos do Campo",
    "Monteiro Verde",
    "da Luz da Mata",
    "Monteiro de da Mata",
    "Jesus do Campo",
    "Carvalho do Oeste",
    "Dias de Moura",
    "Nascimento da Prata",
    "Freitas da Mata",
    "Souza de Monteiro",
    "Souza de Martins",
    "Pires do Galho",
    "Monteiro da Prata",
    "Souza do Campo",
    "Monteiro",
    "Nascimento",
    "Monteiro dos Dourados",
    "Barros da Serra",
    "Nascimento de Gonçalves",
    "da Cunha de Moreira",
    "Almeida Grande",
    "Pinto de Moura",
    "Silva da Prata",
    "Fogaça",
    "Barbosa Verde",
    "Rocha dos Dourados",
    "Viana de Minas",
    "Rezende da Serra",
    "da Cunha de Minas",
    "Martins do Sul",
    "Freitas de Sales",
    "Lopes das Pedras",
    "Oliveira de Dias",
    "Correia Verde",
    "Fogaça do Oeste",
    "Souza de Ferreira",
    "Alves",
    "Ramos Grande",
    "Cardoso do Galho",
    "da Costa de Gonçalves",
    "Pinto Verde",
    "da Rosa de Cavalcanti",
    "Rocha da Praia",
    "Nogueira de Nogueira",
    "da Rosa de Rocha",
    "Mendes de Moreira",
    "Freitas de Pinto",
    "da Paz",
    "Duarte de Caldeira",
    "Campos das Flores",
    "Cardoso da Praia",
    "da Rosa Paulista",
    "da Luz de Fogaça",
    "Nogueira de da Mata",
    "Monteiro da Serra",
    "Castro do Campo",
    "Peixoto de Ribeiro",
    "Peixoto de Martins",
    "Sales dos Dourados",
    "Vieira de da Mata",
    "Peixoto dos Dourados",
    "Pires",
    "Jesus",
    "da Conceição do Sul",
    "Teixeira da Praia",
    "Ribeiro de da Costa",
    "Barbosa de Porto",
    "Melo de Freitas",
    "Ramos das Pedras",
    "Fogaça do Campo",
    "Carvalho do Galho",
    "da Luz do Norte",
    "da Conceição de Moura",
    "Moraes de Duarte",
    "Silveira Grande",
    "da Mota do Galho",
    "Mendes de Barros",
    "Monteiro Alegre",
    "Souza",
    "Martins Verde",
    "Fernandes Grande",
    "Rocha do Campo",
    "Barbosa de Caldeira",
    "Fogaça de da Rosa",
    "Campos de Campos",
    "Almeida",
    "Cunha da Serra",
    "Moraes",
    "Rezende do Galho",
    "Costa de Martins",
    "Barbosa de Almeida",
    "Correia",
    "da Mota de Goiás",
    "da Conceição da Mata",
    "Fernandes",
    "Moraes do Amparo",
    "Souza de Pinto",
    "Almeida das Pedras",
    "Lima do Norte",
    "Vieira da Mata",
    "Vieira da Praia",
    "Sales de Nunes",
    "da Mota",
    "da Conceição de Silva",
    "Cunha do Amparo",
    "Ribeiro de Rocha",
    "Vieira de Campos",
    "Pereira do Oeste",
    "Cavalcanti de Nascimento",
    "Correia das Flores",
    "Campos Verde",
    "Souza Grande",
    "Costa de Ribeiro",
    "Cavalcanti do Norte",
    "Caldeira",
    "Fogaça do Galho",
    "Mendes de da Rocha",
    "Cavalcanti de Ramos",
    "Gomes da Praia",
    "Vieira Alegre",
    "Freitas do Galho",
    "Santos do Amparo",
    "Nunes Grande",
    "Peixoto Paulista",
    "da Conceição do Oeste",
    "Costa",
    "Lima Grande",
    "Cavalcanti de Minas",
    "Ferreira Verde",
    "Almeida de da Cunha",
    "Monteiro da Praia",
    "da Rocha Grande",
    "da Mata",
    "da Cruz de Duarte",
    "da Conceição de da Mata",
    "Vieira da Prata",
    "Farias das Flores",
    "Gonçalves das Flores",
    "da Rosa da Mata",
    "da Cruz",
    "Oliveira",
    "Cunha do Campo",
    "Vieira do Campo",
    "Pinto",
    "Vieira",
    "da Rosa do Campo",
    "Monteiro Paulista",
    "Viana de Cunha",
    "Cunha",
    "Oliveira do Galho",
    "Pinto de Peixoto",
    "Moreira",
    "das Neves das Pedras",
    "Costa Grande",
    "Santos",
    "da Mota de Freitas",
    "Fernandes do Oeste",
    "Azevedo das Pedras",
    "Porto da Mata",
    "Santos do Norte",
    "da Rosa de Azevedo",
    "Melo",
    "Almeida da Mata",
    "Freitas de Goiás",
    "Correia dos Dourados",
    "Gomes Paulista",
    "Farias",
    "Ribeiro de Viana",
    "Ramos de Goiás",
    "Ferreira",
    "Nogueira dos Dourados",
    "Silveira Paulista",
    "Carvalho das Flores",
    "Moura Paulista",
    "Porto da Serra",
    "Freitas Paulista",
    "Monteiro de Azevedo",
    "Pereira da Prata",
    "Nogueira Alegre",
    "Rodrigues dos Dourados",
    "Castro de Minas",
    "Sales da Mata",
    "Melo do Galho",
    "da Paz de Rocha",
    "da Rocha",
    "Silveira das Flores",
    "Azevedo de da Mota",
    "Costa Paulista",
    "da Costa do Amparo",
    "Cunha Grande",
    "Peixoto do Campo",
    "Nogueira do Norte",
    "Rodrigues de Vieira",
    "da Paz do Sul",
    "Cunha das Pedras",
    "Ribeiro Grande",
    "Silva da Praia",
    "da Mata Paulista",
    "Lopes da Serra",
    "Silveira de Goiás",
    "Cardoso da Prata",
    "Monteiro de Silva",
    "Melo da Prata",
    "Caldeira de Goiás",
    "Moraes da Prata",
    "Silveira dos Dourados",
    "Pereira das Flores",
    "Lima de Minas",
    "Santos Verde",
    "Rezende de Aragão",
    "Peixoto da Praia",
    "Nunes do Galho",
    "da Rosa de Peixoto",
    "Moreira da Prata",
    "Costa de Peixoto",
    "da Costa Alegre",
    "da Cunha de Campos",
    "Cunha do Galho",
    "da Luz Verde",
    "Duarte da Praia",
    "Pinto de Nogueira",
    "Silva do Amparo",
    "Rodrigues de Nascimento",
    "Silva de Minas",
    "da Costa da Serra",
    "Monteiro de Caldeira",
    "Almeida Alegre",
    "Rezende de da Cunha",
    "Correia de Gomes",
    "Moura do Norte",
    "Fogaça das Pedras",
    "Nascimento da Mata",
    "Fogaça de Vieira",
    "Souza da Serra",
    "Dias de Pinto",
    "Moraes de Lima",
    "Silva do Norte",
    "Rodrigues do Norte",
    "Moreira de da Conceição",
    "Silveira de Pereira",
    "Pereira da Praia",
    "Peixoto",
    "Vieira de Castro",
    "Oliveira da Mata",
    "da Rosa de Minas",
    "da Cunha Paulista",
    "da Rocha das Pedras",
    "Santos de Melo",
    "Ferreira da Mata",
    "Santos do Oeste",
    "Vieira das Flores",
    "Castro",
    "Azevedo",
    "Nogueira",
    "Barros",
    "Moraes das Flores",
    "Caldeira de Minas",
    "Lopes dos Dourados",
    "Barros do Norte",
    "Porto das Pedras",
    "Nunes das Flores",
    "Ribeiro",
    "Cunha de Duarte",
    "Jesus do Amparo",
    "Vieira dos Dourados",
    "Caldeira do Norte",
    "Costa da Mata",
    "Gonçalves de Cardoso",
    "Freitas do Sul",
    "Jesus de Nogueira",
    "Carvalho",
    "Ferreira dos Dourados",
    "Rodrigues",
    "da Conceição de Monteiro",
    "Nogueira de da Mota",
    "Oliveira da Prata",
    "Ribeiro de Teixeira",
    "Pires do Campo",
    "Moreira de da Costa",
    "Ramos do Amparo",
    "Azevedo do Oeste",
    "Pereira",
    "da Cruz das Flores",
    "Moraes do Campo",
    "Fogaça de Goiás",
    "Viana Verde",
    "da Conceição de Teixeira",
    "Teixeira",
    "Silveira de Santos",
    "da Conceição de Minas",
    "Campos Paulista",
    "Caldeira do Amparo",
    "Lima do Amparo",
    "Castro de Martins",
    "Cunha de Minas",
    "Rocha",
    "da Luz",
    "Lima",
    "Duarte",
    "Jesus de Viana",
    "Caldeira das Pedras",
    "Dias de Nunes",
    "Sales da Serra",
    "Castro da Praia",
    "Gonçalves",
    "Moraes Verde",
    "Cunha da Mata",
    "Sales do Campo",
    "da Costa",
    "Vieira de Lima",
    "Sales do Galho",
    "Vieira do Galho",
    "das Neves",
    "Nunes de Dias",
    "Souza da Mata",
    "Aragão de da Rocha",
    "Caldeira Verde",
    "Nascimento do Norte",
    "Almeida da Praia",
    "Martins das Flores",
    "Viana das Flores",
    "Castro de Rezende",
    "Lima de Goiás",
    "Cavalcanti",
    "das Neves do Amparo",
    "da Mata de Moreira",
    "Rocha da Prata",
    "Correia da Mata",
    "Oliveira de Cardoso",
    "Cavalcanti Paulista",
    "Oliveira de Gomes",
    "da Rosa de da Mota",
    "Silva do Oeste",
    "Nunes",
    "Lima de Santos",
    "Jesus da Prata",
    "Fernandes Paulista",
    "Novaes",
    "Barros de Barbosa",
    "Oliveira do Sul",
    "Duarte Alegre",
    "Farias de Cardoso",
    "Moura das Pedras",
    "Nunes da Serra",
    "Moreira Verde",
    "Araújo das Flores",
    "Gomes",
    "Novaes de Fernandes",
    "Silveira da Serra",
    "Santos dos Dourados",
    "Silveira do Sul",
    "da Cunha da Praia",
    "Silva",
    "Gomes do Galho",
    "da Cunha de Silva",
    "Pereira do Galho",
    "Lopes Alegre",
    "Mendes da Praia",
    "Rezende de Ramos",
    "Monteiro do Galho",
    "Ramos de Martins",
    "Aragão do Campo",
    "Melo dos Dourados",
    "Cardoso de Carvalho",
    "Aragão dos Dourados",
    "Cardoso Grande",
    "Cardoso de Goiás",
    "Fernandes dos Dourados",
    "Melo do Campo",
    "Jesus de Ramos",
    "Ferreira de Pires",
    "da Paz de da Mota",
    "Viana",
    "Fogaça Alegre",
    "Santos Paulista",
    "Souza de Pereira",
    "da Mota do Norte",
    "Cardoso de Dias",
    "Moura",
    "Rocha Verde",
    "Souza de Farias",
    "Aragão",
    "da Rocha de Goiás",
    "Nunes do Oeste",
    "da Mata do Sul",
    "Pereira de Dias",
    "Duarte Grande",
    "Araújo Verde",
    "Moreira de Barros",
    "Gomes de Goiás",
    "Freitas de Viana",
    "Cardoso de Araújo",
    "da Mota do Sul",
    "da Rocha de Rodrigues",
    "Novaes do Amparo",
    "da Cruz da Prata",
    "Cavalcanti dos Dourados",
    "da Mata das Pedras",
    "Cardoso do Norte",
    "Azevedo do Sul",
    "Nascimento de Lopes",
    "Gonçalves do Galho",
    "Peixoto da Prata",
    "Nascimento de Silva",
    "da Cunha de Carvalho",
    "Dias de Rodrigues",
    "Martins",
    "Barbosa Alegre",
    "da Cunha",
    "Correia Grande",
    "da Mota de Viana",
    "Cavalcanti Verde",
    "Pinto do Campo",
    "Teixeira Paulista",
    "Nunes da Prata",
    "Ferreira do Norte",
    "Campos do Amparo",
    "da Rocha do Norte",
    "Gomes de da Cunha",
    "Almeida de Almeida",
    "Barbosa de Costela",
    "Correia de Silveira",
    "Barbosa Grande",
    "Monteiro do Oeste",
    "Gomes Alegre",
    "Dias",
    "Freitas",
    "Duarte da Serra",
    "Nascimento Verde",
    "Lopes da Mata",
    "Barbosa",
    "Cardoso",
    "Sales",
    "Silveira",
    "Gomes de da Rocha",
    "Moura de Goiás",
    "da Rosa",
    "da Cunha da Serra",
    "da Mata do Amparo",
    "da Cruz do Campo",
    "Lima da Prata",
    "da Rocha da Praia",
    "Costa das Flores",
    "Farias do Amparo",
    "Costela de Goiás",
    "da Cruz de Moraes",
    "da Costa de Goiás",
    "Cardoso de Rezende",
    "da Mata de Costa",
    "Rodrigues da Serra",
    "Costela do Sul",
    "Costela do Oeste",
    "da Luz do Galho",
    "Cardoso do Amparo",
    "Campos",
    "Alves de Minas",
    "Porto",
    "Moreira dos Dourados",
    "Ferreira da Praia",
    "Lima de Vieira",
    "Cardoso de Campos",
    "Sales Verde",
    "Rodrigues de Rocha",
    "Sales das Pedras",
    "Ribeiro de Moraes",
    "Lima Paulista",
    "Carvalho da Praia",
    "Duarte do Amparo",
    "Nascimento Alegre",
    "Moura do Campo",
    "Cardoso Verde",
    "Rezende",
    "Melo da Mata",
    "Cavalcanti da Mata",
    "da Conceição",
    "Ribeiro de da Rocha",
    "Nascimento de Rocha",
    "da Luz de Dias",
    "Oliveira do Norte",
    "Nascimento das Pedras",
    "Araújo",
    "da Luz de Pereira",
    "da Conceição do Campo",
    "Rocha de Melo",
    "Santos de Dias",
    "da Rosa Verde",
    "Ramos",
    "da Rocha dos Dourados",
    "Freitas de Cunha",
]

WEATHER_KEY = os.getenv("WEATHER_KEY")
URL_BASE = "http://api.weatherapi.com/v1/current.json"


def consultar_clima(cidade):
    try:
        print(f"Iniciando consulta para {cidade}")
        response = requests.get(URL_BASE, params={"key": WEATHER_KEY, "q": cidade})
        data = response.json()
        temp = data["current"]["temp_c"]
        print(f"{cidade}: {temp}°C")
    except Exception as e:
        print(f"Erro ao consultar {cidade}: {e}")


def ex1():
    inicio = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(consultar_clima, cidades)

    print("Consulta finalizada em {:.2f} segundos".format(time.time() - inicio))


################################### EXERCÍCIO 2 ###################################

# Lista de arquivos (simulando múltiplos .csv pequenos)
arquivos = [f"copia_{i}.csv" for i in range(10)]


# Garante que os arquivos existem (simulando com base no 50k.csv)
def preparar_arquivos_base():
    if not os.path.exists("50k.csv"):
        raise FileNotFoundError("O arquivo 50k.csv não foi encontrado.")
    for nome in arquivos:
        if not os.path.exists(nome):
            with open("50k.csv", "r") as origem, open(nome, "w") as destino:
                destino.write(origem.read())


# Função de leitura com Pandas
def ler_csv(path):
    df = pd.read_csv(path)
    print(f"{path}: {len(df)} linhas")


# Execução concorrente
def ex2():
    preparar_arquivos_base()
    inicio = time.time()

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(ler_csv, arquivos)

    print(f"Ingestão concorrente concluída em {time.time() - inicio:.2f} segundos.")


########### EXERCICIO 3 ###########

# Lista de URLs para testar
urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.python.org",
    "https://www.microsoft.com",
    "https://www.reddit.com",
    "https://www.wikipedia.org",
    "https://www.linkedin.com",
    "https://www.amazon.com",
    "https://www.apple.com",
]


# Função para testar uma URL
def testar_url(url):
    inicio = time.time()
    try:
        resposta = requests.get(url, timeout=5)
        duracao = time.time() - inicio
        return {
            "url": url,
            "status": resposta.status_code,
            "tempo_resposta_s": round(duracao, 3),
        }
    except requests.RequestException as e:
        duracao = time.time() - inicio
        return {"url": url, "status": "Erro", "tempo_resposta_s": round(duracao, 3)}


# Execução concorrente e salvamento em CSV
def ex3():
    with ThreadPoolExecutor(max_workers=5) as executor:
        resultados = list(executor.map(testar_url, urls))

    df = pd.DataFrame(resultados)
    df.to_csv("resultados.csv", index=False)
    print("Resultados salvos em resultados.csv")


#### EXERCÍCIO 4 - Simulação de download concorrente #####


# Lista simulada de arquivos
arquivos = [f"arquivo_{i}.zip" for i in range(10)]


# Função que simula o download de um arquivo
def simular_download(nome_arquivo):
    print(f"Iniciando download de {nome_arquivo}...")
    time.sleep(2)  # Simula o tempo de download de um arquivo grande
    print(f"Download concluído: {nome_arquivo}")


# Execução concorrente
def ex4():
    inicio = time.time()

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(simular_download, arquivos)

    duracao = time.time() - inicio
    print(f"Todos os downloads concluídos em {duracao:.2f} segundos.")


############# EXERCÍCIO 5 - Consulta Banco com ThreadPoolExecutor #############

# Tabelas simuladas
tabelas = ["clientes", "pedidos", "produtos", "estoque", "vendas"]


# Função que simula conexão e leitura de uma tabela
def ler_tabela(nome_tabela):
    print(f"[{nome_tabela}] Conectando ao banco...")
    time.sleep(random.uniform(1, 2))  # Simula tempo de conexão e leitura
    registros = random.randint(100, 1000)
    colunas = random.randint(4, 10)
    print(
        f"[{nome_tabela}] Leitura concluída: {registros} registros, {colunas} colunas"
    )


# Execução com threads
def ex5():
    threads = []

    for tabela in tabelas:
        t = threading.Thread(target=ler_tabela, args=(tabela,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Leitura de todas as tabelas concluída.")


if __name__ == "__main__":
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
