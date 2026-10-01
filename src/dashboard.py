import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine


# Conexão com o banco de dados
DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)


# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)


# Título do dashboard
st.title("Dashboard de Temperaturas IoT")


# Gráfico 1: Temperatura media por ambiente
st.header("Temperatura media por Ambiente")

df_temp_ambiente = load_data("temperatura_media_por_ambiente")


fig1 = px.bar(
    df_temp_ambiente,
    x="room_id/id",
    y="temperatura_media"
)

st.plotly_chart(fig1)

# Gráfico 2: Temperaturas mínimas e máximas por ambiente
st.header("Temperaturas Mínimas e Máximas por Ambiente")

df_temp_max_min = load_data("temp_max_min_ambiente")

fig2 = px.bar(
    df_temp_max_min,
    x="room_id/id",
    y=["mínima", "máxima"],
    barmode="group"
)

st.plotly_chart(fig2)

# Gráfico 3: Entradas e saídas
st.header("Quantidade de Entradas e Saídas")

df_entradas_saidas = load_data("entradas_saidas")

fig3 = px.bar(
    df_entradas_saidas,
    x="out/in",
    y="quantidade"
)

st.plotly_chart(fig3)