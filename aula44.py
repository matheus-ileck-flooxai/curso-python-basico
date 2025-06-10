import random


nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))
soma_numeros_cpf = 0
multiplicador_de_digitos = 10

for numero in nove_digitos:

    soma_numeros_cpf += int(numero) * multiplicador_de_digitos
    multiplicador_de_digitos-= 1

resultado = (soma_numeros_cpf * 10) % 11
resultado = resultado if resultado <= 9 else 0

dez_digitos = nove_digitos + str(resultado)
multiplicador_de_digitos = 11

 

resultado_digito_2 = 0
for numero in dez_digitos:
    resultado_digito_2 += int(numero) * multiplicador_de_digitos
    multiplicador_de_digitos -= 1
    
resultado_digito_2 = (resultado_digito_2 * 10) % 11

novo_cpf = f'{nove_digitos}{resultado}{resultado_digito_2}'


print(novo_cpf)