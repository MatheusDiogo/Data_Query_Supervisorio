##################################################################################
#                         Campo de Bibliotecas                                   #
##################################################################################
from unidecode import unidecode
import pandas as pd
import re

def manipulation(arquivo):
    ##################################################################################
    #                         Abertura do Arquivo                                    #
    ##################################################################################

    abre_Arquivo = pd.read_csv(arquivo, encoding='ISO-8859-1', delimiter = ';') #variavel do tipo data frame que guardara o arquivo
    filename = "teste saida.csv" #nome do arquivo de saida

    ##################################################################################
    #                         Inicializando variaveis                                #
    ##################################################################################
    NumR = abre_Arquivo['TAG'].eq('Descrição').idxmax()+1 #Numero de linhas para repetição
    lstIteracao = [] # Variavel do tipo lista que ira conter os conteudos dos blocos de 17 linhas na iteracao
    listsupervisorio = [] # Variavel do tipo lista que ira conter o conteudo do arquivo .csv
    newlistsupervisorio = [] # Variavel do tipo lista que ira receber a lista com o conteudo sem caracteres indesejados
    supervisoriofinal = pd.DataFrame() # Variavel do tipo data frame que ira conter a formatacao final desejada

    ##################################################################################
    #                         Formatacao do Arquivo                                  #
    ##################################################################################

    listsupervisorio = abre_Arquivo.values.tolist() # Conversao dos dados do arquivo para armazenar na variavel do tipo lista

    listsupervisorio.insert(0,'TAG') # Inserindo item na primeira posicao da lista, item refere-se ao titulo da TAG do componente dentro do arquivo

    # Laco para exclusao de colchetes e aspas contidos nos elementos da lista
    newlistsupervisorio = [re.sub('[\[\'\]]', '', str(item)) for item in listsupervisorio]

    # Criação do DataFrame formatado usando pd.concat
    chunks = [newlistsupervisorio[i:i + NumR] for i in range(0, len(newlistsupervisorio), NumR)]
    supervisoriofinal = pd.concat([pd.Series(chunk) for chunk in chunks], axis=1, ignore_index=True)

    ##################################################################################
    #                         Saída do Arquivo                                       #
    ##################################################################################
    supervisoriofinal = supervisoriofinal.T
    supervisoriofinal = pd.DataFrame(supervisoriofinal.drop([0,2]))
    supervisoriofinal.reset_index(drop = True, inplace = True)
    for col in supervisoriofinal.columns:
        supervisoriofinal[col] = supervisoriofinal[col].apply(lambda x: unidecode(x) if isinstance(x, str) else x)

    # Atribuir nomes das colunas corretamente
    col_names = supervisoriofinal.iloc[0].tolist()
    supervisoriofinal.columns = col_names

    # Remover a primeira linha (que continha os nomes das colunas repetidos)
    supervisoriofinal = supervisoriofinal.iloc[1:].reset_index(drop=True)

    # Atribuir o nome correto à primeira coluna
    supervisoriofinal.rename(columns={col_names[0]: "DATA"}, inplace=True)
    
    # Substituir espaços em branco por sublinhados em todos os nomes de colunas
    supervisoriofinal.rename(columns=lambda col: col.replace(' ', '_'), inplace=True)
    supervisoriofinal.rename(columns=lambda col: col.replace('.', ''), inplace=True)

    # Verificar colunas duplicadas
    if supervisoriofinal.columns.duplicated().any():
        # Identificar o nome da coluna duplicada
        coluna_duplicada = supervisoriofinal.columns[supervisoriofinal.columns.duplicated()][0]
        
        # Excluir a coluna duplicada do DataFrame
        supervisoriofinal = supervisoriofinal.drop(coluna_duplicada, axis=1)

        # Renomear a coluna duplicada
        #supervisoriofinal.rename(columns={coluna_duplicada: coluna_duplicada + '_duplicada'}, inplace=True)

    supervisoriofinal.to_csv(filename, index=False) #convertendo para planilha excel
    return supervisoriofinal
