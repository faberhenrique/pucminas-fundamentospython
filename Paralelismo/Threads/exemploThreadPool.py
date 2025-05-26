import os
from concurrent.futures import ThreadPoolExecutor

import requests

WEATHER_KEY = os.getenv("WEATHER_KEY")


def consultar(cidade):
    r = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={cidade}"
    )
    return f"{cidade}: {r.json()['current']['temp_c']}°C"


cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Recife"]

with ThreadPoolExecutor() as executor:
    resultados = executor.map(consultar, cidades)

for resultado in resultados:
    print(resultado)


# ------------NOTAS AOS ALUNOS
# # ThreadPoollExecutor vs threading.Thread
# Com threading.Thread, você precisa:
# 	•	criar cada thread manualmente,
# 	•	passar os argumentos manualmente,
# 	•	gerenciar listas de threads,
# 	•	chamar .start() e .join() em cada uma.
# Com ThreadPoolExecutor, tudo isso é abstraído:
# 	•	você apenas define a função e os dados,
# 	•	a execução paralela é gerenciada automaticamente.

#
# O módulo concurrent.futures oferece duas implementações com mesma interface:
# 	•	ThreadPoolExecutor (para I/O-bound)
# 	•	ProcessPoolExecutor (para CPU-bound)
# Ao usar ThreadPoolExecutor, você não precisa decidir manualmente quando
# criar ou destruir threads.
# •	Ele cuida de:
# •	quantas threads serão usadas (com base no max_workers),
# •	reuso de threads (economia de recursos),
# •	controle de finalização (com o with, garante que tudo será
#   fechado corretamente).

# Melhor tratamento de retorno e exceções
# 	•	Com ThreadPoolExecutor, você pode capturar o retorno de cada
# função de forma ordenada.
# 	•	Usando submit() e future.result(), também é possível tratar
# exceções individualmente, algo mais difícil com threading.Thread.

# É recomendada pela própria documentação do Python como forma
# preferencial de programar concorrência leve.
