# Operador logico 'not'
# é usado para inverter expressões 
# not True = False / print(not True)
# note False = True / print(not False)

"""
Operadores in e not in / in = estar entre / not in = não estar entre
Strings são interáveis 
0 1 2 3 4 5
m a n o e l
-6-5-4-3-2-1
"""
nome = input('digite alguma palavra: ')
encontrar = input('digite o que quer encontrar na palavra digitada: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')