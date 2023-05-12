"""
Interpolação basica de strings

s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

nome = 'manoel'
preco = 1000.997463
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %04x' % (1500, 1500))