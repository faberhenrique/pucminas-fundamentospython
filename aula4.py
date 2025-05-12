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


def fetch_client_data():
    # Exemplo de query
    query_clientes = """
    SELECT c.customer_id, c.first_name, c.last_name, ci.city, co.country
    FROM customer c
    JOIN address a ON c.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
    """

    df_clientes = run_query(query_clientes)
    df_clientes.head()
    print(df_clientes.head())
    return df_clientes


def buscar_clima(cidade):
    api_key = os.getenv("WEATHER_KEY")
    try:
        url = "http://api.weatherapi.com/v1/current.json?" f"key={api_key}&q={cidade}"
        resposta = requests.get(url, timeout=10)
        return resposta.json()["current"]["temp_c"]
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None


def merge_client_weather(df_clientes):
    # Aplicar em uma amostra das cidades
    amostra = df_clientes["city"].drop_duplicates().head(5)
    df_clima = pd.DataFrame({"cidade": amostra})
    df_clima["temperatura"] = df_clima["cidade"].apply(buscar_clima)
    print(df_clima.head())
    # Exemplo de merge
    df_analise = df_clientes.merge(
        df_clima, how="left", left_on="city", right_on="cidade"
    )
    print(df_analise.head())
    return df_analise


def plot_temperature_distribution(df_analise):
    plt.figure(figsize=(10, 5))
    sns.histplot(data=df_analise, x="temperatura", bins=10, kde=True)
    plt.title("Distribuição da Temperatura nas Cidades dos Clientes")
    plt.show()


df_clientes = fetch_client_data()
df_analise = merge_client_weather(df_clientes)
plot_temperature_distribution(df_analise)
