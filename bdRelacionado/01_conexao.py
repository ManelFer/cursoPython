import sqlite3

# para criar no diretorio
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH /'meuBanco.db')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row
print(conexao)


# criar tabelas
def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))")
    conexao.commit()


# inserir dados
def inserir_dados(conexao, cursor, nome, email):
    # dados
    data = (nome, email)
        # comando
    cursor.execute("INSERT INTO clients (nome, email) VALUES (?, ?);", data)
        # salvar
    conexao.commit()

def atualizar_dados(conexao, cursor, nome, email, id):
    # dados
    data = (nome, email, id)
        # comando
    cursor.execute("UPDATE clients SET nome=?, email=? WHERE id=?;", data)
        # salvar
    conexao.commit()

def excluir_dados(conexao, cursor, id):
    # dados
    data = (id,)
        # comando
    cursor.execute("DELETE FROM clients WHERE id=?;", data)
        # salvar
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clients WHERE id=?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clients ORDER BY nome;")



clientes = listar_clientes(cursor)  
for cliente in clientes:
    print(dict(cliente))  

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))

print (f'Seja bem vindo {cliente["nome"]}')

# inserir muitos dados sem perder a conexao
#def inserir_muitos(conexao, cursor, dados):
#  cursor.executemany("INSERT INTO clients (nome, email) VALUES (?, ?);", dados)
#    conexao.commit()
#dados = [
#    ("manoel", "manoel@teste.com"),
#    ("joao", "joao@teste.com"),
#    ("maria", "maria@teste.com"),
#]
#inserir_muitos(conexao, cursor, dados)