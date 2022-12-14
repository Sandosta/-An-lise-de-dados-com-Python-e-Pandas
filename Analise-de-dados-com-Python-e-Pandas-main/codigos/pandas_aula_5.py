# -*- coding: utf-8 -*-
"""Pandas_aula_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ckL8vbsie_OJL3ZHZ86WKWFSEmvZMH7k

# **Trabalhando com planilhas do Excel**
"""

# importando o pandas
import pandas as pd

# Leitura dos arquivos - via upload, os arquivos ficam temporariamente no google drive
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

# juntando todos os arquivos
df = pd.concat([df1,df2,df3,df4,df5])

# Exibindo as 5 primeiras linhas
df.head()

# exibindo as 5 últimas linhas
df.tail()

# verificando o tipo de dado de cada coluna
df.dtypes

# Mostra 5 linhas aleatórias
df.sample(5)

# alterando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")

df.dtypes

df.head()

"""### **Tratando valores faltantes**"""

# consultando linhas com valores faltantes (null)
df.isnull().sum()

df

# substituindo valores faltantes - neste caso mostrando a alteração da coluna de vendas
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True) # colocanco a média (mean) onde tem null

# substituindo os valores nulos (null) por zero
df["Vendas"].fillna(0, inplace=True)

# apagando as linhas com valores nulos
df.dropna(inplace=True)

# apagando as linhas com os vaores nulos (null) com base apenas de 1 coluna
df.dropna(subset=["Vendas"], inplace=True)

df["Vendas"].mean()

from numpy import True_
# removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

"""## **Criando colunas novas**"""

# criando a coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])
df.head()

# achando a quantidade
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]
df.head()

# retornando a maior receita
df["Receita"].max()

# retornando a menor receita
df["Receita"].min()

# nlargest - a maior receita
df.nlargest(3, "Receita")

# nsamllest - a menor receita
df.nsmallest(3, "Receita")

# agrupamento por cidade
df.groupby("Cidade")["Receita"].sum()

# ordenando o conjunto de dados
df.sort_values("Receita", ascending=False).head(10)

"""## **Trabalhando com datas**"""

# transformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")
df.head()

# verificando o tipo de dado de cada coluna
df.dtypes

# transformando a coluna data em data
df["Data"] = pd.to_datetime(df["Data"])
df.dtypes

df.head()

# agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()

# criando uma nova coluna com o ano
df["Ano_Vendas"] = df["Data"].dt.year
df.sample(5)

# extraindo mês e dia
df["mes_venda"], df["dia_venda"] = df["Data"].dt.month, df["Data"].dt.day
df.sample(5)

# retornando a data mais antiga
df["Data"].min()

# calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()
df.sample(5)

# criando a coluna de trimestre
df["Trimestre_Vendas"] = df["Data"].dt.quarter
df.sample(5)

# filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
vendas_marco_19

"""# **Visualização de dados**"""

df["LojaID"].value_counts(ascending=False)  # value_counts() soma as quantidades de linhas de cada loja

# gráfico de barras
df["LojaID"].value_counts(ascending=False).plot.bar()

# gráfico de barras horizotais
df["LojaID"].value_counts().plot.barh()

# gráfico de barras horizontais
df["LojaID"].value_counts(ascending=True).plot.barh();   # rterminando com ";" na aparece a primeira linha do matplotlib

# gráfico de pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

# total de vendas por cidade
df["Cidade"].value_counts()

# adicionando um título e alterando o nome dos eixos
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar (title="Total Vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

# alterando a cor
df["Cidade"].value_counts().plot.bar(title="Total Vendas por Cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

# alterando o estilo
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total Produtos Vendidos por mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend()

df.groupby(df["mes_venda"])["Qtde"].sum()

# selecionando apenas as vendas de 2019
df_2019 = df[df["Ano_Vendas"] == 2019]

# total de produtos vendidos por mês
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "o")
plt.xlabel("Mês")
plt.ylabel("Total de Produtos Vendidos");

# Histograma
plt.hist(df["Qtde"], color="orangered")

plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"]);

# salvando em png
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos  por mês")
plt.xlabel("Mês")
plt.ylabel("Total de Produtos Vendidos");
plt.legend()
plt.savefig("grafico QTDE x MES.png")

