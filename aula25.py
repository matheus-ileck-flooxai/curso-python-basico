"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa Noite 18-23.

"""

try:
    hora_str = input('Digite a hora: ')
    hora_int = int(hora_str)

    if(hora_int >= 0 and hora_int <= 12):
        print('Bom dia!')
    elif(hora_int >= 13 and hora_int <= 17):
        print('Boa tarde!')
    elif(hora_int >= 18 and hora_int <= 23):
        print('Boa noite!')
    else:
        print('Você não digitou um número valido.')
  

except:
    print('Você não digitou um número valido.')

