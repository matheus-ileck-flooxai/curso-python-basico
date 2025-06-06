"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, 
informe que não é um núimero inteiro.
"""
try:
    numero_str = input('Digite um número: ')
    numero_int = int(numero_str)

    verifica_numero_par_ou_impar = numero_int % 2 == 0
    
    if verifica_numero_par_ou_impar is True:
        print('Seu número é par.')
    else:
        print('Seu número é impar.')

except:
    print('Você não digitou um número inteiro.')



