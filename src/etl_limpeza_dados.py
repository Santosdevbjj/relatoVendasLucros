"""
Script de ETL: Limpeza e Preparação dos Dados de Vendas e Lucros
Autor: Sérgio Santos
Descrição: Este script realiza a carga, limpeza e transformação dos dados
para posterior análise em Power BI ou Jupyter.
"""

import pandas as pd

# === Carregar os arquivos CSV ===
vendas = pd.read_csv("../data/vendas.csv")
produtos = pd.read_csv("../data/produtos.csv")
clientes = pd.read_csv("../data/clientes.csv")
regioes = pd.read_csv("../data/regioes.csv")

# === Limpeza básica ===
vendas.dropna(inplace=True)
vendas["Data"] = pd.to_datetime(vendas["Data"])
vendas["Receita"] = vendas["Quantidade"] * vendas["Preco_Unitario"]
vendas["Custo"] = vendas["Quantidade"] * vendas["Custo_Unitario"]
vendas["Lucro"] = vendas["Receita"] - vendas["Custo"]

# === Merge com dimensões ===
df_final = vendas.merge(produtos, on="ID_Produto") \
                 .merge(clientes, on="ID_Cliente") \
                 .merge(regioes, on="ID_Regiao")

# === Salvar resultado final ===
df_final.to_csv("../data/vendas_tratadas.csv", index=False)

print("✅ Dados tratados com sucesso e exportados para /data/vendas_tratadas.csv")
