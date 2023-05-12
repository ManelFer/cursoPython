primeiro_valor = input('digite um numero: ')
segundo_valor = input('digite outro numero: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor} é igual ao {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'{primeiro_valor} é menor que {segundo_valor}')

print('fim do codigo')