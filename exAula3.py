
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
df_avg_temperatura = (
    dataFrameEx
    .groupby(by=["cidade"])
    .agg(avg_temperatura=("temp_c", "mean"), mediana=("temp_c", "median")) # Agrupando por cidade e calculando a média e mediana de temperatura
    .sort_values(by=["avg_temperatura", "mediana"], ascending=[False, True])
    .reset_index()
) # criamos uma nova coluna chamada avg_temperatura com a média de temperatura e mediana com a mediana de temperatura, estamos utilizando o método sort_values para ordenar os valores pela média de temperatura e mediana, e o método reset_index para redefinir o índice do DataFrame resultante
print(df_avg_temperatura) # Exemplo durante a aula

media_temp_cidade = dataFrameEx.groupby("cidade")["temp_c"].mean().sort_values(ascending=False, ) # Agrupando por cidade e calculando a média de temperatura .sort_values(ascending=False) ordena os valores em ordem decrescente
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
print(acima_35)
print(f"Quantidade de registros acima de 35°C: {qtd_acima_35}")
print(f"Média de umidade acima de 35°C: {media_umidade_acima_35:.2f}%")

########### Variacao 1
print(dataFrameEx[dataFrameEx['feelslike_c']>35].agg({'feelslike_c':'count','humidity':'mean'}))

########### Variacao 2
# 6 - sensação térmica acima de 35oC
df_humidity_feelslike = (
    dataFrameEx
    .loc[(dataFrameEx["feelslike_c"] > 35)]
    .agg(
        count=("feelslike_c", "count"),
        avg_humidity = ("humidity", "mean")
    )
)
print(df_humidity_feelslike)
 
##########

# 7. Criar coluna delta_sensacao
dataFrameEx["delta_sensacao"] = (dataFrameEx["feelslike_c"] - dataFrameEx["temp_c"]).round(1) #arrendando para 1 casa decimal
print(dataFrameEx[["cidade", "temp_c", "feelslike_c", "delta_sensacao"]].head()) # Exibindo as primeiras linhas com a nova coluna .head() retorna as primeiras linhas do DataFrame
# 8. Região com maior média de vento
media_vento_regiao = dataFrameEx.groupby("regiao")["wind_kph"].mean().sort_values(ascending=False)

#######
print(dataFrameEx.agg({"wind_kph": "mean"}).sort_values(ascending=False))  # Média de vento por região
######
# 9. Classificação da visibilidade
def classificar_visibilidade(valor):
    if valor >= 10:
        return "Alta"
    elif valor >= 5:
        return "Média"
    else:
        return "Baixa"

dataFrameEx["visibilidade_classificada"] = dataFrameEx["vis_km"].apply(classificar_visibilidade)  # Aplicando a função de classificação .apply() aplica uma função a cada elemento da coluna
print(dataFrameEx[["cidade", "vis_km", "visibilidade_classificada"]].head()) # Exibindo as primeiras linhas com a nova coluna


########## variacao 1

dataFrameEx['visibilidade_classificada'] = np.where(dataFrameEx['vis_km'] >= 10, 'Alta', '')
dataFrameEx['visibilidade_classificada'] = np.where((dataFrameEx['vis_km'] >= 5) & (dataFrameEx['vis_km'] < 10), 'Média',  dataFrameEx['visibilidade_classificada'])
dataFrameEx['visibilidade_classificada'] = np.where(dataFrameEx['vis_km'] < 5 ,'Baixa', dataFrameEx['visibilidade_classificada'])
print(dataFrameEx['visibilidade_classificada'].value_counts())

########## Variacao 2
dataFrameEx["vis_class"] = (
    dataFrameEx["vis_km"]
    .apply(lambda x: "Alta" if x >= 10 else ("Média" if x >= 5 else "Baixa"))
)
print(dataFrameEx[["vis_class", "vis_km"]].sample(10))
############# Variacao 3

# condicoes = [
#     (dataFrameEx['vis_km'] >= 10),  #  "Alta"
#     (dataFrameEx['vis_km'] >= 5) & (dataFrameEx['vis_km'] < 10),  #  "Média"
#     (dataFrameEx['vis_km'] < 5)  # "Baixa"
#     ]
# valores = ['Alta', 'Média', 'Baixa']
# test = np.select(condicoes, valores)
# dataFrameEx['categoria_visibilidade'] = 0
# print(dataFrameEx['categoria_visibilidade'].value_counts())

#############
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
