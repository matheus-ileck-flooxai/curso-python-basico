"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem
regressiva começando de 10

Somar todos os resultados
Multiplicar o resultado anterior por 10
Obter o resto da divisão da conta anterior por 11
se o resultado anterior for maior que 9:
    resultado é 0
Contrario disso?
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
import sys

entrada = input('Digite o CPF (ex: 746.824.890-70): ')

cpf_sem_ponto = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()


nove_digitos = cpf_sem_ponto[:9]
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

if cpf_sem_ponto == novo_cpf:
    print('Cpf é valido')
else:
    print('Cpf invalido')