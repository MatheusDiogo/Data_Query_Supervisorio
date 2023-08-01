<html>
<body>
  <h1>Projeto de Data Visualization - Supervisório da Planta da Fábrica da Saboaria</h1>
  <p>Este repositório contém códigos e scripts para extrair, tratar e criar um banco de dados para um projeto de Data Visualization dos dados do Supervisório da Planta da Fábrica da Saboaria. O projeto visa obter insights valiosos e visualizações claras a partir dos dados coletados pelo sistema de supervisão da fábrica.</p>
  
  <h2>Objetivo do Projeto</h2>
  <p>O objetivo principal deste projeto é desenvolver um sistema capaz de extrair informações relevantes dos dados do Supervisório da Planta da Fábrica da Saboaria e criar visualizações eficazes para auxiliar na tomada de decisões e no monitoramento do processo produtivo.</p>
  
  <h2>Como Funciona</h2>
  <p>O projeto é composto por três principais códigos Python:</p>
  
  <h3>1. <code>data_alpha.py</code></h3>
  <p>Este código é responsável por extrair os dados do Supervisório. Ele utiliza o comando <code>al_php</code> para obter os dados das tags específicas definidas pelo usuário. Os dados são coletados em intervalos regulares e armazenados em um arquivo CSV.</p>
  
  <h3>2. <code>manipulation_data.py</code></h3>
  <p>Este código é responsável por tratar os dados coletados pelo <code>data_alpha.py</code>. Ele realiza a formatação adequada dos dados e remove caracteres indesejados. O resultado é salvo em um novo arquivo CSV com os dados prontos para serem inseridos no banco de dados.</p>
  
  <h3>3. <code>script.py</code></h3>
  <p>Este é o script principal que utiliza as duas etapas anteriores para criar um banco de dados SQLite. Ele utiliza a biblioteca SQLAlchemy para criar e manipular o banco de dados, criando uma tabela chamada 'Dados' com os dados tratados e inseridos. Além disso, o script executa consultas SQL para extrair informações específicas do banco de dados e exibir os resultados.</p>
  
  <h2>Como Utilizar</h2>
  <p>Para utilizar este projeto, siga os passos abaixo:</p>
  <ol>
    <li>Certifique-se de ter todas as bibliotecas Python necessárias instaladas em seu ambiente.</li>
    <li>Execute o código <code>data_alpha.py</code> para coletar os dados do Supervisório. Defina as tags desejadas no código antes de executá-lo.</li>
    <li>Execute o código <code>manipulation_data.py</code> para formatar os dados coletados e salvá-los em um arquivo CSV pronto para o banco de dados.</li>
    <li>Execute o código <code>script.py</code> para criar o banco de dados e realizar consultas específicas. Certifique-se de que o arquivo CSV gerado pelo <code>manipulation_data.py</code> esteja no mesmo diretório do script.</li>
  </ol>
  <p>Lembre-se de que o script <code>data_alpha.py</code> pode ser configurado para coletar os dados em intervalos regulares. Neste projeto, ele está programado para executar a cada 1 minuto, mas você pode ajustar esse valor conforme suas necessidades.</p>
  
  <h2>Observação</h2>
  <p>Este projeto foi desenvolvido para atender às necessidades específicas do Supervisório da Planta da Fábrica da Saboaria. Caso deseje adaptá-lo para outras finalidades ou sistemas de supervisão, é possível modificar os códigos conforme necessário.</p>
  <p>Esperamos que este projeto seja útil e facilite a extração, tratamento e visualização dos dados do Supervisório da Planta da Fábrica da Saboaria.</p>
  
  <p>Para mais informações, entre em contato conosco.</p>

</body>
</html>
