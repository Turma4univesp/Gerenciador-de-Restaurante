import streamlit as st
import pandas as pd
from database import conectar

st.title("📋 Estoque Atual")

conn = conectar()
query = "SELECT * FROM produtos"
produtos = pd.read_sql(query, conn)
conn.close()

if not produtos.empty:
    st.dataframe(produtos)
else:
    st.warning("⚠️ Nenhum produto cadastrado ainda.")
