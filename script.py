import os
import pandas as pd
from sqlalchemy import create_engine
from Query_Sql import *
from manipulation_data import *
from data_alpha import *

# Lista com as tags desejadas
tags_desejadas = ['V-1101', 'LI-1101', 'TI-2101', 'V-1201', 'LI-1201',
                  'TI-2102', 'V-1301', 'LI-1301', 'TI-2103', 'V-2105',
                  'LI-2105', 'TI-2105', 'V-2106', 'LI-2106', 'TI-2106',
                  'TI-2104', 'LI-1401', 'LI-3102', 'LI-3101', 'FI-4201',
                  'FI-4204', 'FI-4202', 'LI-3107', 'LI-3104', 'TI-4303',
                  'LI-4101', 'PI-4401', 'PI-4402', 'TI-4305', 'TI-4304',
                  'LI-1401', 'TI-0103', 'LI-6101', 'FI-0201', 'TI-0403',
                  'PI-0301', 'PI-6401', 'TI-0803', 'TI-0804', 'PI-0302']

# # Loop principal para executar a cada 1 minuto
while True:
    retirar_dados(tags_desejadas)
    time.sleep(60)  # Aguarda 1 minuto antes da próxima execução

    dados = manipulation("teste entrada.csv")

    engine = create_engine('sqlite:///supervisorio.db')

    dados.to_sql('Dados', engine, if_exists = 'replace', index=False)

    query = '''SELECT DATA, Volume_Tq_Sebo_1_em_kg, Nivel_Tanque_Sebo_1, Temperatura_Tanque_de_Sebo_1
    FROM Dados'''

    df = sql_df(query, engine)
    print(df.tail())