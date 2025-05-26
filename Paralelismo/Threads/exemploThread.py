import os
import threading
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
threads = []

for cidade in cidades:
    t = threading.Thread(
        target=consultar, args=(cidade,)
    )  # create a thread for each city
    threads.append(t)  # adiciona a thread à lista
    t.start()  # Inicia a thread para cada cidade

for t in threads:
    t.join()  #  Espera todas as threads terminarem

print("Tempo total:", time.time() - inicio)
