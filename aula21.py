"""
operador logico
and (e) or (ou) not (não)
and - todas as condições precisam ser verddeiras 
se qualquer valor for considerado falso, a expressão
inteira sera avaliada naquele valor
são consideradas falsy 0 0.0 '' False
tambem existe do tipo none que é usado para representar
um não valor
"""

# avaliação de curto circuito
# print (True and False and True)
#print(True and 0 and True)

entrada = input('[E]ntrada [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou')
else:
    ('saiu')