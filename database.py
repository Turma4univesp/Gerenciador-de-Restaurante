import sqlite3

DB_NAME = "estoque.db"

def conectar():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL,
            validade DATE
        )
    ''')
    conn.commit()
    conn.close()

# Executa a criação da tabela ao iniciar o sistema
criar_tabela()
