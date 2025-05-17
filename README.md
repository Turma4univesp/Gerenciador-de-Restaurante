# 🍽️ Gerenciador de Restaurante

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow" alt="status">
  <img src="https://img.shields.io/badge/Python-3.10-blue" alt="python">
  <img src="https://img.shields.io/badge/Streamlit-red?logo=streamlit" alt="streamlit">
  <img src="https://img.shields.io/badge/SQLite-lightgrey?logo=sqlite" alt="sqlite">
</p>

## 📌 Descrição

O **Gerenciador de Restaurante** é uma aplicação web interativa desenvolvida como parte do Projeto Integrador da UNIVESP. Ela tem como objetivo facilitar o dia a dia de estabelecimentos gastronômicos, automatizando o controle de pedidos, gerenciamento de estoque e exibição de relatórios, com uma interface simples e acessível.

---

## 🧩 Funcionalidades

✅ Registro e visualização de pedidos  
✅ Controle de estoque com atualizações em tempo real  
✅ Consulta de dados diretamente na interface  
✅ Link para página HTML externa com conteúdo adicional  
✅ Interface com navegação lateral usando Streamlit

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python** — Lógica da aplicação
- 🖼️ **Streamlit** — Criação da interface web
- 🔥 **Flask** — Servidor leve para arquivos estáticos
- 💾 **SQLite** — Banco de dados local
- 🌐 **HTML/CSS** — Página externa customizável

---

## 🗂️ Estrutura do Projeto

├── app.py # Aplicação principal (Streamlit)
├── server.py # Servidor Flask para arquivos HTML
├── database.py # Operações no banco SQLite
├── estoque.db # Banco de dados local
├── requirements.txt # Dependências do projeto
├── Procfile # Arquivo para deploy no Render
├── static/
│ └── index.html # Página HTML externa
└── pages/
└── link.py # Página com link para o HTML


---

## 💻 Como Executar Localmente

> Pré-requisitos: Python 3.10+, Git

```bash
# 1. Clone o repositório
git clone https://github.com/Turma4univesp/Gerenciador-de-Restaurante.git
cd Gerenciador-de-Restaurante

# 2. Crie o ambiente virtual
python -m venv venv
# Ative o ambiente:
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode o servidor Flask
python server.py
# Acesse: http://localhost:5001

# 5. Em outro terminal, execute o app Streamlit
streamlit run app.py
# Acesse: http://localhost:8501

👨‍💻 Equipe
Nome	GitHub
Turma 06 - UNIVESP	@Turma4univesp

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

