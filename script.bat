@echo off
setlocal EnableDelayedExpansion

:loop

REM Obter data e hora atual do sistema no formato dd/mm/yy hh:mm
set "datetime=%DATE:/=%%TIME::=%"
set "datetime=!datetime: =!"
set "datetime=!datetime:~0,12!"

REM Defina as variáveis com os valores desejados
set "supervisory_cmd=al_php 1 hist ""<tag1> <tag2>"" !datetime! !datetime! 60 > arquivo.txt"
set "output_file=C:\caminho\para\seu\arquivo.txt"

REM Execute o comando do supervisório
%supervisory_cmd%

REM Copie os dados para o servidor local (ou execute os comandos necessários para fazer isso)
REM Exemplo de comando para copiar o arquivo para um servidor usando o comando "copy":
copy arquivo.txt \\nomedo servidor\caminho\para\pasta

REM Aguarde 1 minuto
timeout 60 /nobreak

goto loop
