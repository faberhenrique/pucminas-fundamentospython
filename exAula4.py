#  Aula Prática – Integração entre PostgreSQL (Pagila) e APIs com Python

# Nesta atividade, você irá:
# - Consultar dados da base Pagila com `psycopg2`
# - Integrar dados climáticos e populacionais usando APIs externas
# - Analisar, transformar e visualizar os dados
# - Praticar o uso de Pandas, APIs, SQL e operações avançadas como `lambda`, `groupby`, `merge`, entre outras


import os

import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
import requests
import seaborn as sns
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# String de conexão
user = os.getenv("PG_USER")
password = os.getenv("PG_PASSWORD")
host = os.getenv("PG_HOST")
db = os.getenv("PG_DB")

engine = psycopg2.connect(f"postgresql://{user}:{password}@{host}/{db}?sslmode=require")


def run_query(sql, coon=engine):
    """
    Executes a SQL query on the provided database connection and returns the result as a DataFrame.

    Args:
        sql (str): The SQL query to be executed.
        coon (sqlalchemy.engine.base.Connection or sqlite3.Connection): The database connection object.

    Returns:
        pandas.DataFrame: A DataFrame containing the results of the SQL query.
    """
    return pd.read_sql_query(sql, coon)

## https://github.com/devrimgunduz/pagila/tree/master 


#   Exercício 1 – Temperatura Média das Capitais dos Clientes
# 	•	Recupere as cidades dos clientes com mais de 10 transações.
# 	•	Use a WeatherAPI para buscar a temperatura atual dessas cidades.
# 	•	Calcule a temperatura média ponderada por número de clientes.
# 	•	Insight esperado: quais cidades concentram clientes e temperaturas extremas?

# ⸻

#   Exercício 2 – Receita Bruta em Cidades com Clima Ameno
# 	•	Calcule a receita bruta por cidade.
# 	•	Use a WeatherAPI para consultar a temperatura atual.
# 	•	Filtre apenas cidades com temperatura entre 18°C e 24°C.
# 	•	Resultado: qual o faturamento total vindo dessas cidades?


# ⸻

#   Exercício 3 – Aluguel de Filmes por Região e População
# 	•	Identifique os países dos clientes com maior número de aluguéis.
# 	•	Use a REST Countries API para obter a população desses países.
# 	•	Calcule o número de aluguéis por 1.000 habitantes.
# 	•	Análise: quais países são mais “cinéfilos” proporcionalmente?

# ⸻

#   Exercício 4 – Filmes Mais Populares em Cidades Poluídas
# 	•	Liste as 10 cidades com maior número de clientes.
# 	•	Use a AirVisual API para consultar o AQI dessas cidades.
# 	•	Relacione os filmes mais alugados em cidades com AQI > 150.
# 	•	Discussão: poluição impacta preferências de filmes?

# ⸻

#   Exercício 5 – Clientes em Áreas Críticas
# 	•	Recupere os clientes com endereço em cidades com AQI acima de 130.
# 	•	Combine nome do cliente, cidade, país, temperatura e AQI.
# 	•	Classifique os clientes em “zona de atenção” com base nos critérios ambientais.

# ⸻

#   Exercício 6 – Receita por Continente
# 	•	Use a REST Countries API para mapear o continente de cada país.
# 	•	Agrupe a receita total por continente.
# 	•	Exiba os resultados em um gráfico de pizza com matplotlib.

# ⸻

#   Exercício 7 – Tempo Médio de Aluguel vs Clima
# 	•	Calcule o tempo médio de aluguel por cidade (entre rental_date e return_date).
# 	•	Combine com a temperatura atual dessas cidades.
# 	•	Visualize a correlação entre temperatura e tempo médio de aluguel (scatterplot + linha de tendência).

# ⸻

#   Exercício 8 – Perfil de Clima por Cliente
# 	•	Para cada cliente, crie um perfil com:
# 	•	cidade, temperatura, AQI, total de aluguéis, gasto total.
# 	•	Agrupe os perfis por faixa etária (simulada ou fictícia) e avalie padrões.
# 	•	Objetivo: conectar comportamento de consumo e ambiente.

# ⸻

#   Exercício 9 – Exportação Inteligente
# 	•	Gere um relatório Excel com os seguintes critérios:
# 	•	Clientes de países com temperatura < 15°C
# 	•	AQI acima de 100
# 	•	Receita individual > média geral
# 	•	Utilize OpenPyXL e organize em múltiplas abas: Clientes, Temperaturas, Alertas.

# ⸻

#   Exercício 10 – API Cache Inteligente (Desafio)
# 	•	Implemente uma lógica que salve os dados de clima e AQI localmente em CSV.
# 	•	Ao consultar novamente a mesma cidade, busque do CSV ao invés da API.
# 	•	Evite chamadas redundantes — bom para práticas de performance e economia de requisições.

