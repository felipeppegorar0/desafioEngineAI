# Utilização do ambiente

Lembre-se de instalar as bibiliotecas necessárias no ambiente:

pip install pandas
pip install streamlit
pip install snowflake-connector-python

Versão do Python: 3.10.12


# CONSIDERAÇÕES DO DESAFIO:

1. Performance:
    - Quanto na parte das queries, os joins podem ser mais performaticos com colunas indexadas nas tabelas de origem;
    - Foi utilizado as CTE's como forma de stage e facilitar a visualização de cada etapa do código realizada;

    - No streamlit há uma demora (siginificativa) para a carga inicial dos dados na página Home que gera toda a conexão e queries no banco,
    pode ser pelas queries realizadas que há demora para processarem no banco de dados;

    - Acredito que dê para melhorar a estrutura e separação do código, porém de imediato creio atender as necessidades do desafio.

2. Estudo dos dados:

    - Foi utilizado a tabela position para normalização dos dados referente a gaps existentes nas datas de preço de fechamento e position.
    Toda vez em que a tabela position buscava os dados de preço na tabela price, e a data nao existia referente aquele dia, utilizou-se sempre a ultima data de fechamento. A query da questão 1 aborda melhor esse cenário.

    - Para trazer os preços diarios solicitados pela questão 3 na parte de dashboard, utilizou estes dados normalizado com base na tabela position, pois os dados ja estavam tratados, motivo para encontrar dados apartir de 2016.

3. Validações:

    - Foi pego uma amostra para verificar a veracidade dos preços e gráficos utilizando o site https://br.tradingview.com/.

