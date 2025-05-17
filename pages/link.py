import os
import streamlit as st
import streamlit.components.v1 as components

# Caminho absoluto baseado na raiz do app
#file_path = os.path.join(os.path.dirname(__file__), "..", "rest", "index.html")

#with open(file_path, 'r', encoding='utf-8') as f:
 #   html_content = f.read()

#components.html(html_content, height=600, scrolling=True)
#st.markdown('[Abrir página HTML](http://localhost:8000/index.html)', unsafe_allow_html=True)
#st.markdown(
 #   '<a href="http://localhost:8000/index.html" target="_blank">Abrir Cardapio</a>',
  #  unsafe_allow_html=True
#)
st.title("App com link para HTML externo")

st.markdown(
    '<a href="http://localhost:5001/html/index.html" target="_blank">Abrir HTML</a>',
    unsafe_allow_html=True
)
