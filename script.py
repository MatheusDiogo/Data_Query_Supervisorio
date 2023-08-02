import os
import pandas as pd
from sqlalchemy import create_engine
from Query_Sql import *
from manipulation_data import *
from data_alpha import *

dados = manipulation("teste entrada.csv")

engine = create_engine('sqlite:///supervisorio.db')

# Verificar colunas duplicadas
if dados.columns.duplicated().any():
    # Identificar o nome da coluna duplicada
    coluna_duplicada = dados.columns[dados.columns.duplicated()][0]
    
    # Excluir a coluna duplicada do DataFrame
    dados = dados.drop(coluna_duplicada, axis=1)

    # Renomear a coluna duplicada
    #dados.rename(columns={coluna_duplicada: coluna_duplicada + '_duplicada'}, inplace=True)

dados.to_sql('Dados', engine, if_exists = 'replace', index=False)

query = '''SELECT DATA, Volume_Tq_Sebo_1_em_kg, Nivel_Tanque_Sebo_1, Temperatura_Tanque_de_Sebo_1
FROM Dados'''

df = sql_df(query, engine)
print(df.tail())

# Lista com as tags desejadas
tags_desejadas = ['tag1', 'tag2', 'tag3']

# # Loop principal para executar a cada 1 minuto
# while True:
#     retirar_dados(tags_desejadas)
#     time.sleep(60)  # Aguarda 1 minuto antes da próxima execução