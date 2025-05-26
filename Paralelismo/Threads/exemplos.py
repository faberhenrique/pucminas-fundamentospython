import os
import time

import requests

WEATHER_KEY = os.getenv("WEATHER_KEY")
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador"]


def consultar(cidade):
    r = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={cidade}"
    )
    dados = r.json()
    print(f"{cidade}: {dados['current']['temp_c']}°C")


inicio = time.time()
for cidade in cidades:
    consultar(cidade)
print("Tempo total:", time.time() - inicio)
