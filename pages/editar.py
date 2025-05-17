import streamlit as st
import sqlite3
from database import conectar

st.title("✏️ Editar/Remover Produtos")

conn = conectar()
c = conn.cursor()

# Carrega produtos
c.execute("SELECT id, nome FROM produtos")
produtos = c.fetchall()
produto_dict = {produto[1]: produto[0] for produto in produtos}

produto_selecionado = st.selectbox("Selecione um produto", list(produto_dict.keys()))

if produto_selecionado:
    produto_id = produto_dict[produto_selecionado]

    # Carregar os dados do produto selecionado
    c.execute("SELECT quantidade, preco FROM produtos WHERE id=?", (produto_id,))
    produto = c.fetchone()
    
    if produto:
        nova_quantidade = st.number_input("Nova Quantidade", value=produto[0], min_value=0)
        novo_preco = st.number_input("Novo Preço", value=produto[1], min_value=0.0, format="%.2f")

        if st.button("Atualizar"):
            c.execute("UPDATE produtos SET quantidade=?, preco=? WHERE id=?", (nova_quantidade, novo_preco, produto_id))
            conn.commit()
            st.success(f"✅ Produto '{produto_selecionado}' atualizado!")

        if st.button("Remover Produto"):
            c.execute("DELETE FROM produtos WHERE id=?", (produto_id,))
            conn.commit()
            st.error(f"🚨 Produto '{produto_selecionado}' removido!")

conn.close()
