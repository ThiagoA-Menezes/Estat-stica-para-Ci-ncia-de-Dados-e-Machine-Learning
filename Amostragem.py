# %%
import pandas as pd
import numpy as np
import random

pathFile = "P:/Python - Projetos/Estatística para Ciência de Dados e Machine Learning/Estatística para Ciência de Dados e Machine Learning/Bases de dados"

dataset = pd.read_csv(f"{pathFile}/census.csv")
# %%
dataset.shape
# %%
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
