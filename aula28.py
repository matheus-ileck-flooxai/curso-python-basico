"""
Iterando string com while
"""

nome = input('Digite seu Nome: ')

TAMANHO_NOME = len(nome)

contador = 0

while contador <= TAMANHO_NOME - 1:
    print(nome[contador], end='')
    contador +=1 
