from sqlalchemy import create_engine, inspect, text
import pandas as pd

def sql_df(query, engine):
  with engine.connect() as conexao:
    consulta = conexao.execute(text(query))
    dados = consulta.fetchall()
  return pd.DataFrame(dados,columns=consulta.keys())