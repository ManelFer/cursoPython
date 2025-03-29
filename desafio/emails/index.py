# Recebe a entrada e armazena na variável "entrada"
entrada = input()

# Função reponsável por extrair os domínios dos emails
def extrair_dominios(emails_str):
    # Separa os emails por ponto e vírgula
    lista_emails = emails_str.split(';')
    
    # TODO: Implemente a lógica necessária para extrair os domínios
    dominios = [email.split('@')[1] for email in lista_emails if '@' in email]
    
    return dominios

# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))  
