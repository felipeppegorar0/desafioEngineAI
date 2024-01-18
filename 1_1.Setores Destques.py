import pandas as pd
import streamlit as st

# Configuração da página para centralizar os dados com base no layout (default)
st.set_page_config(
    page_title="Série Temporal de Preços",
    layout="wide",
)

# Logo da Engine AI na barra lateral
st.sidebar.image("Images/logoEngineAI.JPG")

# Verifica se as informações estão carregadas
if "top_sectors_data" not in st.session_state:
    # Exibe um spinner enquanto as informações estão sendo carregadas
    with st.spinner("Retorne a página Home e aguarde os dados a serem carregados..."):
        # Aguarde até que as informações estejam disponíveis na st.session_state
        while "top_sectors_data" not in st.session_state:
            pass

# Informações geradas na página Home (dataframe)
top_sectors_data = st.session_state.top_sectors_data

# Ordenação do dataframe pelo valor
top_sectors_data = top_sectors_data.sort_values(by='POSITIONUSD', ascending=False)

# Tratamento do dado concatenando o índice do dataframe com o nome para deixar de forma ordenada o gráfico de barras, visto as limitações do streamlit para realizar essa operação de ordenação
top_sectors_data['Setor Numerado'] = top_sectors_data.index.map(lambda x: f"{x}. {top_sectors_data['SECTOR'][x]}")

# Configuração da página usando a documentação e lib do streamlit
st.title("Bem Vindo a Analise de dados Financeira")

st.header("Top 10 Setores por Posição")

st.markdown(" ")

# Gráfico em barra usando container para ajustar ao tamanho da página
st.bar_chart(top_sectors_data.set_index('Setor Numerado')['POSITIONUSD'], use_container_width=True, height=500)
