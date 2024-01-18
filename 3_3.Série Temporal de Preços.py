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
if "daily_price" not in st.session_state:
    # Exibe um spinner enquanto as informações estão sendo carregadas
    with st.spinner("Retorne a página Home e aguarde os dados a serem carregados..."):
        # Aguarde até que as informações estejam disponíveis na st.session_state
        while "daily_price" not in st.session_state:
            pass

# Seleção das colunas do dataframe
columns_to_select = ["DATA", "PRECO_DE_FECHAMENTO"]

daily_price = st.session_state.daily_price

# tratamento no metadado
daily_price["PRECO_DE_FECHAMENTO"] = pd.to_numeric(daily_price["PRECO_DE_FECHAMENTO"], errors='coerce') # dado formatado para numero
daily_price["DATA"] = pd.to_datetime(daily_price["DATA"])  # Dado formatado para data

# Ticker traz o dado unico para nao duplicar valores e incluir no selectbox (filtro de dados)
ticker = daily_price["EMPRESA_TICKER"].value_counts().index
empresas = st.sidebar.selectbox("Ticker Empresas", ticker)

# Ordernação dos dados
daily_price = daily_price.sort_values(by="DATA", ascending=False)

# Traz o valor mais recente do preço com base no filtro selecionado
valor_mais_recente = daily_price.loc[daily_price["EMPRESA_TICKER"] == empresas, "PRECO_DE_FECHAMENTO"].iloc[0]

# Filtro de ano
start_year = daily_price["DATA"].dt.year.min()
end_year = daily_price["DATA"].dt.year.max()
selected_year = st.sidebar.slider("Selecione um ano", start_year, end_year, (start_year, end_year))

# Filtro de dados no intervalos selecionado pelo filtro
df_empresa_price = daily_price[(daily_price["EMPRESA_TICKER"] == empresas) & 
                               (daily_price["DATA"].dt.year >= selected_year[0]) &
                               (daily_price["DATA"].dt.year <= selected_year[1])]

# Traz as colunas armazenadas no inicio do código
df_selected_columns = df_empresa_price[columns_to_select]

# Configuração da página usando a documentação e lib do streamlit
st.title("Histórico de preços das empresas por Ação")

st.subheader(f"Histórico de preços para a empresa selecionada: {empresas}")


st.subheader(f"Cotação mais recente: USD {valor_mais_recente}")

st.write("O gráfico abaixo contem o histórico de fechamento dos preços, sendo determinado por data. Utilize os filtros para determinar as empresas e a série temporal")

# Gráfico de linhas
st.line_chart(df_selected_columns.set_index("DATA"), use_container_width=True, height=500, width=650)
