import sqlite3

# para criar no diretorio
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH /'meuBanco.db')
print(conexao)


# criar tabelas
cursor = conexao.cursor()

cursor.execute("CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))")