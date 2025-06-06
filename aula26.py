"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto" se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""


try:
    NOME_USUARIO = input("Digite seu nome: ")

    tamanho_nome_usuario = len(NOME_USUARIO)

    if(tamanho_nome_usuario <= 4):
        print('Seu nome é curto')

    elif(tamanho_nome_usuario >= 5 and tamanho_nome_usuario <=6):
        print('Seu nome é normal')

    elif(tamanho_nome_usuario > 6):
        print('Seu nome é muito grande')

    else:
        print('Você digitou um valor inválido')

except:
    print('Você digitou um valor inválido')