import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime, timedelta
from database import conectar

st.set_page_config(page_title="Gestão de Estoque", layout="wide")

st.title("📦 Gestão de Estoque Restaurante")

# Função para obter produtos com menor quantidade
def produtos_menor_quantidade():
    conn = conectar()
    query = "SELECT * FROM produtos WHERE quantidade <= 5"
    produtos = pd.read_sql(query, conn)
    conn.close()
    return produtos

# Função para obter produtos próximos ao vencimento
def produtos_proximos_vencimento():
    conn = conectar()
    data_atual = datetime.now()
    data_limite = data_atual + timedelta(days=5)  # Produtos que vencem dentro de 7 dias
    query = "SELECT * FROM produtos WHERE validade BETWEEN ? AND ?"
    produtos = pd.read_sql(query, conn, params=[data_atual.date(), data_limite.date()])
    conn.close()
    return produtos

# Exibindo dashboard
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔴 Produtos com Menor Quantidade")
    produtos_low = produtos_menor_quantidade()
    if not produtos_low.empty:
        st.dataframe(produtos_low)
    else:
        st.info("✅ Nenhum produto com quantidade baixa.")

with col2:
    st.subheader("⚠️ Produtos Próximos ao Vencimento")
    produtos_vencimento = produtos_proximos_vencimento()
    if not produtos_vencimento.empty:
        st.dataframe(produtos_vencimento)
    else:
        st.info("✅ Nenhum produto próximo ao vencimento.")
