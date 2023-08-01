#Projeto de Data Visualization - Supervisório da Planta da Fábrica da Saboaria

Este repositório contém códigos e scripts para extrair, tratar e criar um banco de dados para um projeto de Data Visualization dos dados do Supervisório da Planta da Fábrica da Saboaria. O projeto visa obter insights valiosos e visualizações claras a partir dos dados coletados pelo sistema de supervisão da fábrica.

Objetivo do Projeto
O objetivo principal deste projeto é desenvolver um sistema capaz de extrair informações relevantes dos dados do Supervisório da Planta da Fábrica da Saboaria e criar visualizações eficazes para auxiliar na tomada de decisões e no monitoramento do processo produtivo.

Como Funciona
O projeto é composto por três principais códigos Python:

1. data_alpha.py
Este código é responsável por extrair os dados do Supervisório. Ele utiliza o comando al_php para obter os dados das tags específicas definidas pelo usuário. Os dados são coletados em intervalos regulares e armazenados em um arquivo CSV.

2. manipulation_data.py
Este código é responsável por tratar os dados coletados pelo data_alpha.py. Ele realiza a formatação adequada dos dados e remove caracteres indesejados. O resultado é salvo em um novo arquivo CSV com os dados prontos para serem inseridos no banco de dados.

3. script.py
Este é o script principal que utiliza as duas etapas anteriores para criar um banco de dados SQLite. Ele utiliza a biblioteca SQLAlchemy para criar e manipular o banco de dados, criando uma tabela chamada 'Dados' com os dados tratados e inseridos. Além disso, o script executa consultas SQL para extrair informações específicas do banco de dados e exibir os resultados.

Como Utilizar
Para utilizar este projeto, siga os passos abaixo:

Certifique-se de ter todas as bibliotecas Python necessárias instaladas em seu ambiente.
Execute o código data_alpha.py para coletar os dados do Supervisório. Defina as tags desejadas no código antes de executá-lo.
Execute o código manipulation_data.py para formatar os dados coletados e salvá-los em um arquivo CSV pronto para o banco de dados.
Execute o código script.py para criar o banco de dados e realizar consultas específicas. Certifique-se de que o arquivo CSV gerado pelo manipulation_data.py esteja no mesmo diretório do script.
Lembre-se de que o script data_alpha.py pode ser configurado para coletar os dados em intervalos regulares. Neste projeto, ele está programado para executar a cada 1 minuto, mas você pode ajustar esse valor conforme suas necessidades.

Observação
Este projeto foi desenvolvido para atender às necessidades específicas do Supervisório da Planta da Fábrica da Saboaria. Caso deseje adaptá-lo para outras finalidades ou sistemas de supervisão, é possível modificar os códigos conforme necessário.

Esperamos que este projeto seja útil e facilite a extração, tratamento e visualização dos dados do Supervisório da Planta da Fábrica da Saboaria.

Para mais informações, entre em contato conosco.
