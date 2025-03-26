#   Estudos
Relacionamentos de tabela
	um para um: só pode ter um registro para um único id
	um para muitos: um item pode receber mais de um id
	muitos para muitos:

criação usando SQL
	# Comando para criar um banco
```
	CREATE DATABASE loja
```
- Comando para criar  tabela para armazenar informações
```
	CREATE TABLE produtos (id INTERGER PRIMARY KEY AUTOINCREMENT, nome
	VARCHAR(100), preco DECIMAL);
```
- Incluir novo produto
```
	INSERT INTO produtos(nome, preco) VALUES('Curso python', 250.00)
```

-- Listar todos os produtos
```
    SELECT * FROM produtos
```

-- Atualizar o produto com if informado
```
    UPDATE produtos SET nome='Curso de python para iniciante' WHERE id = 1;
```

-- Excluir o produto com id informado
```
    DELETE FROM produtos WHERE id = 1;
```