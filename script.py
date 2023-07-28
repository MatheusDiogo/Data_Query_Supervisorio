import os
import pandas as pd
from sqlalchemy import create_engine
from Query_Sql import *
from manipulation_data import *
from data_alpha import *

dados = manipulation("humberto.csv")

engine = create_engine('sqlite:///supervisorio.db')

dados.to_sql('Dados', engine, if_exists='replace', index=False)

query = '''SELECT DATA, Volume_Tq_Sebo_1, Nivel_Tanque_Sebo_1
FROM Dados'''

df = sql_df(query, engine)
print(df.tail())

# Lista com as tags desejadas
tags_desejadas = ['tag1', 'tag2', 'tag3']

# Loop principal para executar a cada 1 minuto
while True:
    retirar_dados(tags_desejadas)
    time.sleep(60)  # Aguarda 1 minuto antes da próxima execução