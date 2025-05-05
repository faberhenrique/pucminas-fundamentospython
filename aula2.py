import json
import os
from datetime import datetime, timedelta

import requests

# Chaves de API obtidas do ambiente
WEATHER_KEY = os.getenv("WEATHER_KEY")
AIRVISUAL_KEY = os.getenv("AIRVISUAL_KEY")


def buscar_clima(cidade):
    """
    Consulta o clima atual de uma cidade utilizando a WeatherAPI.

    Args:
        cidade (str): O nome da cidade para a qual o clima será consultado.

    Returns:
        dict | None: Dados do clima ou None se falhar.
    """
    try:
        resposta = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={cidade}"
        )
        resposta.raise_for_status()
        return resposta.json()
    except Exception as e:
        print(f"Erro ao buscar clima: {e}")
        return None


def buscar_qualidade_ar(cidade, estado, pais):
    """
    Consulta a qualidade do ar para uma cidade usando a AirVisual API.

    Args:
        cidade (str), estado (str), pais (str)

    Returns:
        dict | None: Dados da qualidade do ar ou None se falhar.
    """
    try:
        resposta = requests.get(
            f"http://api.airvisual.com/v2/city?city={cidade}&state={estado}&country={pais}&key={AIRVISUAL_KEY}"
        )
        resposta.raise_for_status()
        return resposta.json()
    except Exception as e:
        print(f"Erro ao buscar qualidade do ar: {e}")
        return None


def buscar_dados_pais(pais):
    """
    Consulta informações sobre um país utilizando a REST Countries API.

    Args:
        pais (str): Nome do país

    Returns:
        dict | None: Dados do país ou None se falhar.
    """
    try:
        resposta = requests.get(f"https://restcountries.com/v3.1/name/{pais}")
        resposta.raise_for_status()
        return resposta.json()
    except Exception as e:
        print(f"Erro ao buscar dados do país: {e}")
        return None


def forecast_cidade(cidade, data):
    """
    Consulta a previsão do tempo para uma cidade utilizando a WeatherAPI.

    Args:
        cidade (str): O nome da cidade para a qual a previsão será consultada.

    Returns:
        dict | None: Dados da previsão ou None se falhar.
    """
    try:
        # Date between 14 days and 300 days from today in the future in yyyy-MM-dd format
        data_minima = datetime.today() + timedelta(days=14)
        data_maxima = datetime.today() + timedelta(days=300)
        data_formatada = datetime.strptime(data, "%Y-%m-%d")
        if not (data_minima <= data_formatada <= data_maxima):
            raise ValueError("A data deve estar entre 14 e 300 dias a partir de hoje.")
        resposta = requests.get(
            f"http://api.weatherapi.com/v1/future.json?key={WEATHER_KEY}&q={cidade}&dt={data_formatada}"
        )
        resposta.raise_for_status()
        return resposta.json()
    except Exception as e:
        print(f"Erro ao buscar previsão do tempo: {e}")
        return None


def listar_paises_dados_qualidade_ar():
    """Lista os países disponíveis na API de qualidade do ar."""
    try:
        resposta = requests.get(
            f"http://api.airvisual.com/v2/countries?key={AIRVISUAL_KEY}"
        )
        resposta.raise_for_status()
        return resposta.json()
    except Exception as e:
        print(f"Erro ao listar países: {e}")
        return None


def listar_estado_dados_qualidade_ar(pais):
    """Lista os estados disponíveis em um país via AirVisual API."""
    try:
        resposta = requests.get(
            f"http://api.airvisual.com/v2/states?country={pais}&key={AIRVISUAL_KEY}"
        )
        resposta.raise_for_status()
        return resposta.json()
    except Exception as e:
        print(f"Erro ao listar estados: {e}")
        return None


def enriquecimento_dados_cidade(cidade):
    """
    Enriquecimento de dados: clima, país e qualidade do ar de uma cidade.

    Args:
        cidade (str): Nome da cidade

    Returns:
        dict | None: Dados enriquecidos ou None se falhar.
    """
    try:
        clima = buscar_clima(cidade)
        if not clima:
            raise ValueError("Não foi possível obter os dados climáticos.")

        pais = clima["location"]["country"]
        estado = clima["location"]["region"]

        dados_pais = buscar_dados_pais(pais)
        dados_ar = buscar_qualidade_ar(cidade, estado, pais)

        dados_enriquecidos = {
            "cidade": cidade,
            "clima": clima,
            "dadosPais": dados_pais,
            "dadosAr": dados_ar,
        }

        print(json.dumps(dados_enriquecidos, indent=4, ensure_ascii=False))
        return dados_enriquecidos
    except Exception as e:
        print(f"Erro ao enriquecer dados da cidade: {e}")
        return None


def persistir_dados(dados, nome_arquivo):
    """
    Persiste os dados em um arquivo JSON.

    Args:
        dados (dict): Dados a serem persistidos.
        nome_arquivo (str): Nome do arquivo onde os dados serão salvos.
    """
    try:
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"Dados persistidos em {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao persistir dados: {e}")


def carregar_dados(nome_arquivo):
    """
    Carrega os dados de um arquivo JSON.

    Args:
        nome_arquivo (str): Nome do arquivo de onde os dados serão carregados.

    Returns:
        dict | None: Dados carregados ou None se falhar.
    """
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None


def cargaInicial():
    dados = enriquecimento_dados_cidade("Belo Horizonte")
    persistir_dados(dados, "dados_cidade.json")


def main():
    # print("Enriquecendo dados da cidade 'Capanema':\n")
    # enriquecimento_dados_cidade("Capanema")

    # print("\n--- Testes adicionais ---\n")
    # cidade = input("Digite o nome de outra cidade para consultar o clima: ")
    # clima = buscar_clima(cidade)
    # if clima:
    #     print(json.dumps(clima, indent=4, ensure_ascii=False))

    # ar = buscar_qualidade_ar("São Paulo", "São Paulo", "Brazil")
    # if ar:
    #     print("\nQualidade do ar em São Paulo:")
    #     print(json.dumps(ar, indent=4, ensure_ascii=False))

    # pais = buscar_dados_pais("Brazil")
    # if pais:
    #     print("\nDados do país Brazil:")
    #     print(json.dumps(pais, indent=4, ensure_ascii=False))
    # cargaInicial()
    forecast = forecast_cidade("Angra dos Reis", "2025-05-20")
    print(json.dumps(forecast, indent=4, ensure_ascii=False))
    persistir_dados(forecast, "dados_forecastAula.json")

    # forecast_cidade("Capanema", "2024-01-02")
    # forecast_cidade("Capanema", "2024-01-03")
    # forecast_cidade("Capanema", "2024-01-04")
    # forecast_cidade("Capanema", "2024-01-05")
    # forecast_cidade("Capanema", "2024-01-06")
    # forecast_cidade("Capanema", "2024-01-07")


if __name__ == "__main__":
    main()
