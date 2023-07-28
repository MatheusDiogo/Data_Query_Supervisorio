import os
import pandas as pd
from sqlalchemy import create_engine
from Query_Sql import *
from manipulation_data import *

dados = manipulation("humberto.csv")

engine = create_engine('sqlite:///supervisorio.db')

dados.to_sql('Dados', engine, if_exists='replace', index=False)

query = '''SELECT DATA, Volume_Tq_Sebo_1, Nivel_Tanque_Sebo_1
FROM Dados'''

df = sql_df(query, engine)
print(df.tail())