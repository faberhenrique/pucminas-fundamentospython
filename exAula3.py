
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Suponha que você já tenha o DataFrame `df_sintetico` carregado com 50 mil linhas
dataFrameEx = pd.read_csv('50k.csv', sep=',', encoding='utf-8')
print(dataFrameEx.head())
print(dataFrameEx.columns)
print(dataFrameEx.dtypes)
# 1. Filtrar por cidade "Manaus"
df_manaus = dataFrameEx[dataFrameEx["cidade"] == "Manaus"]
print(df_manaus)
# 2. Temperatura média por cidade
media_temp_cidade = dataFrameEx.groupby("cidade")["temp_c"].mean().sort_values(ascending=False) # Agrupando por cidade e calculando a média de temperatura .sort_values(ascending=False) ordena os valores em ordem decrescente
print(media_temp_cidade)
# 3. Dias com maior precipitação
dataFrameEx["time"] = pd.to_datetime(dataFrameEx["time"]) # Convertendo para datetime
dataFrameEx["data"] = dataFrameEx["time"].dt.date
top5_precipitacao = dataFrameEx.groupby("data")["precip_mm"].sum().sort_values(ascending=False).head(5) # Agrupando por data e somando a precipitação .head(5) retorna os 5 maiores valores
print(top5_precipitacao)
# 4. Média de UV por período do dia
media_uv_dia_noite = dataFrameEx.groupby("is_day")["uv"].mean() # Agrupando por is_day e calculando a média de UV
print(media_uv_dia_noite)
# 5. Contagem das condições climáticas
contagem_condicoes = dataFrameEx["condicao"].value_counts() # Contando as condições climáticas value_counts() retorna a contagem de valores únicos
print(contagem_condicoes)
# 6. Sensação térmica acima de 35°C e média de umidade
acima_35 = dataFrameEx[dataFrameEx["feelslike_c"] > 35]
qtd_acima_35 = acima_35.shape[0] # Contando os registros acima de 35°C shape[0] retorna o número de linhas 
media_umidade_acima_35 = acima_35["humidity"].mean()
print(f"Quantidade de registros acima de 35°C: {qtd_acima_35}")
print(f"Média de umidade acima de 35°C: {media_umidade_acima_35:.2f}%")

# 7. Criar coluna delta_sensacao
dataFrameEx["delta_sensacao"] = (dataFrameEx["feelslike_c"] - dataFrameEx["temp_c"]).round(1) #arrendando para 1 casa decimal
print(dataFrameEx[["cidade", "temp_c", "feelslike_c", "delta_sensacao"]].head()) # Exibindo as primeiras linhas com a nova coluna .head() retorna as primeiras linhas do DataFrame
# 8. Região com maior média de vento
media_vento_regiao = dataFrameEx.groupby("regiao")["wind_kph"].mean().sort_values(ascending=False)

# 9. Classificação da visibilidade
def classificar_visibilidade(valor):
    if valor >= 10:
        return "Alta"
    elif valor >= 5:
        return "Média"
    else:
        return "Baixa"

dataFrameEx["visibilidade_classificada"] = dataFrameEx["vis_km"].apply(classificar_visibilidade) # Aplicando a função de classificação .apply() aplica uma função a cada elemento da coluna

# 10. Gráfico de temperatura ao longo do tempo para Belo Horizonte
df_bh = dataFrameEx[dataFrameEx["cidade"] == "Belo Horizonte"]
plt.figure(figsize=(12, 4))
plt.plot(df_bh["time"], df_bh["temp_c"], linewidth=0.5)
plt.title("Variação da Temperatura em Belo Horizonte")
plt.xlabel("Tempo")
plt.ylabel("Temperatura (°C)")
plt.tight_layout()
plt.grid(True)
plt.show()
