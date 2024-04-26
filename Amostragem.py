# %%
import pandas as pd
import numpy as np
import random

pathFile = "P:/Python - Projetos/Estatística para Ciência de Dados e Machine Learning/Estatística para Ciência de Dados e Machine Learning/Bases de dados"

dataset = pd.read_csv(f"{pathFile}/census.csv")
# %%
dataset.shape
# %%
# Shape do Dataset carregado 
dataset.head()
# %%
dataset.tail()
# %%
df_amostra_aleatoria_simples = dataset.sample(n=100, random_state=1)
# %%
df_amostra_aleatoria_simples.shape
# %%
df_amostra_aleatoria_simples.head()
# %%
def amostragem_aleatoria_simples(dataset, amostras):
    return dataset.sample(n = amostras, random_state=1)
# %%
df_amostra_aleatoria_simples = amostragem_aleatoria_simples(dataset, 100)
df_amostra_aleatoria_simples.shape
# %%
df_amostra_aleatoria_simples.head()
# %%

# Amostragem sistemática
len(dataset) // 100
# %%
# Selecionar um numero aleatório de 0 a 325
random.seed(1)
random.randint(0,325)
# %%
# Aqui vamos buscar o resultado do Seed (1) somado ao número de amostragem
68+325
# %%
# Validando os números açeatórios que serão selecionados
393+325
# %%
# Buscar um range aleatório com base nas amostragens que levantamos anteriormente.
np.arange(68, len(dataset), step=325)
# %%
#Vamos criar uma função para colocar o codigo da amostragem sistemática
def amostragem_sistematica(dataset, amostras):
    intervalo = len(dataset) // amostras
    random.seed(1)
    inicio = random.randint(0, intervalo)
    indices = np.arange(inicio, len(dataset), step = intervalo)
    amostra_sistematica = dataset.iloc[indices]
    return amostra_sistematica

# %%
df_amostra_sistematica = amostragem_sistematica(dataset, 100)
df_amostra_sistematica.shape
# %%
df_amostra_sistematica.head()
# %%
