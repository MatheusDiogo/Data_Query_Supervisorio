import subprocess
import time
import datetime

def retirar_dados(tags):
    # Defina os parâmetros do comando al_php
    nome_arquivo_coleta = 'nome_arquivo_coleta'
    numero_alinkw_ini = 1
    tags_str = "".join(f"{{{tag}}}" for tag in tags)  # Substitua pelas tags desejadas
    data_hora_inicial = "dd1/mm1/yy1 hh1:mm1"  # Substitua pelas datas e horas desejadas
    # Obter a data e hora atual
    data_hora_atual = datetime.datetime.now()
    # Formatar a data e hora no formato desejado
    data_hora_final = data_hora_atual.strftime("%d/%m/%y %H:%M")
    intervalo_segundos = 60

    # Monta o comando completo
    comando_al_php = f"al_php {numero_alinkw_ini} hist \"{tags_str}\" {data_hora_inicial} {data_hora_final} {intervalo_segundos} {nome_arquivo_coleta}"
    print(comando_al_php)
    # Executa o comando al_php no prompt de comando
    subprocess.run(comando_al_php, shell=True)