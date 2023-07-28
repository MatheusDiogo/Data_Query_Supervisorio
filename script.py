import os
import pandas as pd
from sqlalchemy import create_engine
from Query_Sql import *
from manipulation_data import *

dados = manipulation("humberto.csv")

print(dados)