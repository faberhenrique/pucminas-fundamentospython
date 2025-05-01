import json
import os

import requests

WEATHER_KEY = os.getenv("WEATHER_KEY")
AIRVISUAL_KEY = os.getenv("AIRVISUAL_KEY")


def buscar_clima(cidade):
    """
    Consulta o clima atual de uma cidade utilizando a WeatherAPI.

    Args:
        cidade (str): O nome da cidade para a qual o clima será consultado.

    Returns:
        dict: Um dicionário contendo os dados do clima retornados pela API,
              caso a consulta seja bem-sucedida.
        None: Retorna None se ocorrer um erro durante a consulta.

    Raises:
        requests.exceptions.RequestException: Caso ocorra um erro na requisição HTTP.
    """
    """Consulta o clima atual de uma cidade na WeatherAPI."""
    try:
        resposta = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={cidade}"
        )
        resposta.raise_for_status()  # Levanta um erro se a requisição falhar
        return resposta.json()  # Retorna os dados da resposta em formato JSON
    except Exception as e:
        print(f"Erro ao buscar clima: {e}")
        return None


def buscar_qualidade_ar(cidade, estado, pais):
    """
    Consulta a qualidade do ar para uma cidade específica usando a AirVisual API.

    Args:
        cidade (str): O nome da cidade para a qual deseja consultar a qualidade do ar.
        estado (str): O estado ou província onde a cidade está localizada.
        pais (str): O país onde a cidade está localizada.

    Returns:
        dict: Um dicionário contendo os dados da qualidade do ar retornados pela API,
              caso a consulta seja bem-sucedida.
        None: Retorna None se ocorrer um erro durante a consulta.

    Raises:
        requests.exceptions.RequestException: Caso ocorra um erro na requisição HTTP.
    """
    """Consulta a qualidade do ar usando a AirVisual API."""
    try:
        reposta = requests.get(
            f"http://api.airvisual.com/v2/city?city={cidade}&state={estado}&country={pais}&key={AIRVISUAL_KEY}"
        )
        reposta.raise_for_status()  # Levanta um erro se a requisição falhar
        return reposta.json()  # Retorna os dados da resposta em formato JSON
    except Exception as e:
        print(f"Erro ao buscar qualidade do ar: {e}")
        return None


def buscar_dados_pais(pais):
    """
    Consulta informações sobre um país utilizando a REST Countries API.

    resposta_country = requests.get(url_country)
    resposta_country.raise_for_status()
    return resposta_country.json()

    Returns:
        dict: Um dicionário contendo os dados do país retornados pela API,
              caso a consulta seja bem-sucedida.
        None: Retorna None se ocorrer um erro durante a consulta.

    Raises:
        requests.exceptions.RequestException: Caso ocorra um erro na requisição HTTP.
    """
    try:
        resposta_country = requests.get(f"https://restcountries.com/v3.1/name/{pais}")
        resposta_country.raise_for_status()  # Levanta um erro se a requisição falhar
        return resposta_country.json()  # Retorna os dados da resposta em formato JSON
    except Exception as e:
        print(f"Erro ao buscar dados do país: {e}")
        return None


# Testando as funções
def testeFunctions(
    buscar_clima=buscar_clima,
    buscar_qualidade_ar=buscar_qualidade_ar,
    buscar_dados_pais=buscar_dados_pais,
):
    cidade = input("Digite o nome da cidade: ")
    clima = buscar_clima(cidade)
    if clima:
        print(f"Clima em {cidade}:")
        print(json.dumps(clima, indent=4, ensure_ascii=False))
    arQualidade = buscar_qualidade_ar("Sao Paulo", "Sao Paulo", "Brazil")
    if arQualidade:
        print("Qualidade do ar em São Paulo:")
        print(json.dumps(arQualidade, indent=4, ensure_ascii=False))
    dadosPais = buscar_dados_pais("Brazil")
    if dadosPais:
        print("Dados do país Brasil:")
        print(json.dumps(dadosPais, indent=4, ensure_ascii=False))


def main():
    testeFunctions()


if __name__ == "__main__":
    main()
