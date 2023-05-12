"""
peça ao usuário digitar seu nome.
peça ao usuário para digitar sua idade.
se nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        seu nome tem {n} letras
        a primeira letra do seu nome é:
        a ultima letra do seu nome é:
se nada for digitado em nome e idade:
    exiba:
        "Desculpa, você deixou campos vazio."
"""

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")
if nome:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    print(f'seu nome tem {len(nome)} letras')
else:
    print("vc não digitou")

if idade:
    print(f'sua idade é {idade}')
else:
    print("vc não digitou")