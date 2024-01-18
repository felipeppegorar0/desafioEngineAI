import pandas as pd
import streamlit as st
from datetime import datetime


# Configuração da página para centralizar os dados com base no layout (default)

st.set_page_config(
    page_title="Série Temporal de Preços",
    layout="wide",
)

# Logo da Engine AI na barra lateral
st.sidebar.image("Images/logoEngineAI.JPG")

# Verifica se as informações estão carregadas
if "top_companies_25" not in st.session_state:
    # Exibe um spinner enquanto as informações estão sendo carregadas
    with st.spinner("Retorne a página Home e aguarde os dados a serem carregados..."):
        # Aguarde até que as informações estejam disponíveis na st.session_state
        while "top_companies_25" not in st.session_state:
            pass

# Informações geradas na página Home (dataframe)
top_companies_25 = st.session_state.top_companies_25


# Renomear as colunas para o visual
top_companies_25.rename(columns={
    'TICKER': 'Código da Ação',
    'MEDIA': 'Média USD (Ano anterior)',
    'SECTOR_NAME': 'Nome do setor',
    'CLOSE_USD': 'Preço de fechamento USD (Ano atual)',
    'SHARES': 'Ações (Ano atual)',
}, inplace=True)

# Ordenar as colunas para deixar a visualização mais intuitiva
order_of_columns = ['Código da Ação','Nome do setor','Média USD (Ano anterior)','Preço de fechamento USD (Ano atual)','Ações (Ano atual)']
top_companies_25 = top_companies_25[order_of_columns]

# lib datetime para trazer informação dinamica no titulo da página
ano_atual = datetime.now().year

ano_anterior = ano_atual - 1

# Configuração da página usando a documentação e lib do streamlit
st.title(f"Top 25 Companias do Ultimo Ano: {ano_anterior}")

st.table(top_companies_25)
