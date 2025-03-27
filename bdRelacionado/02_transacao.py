import sqlite3

# para criar no diretorio
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH /'meuBanco.db')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSET INTO clientes (nome, email) VALUES (?, ?)", ("TESTE 1", "teste@teste.com"))
    cursor.execute("INSET INTO clientes (id, nome, email) VALUES (?, ?, ?)", (2, "TESTE 1", "teste@teste.com"))
    conexao.commit()
except Exception:
    print("Erro ao inserir dados")
    conexao.rollback()