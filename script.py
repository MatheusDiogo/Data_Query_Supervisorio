import os
import pandas as pd
from sqlalchemy import create_engine
from Query_Sql import *

file = "Dados.csv"

dados = pd.read_csv(str(file), delimiter =';', encoding='iso-8859-1')

engine = create_engine('sqlite:///supervisorio.db')

dados.to_sql('Dados', engine, if_exists='replace', index=False)

query = '''SELECT DATA, Inversor_Jet, Nivel_Jet, Valvula_Pressao_Reator, Valvula_Vazao_Soda, Vavula_Temp_TC1_Secagem_2
FROM dados 
WHERE DATA < 17;'''
df_produtos = sql_df(query, engine)
print(df_produtos.tail())