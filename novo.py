import requests
import os
import json


WEATHER_KEY = os.getenv("WEATHER_KEY")
AIRVISUAL_KEY = os.getenv("AIRVISUAL_KEY")

def buscar_clima(cidade):
   
    try:
        resposta = requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={cidade}')
        resposta.raise_for_status()  # Levanta um erro se a requisição falhar
        return resposta.json()  # Retorna os dados da resposta em formato JSON
    except Exception as e:
        print(f"Erro ao buscar clima: {e}")
        return None

def listar_paises_dados_qualidade_ar():
   
    try:
        resposta = requests.get(f"http://api.airvisual.com/v2/countries?key={AIRVISUAL_KEY}")
        resposta.raise_for_status()  # Levanta um erro se a requisição falhar
        return resposta.json()  # Retorna os dados da resposta em formato JSON
    except Exception as e:
        print(f"Erro ao buscar dados de qualidade do ar: {e}")
        return None
    

def listar_estado_dados_qualidade_ar(pais):
  
    try:
        resposta = requests.get(f"http://api.airvisual.com/v2/states?country={pais}&key={AIRVISUAL_KEY}")
        resposta.raise_for_status()  # Levanta um erro se a requisição falhar
        return resposta.json()  # Retorna os dados da resposta em formato JSON
    except Exception as e:
        print(f"Erro ao buscar dados de qualidade do ar: {e}")
        return None

def buscar_qualidade_ar(cidade, estado, pais):
    try:
        reposta = requests.get(f'http://api.airvisual.com/v2/city?city={cidade}&state={estado}&country={pais}&key={AIRVISUAL_KEY}')
        reposta.raise_for_status()  # Levanta um erro se a requisição falhar
        return reposta.json()  # Retorna os dados da resposta em formato JSON
    except Exception as e:
        print(f"Erro ao buscar qualidade do ar: {e}")
        return None

def lista_info_pelo_nome (pais):

    try:
        resposta = requests.get(f'https://restcountries.com/v3.1/name/{pais}')
        resposta.raise_for_status()  # Levanta um erro se a requisição falhar
        return resposta.json()  # Retorna os dados da resposta em formato JSON
    except Exception as e:
        print(f"Erro ao buscar dados de qualidade do ar: {e}")
        return None


def enriquecimento_dados_cidade(cidade):
    try:
        clima = buscar_clima(cidade)
        pais = clima["location"]["country"]
        estado = clima["location"]["region"]
        dadosPais = lista_info_pelo_nome(pais)
        dadosAr = buscar_qualidade_ar(cidade, estado, pais)
        dadosEnriquecidos = {
            "cidade": cidade,
            "clima": clima,
            "dadosPais": dadosPais,
            "dadosAr": dadosAr,
        }
        print(json.dumps(dadosEnriquecidos, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Erro ao buscar dados de qualidade do ar: {e}")
        return None

#print(json.dumps(buscar_clima("New York"), indent=4, ensure_ascii=False))


enriquecimento_dados_cidade("Capanema")