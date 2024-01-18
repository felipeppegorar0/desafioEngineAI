import pandas as pd # manipulação dos dados
import streamlit as st # lib para criação do dashboard
import snowflake.connector # conexão com o snowflake
import webbrowser as webbrowser # Redirecionamento para links externos
from queries import query_top_sectors, query_top_companies_25, query_daily_price # importando as queries para oragnizar o código

# Configuração da página para centralizar os dados com base no layout (default)
st.set_page_config(
    page_title="Home",
    layout="centered",
)

# Função para obter a conexão com o Snowflake
def get_snowflake_connection():
    credentials = {
        "user": "guest_felipepegoraro",
        "password": "F123456f*",
        "account": "ui76830.west-europe.azure",
        "database": "CODE_CHALLENGE_FELIPEPEGORARO",
        "schema": "SOURCE",
        "warehouse": "GUEST_CODE_CHALLENGE_FELIPEPEGORARO",
        "role": "GUEST_CODE_CHALLENGE_FELIPEPEGORARO",
    }
    return snowflake.connector.connect(**credentials)

# Função para executar a consulta SQL no Snowflake junto do dataframe 
def fetch_data_from_snowflake(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    data = cursor.fetchall()
    connection.close()
    return pd.DataFrame(data, columns=columns)


# Executar a consulta e obter os dados através da conexão e das queries existentes. Foi criado uma consulta para cada página
snowflake_connection_1 = get_snowflake_connection()
top_sectors_data = fetch_data_from_snowflake(snowflake_connection_1, query_top_sectors)
st.session_state.top_sectors_data = top_sectors_data


snowflake_connection_2 = get_snowflake_connection()
top_companies_25 = fetch_data_from_snowflake(snowflake_connection_2, query_top_companies_25)
st.session_state.top_companies_25 = top_companies_25


snowflake_connection_3 = get_snowflake_connection()
daily_price = fetch_data_from_snowflake(snowflake_connection_3, query_daily_price)
st.session_state.daily_price = daily_price

# Configuração da página usando a documentação e lib do streamlit

st.title("Bem vindo ao Desafio de dados da Engine AI")

st.sidebar.image("Images/logoEngineAI.JPG")


st.markdown(" ")
st.markdown("Como desenvolvedor Python da Equipe de Dashboard, você será responsável por criar dashboards com nossas ferramentas internas. Este exercício tem como objetivo usar dados do Exercício de Dados e realizar as transformações necessárias para produzir um conjunto de tabelas e conteúdo para o dashboard. Os requisitos do dashboard estão listados abaixo.")

st.markdown("1. O dashboard deve começar com um widget mostrando os 10 principais setores por posição na data mais recente.")

st.markdown("2. O segundo widget do dashboard deve ser uma tabela contendo as 25% principais empresas encontradas no Exercício de Dados em uma tabela. A tabela deve mostrar cada empresa e os dados mais recentes. Por favor, mostre os seguintes atributos para cada empresa: Ticker, Setor, Ações, Último Preço de Fechamento em USD, Posição Média do Último Ano.")

st.markdown("3. Por fim, crie uma caixa de seleção com todas as empresas disponíveis no Exercício de Dados que permita escolher uma empresa e mostrar um gráfico de linha de séries temporais com o preço de fechamento diário.")



