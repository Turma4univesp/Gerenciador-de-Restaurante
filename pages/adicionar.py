import streamlit as st
import sqlite3
from database import conectar

st.title("➕ Adicionar Produto")

conn = conectar()
c = conn.cursor()

with st.form("form_adicionar"):
    nome = st.text_input("Nome do Produto")
    quantidade = st.number_input("Quantidade", min_value=0, step=1)
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")
    validade = st.date_input("Data de Validade")
    submit_button = st.form_submit_button("Adicionar Produto")

    if submit_button:
        if nome and quantidade > 0 and preco > 0 and validade:
            c.execute("INSERT INTO produtos (nome, quantidade, preco, validade) VALUES (?, ?, ?, ?)",
                      (nome, quantidade, preco, validade))
            conn.commit()
            st.success(f"✅ Produto '{nome}' adicionado com sucesso!")
        else:
            st.error("❌ Preencha todos os campos corretamente!")

conn.close()
