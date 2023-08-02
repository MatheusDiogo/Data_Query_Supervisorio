import subprocess
import time

def retirar_dados(tags):
    # Defina os parâmetros do comando al_php
    numero_alinkw_ini = 1
    tags_str = "".join(f'\u00A0"{tag}"\u00A0' for tag in tags)  # Substitua pelas tags desejadas
    data_hora_inicial = "dd1/mm1/yy1 hh1:mm1"  # Substitua pelas datas e horas desejadas
    data_hora_final = "dd2/mm2/yy2 hh2:mm2"  # Substitua pelas datas e horas desejadas
    intervalo_segundos = 60

    # Monta o comando completo
    comando_al_php = f"al_php {numero_alinkw_ini} hist \"{tags_str}\" {data_hora_inicial} {data_hora_final} {intervalo_segundos}"
    print(comando_al_php)
    # Executa o comando al_php no prompt de comando
    subprocess.run(comando_al_php, shell=True)