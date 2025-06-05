"""
Introdução ao try/except
try -> Tenta executar o código.
except -> Ocorreu algum erro ao tentar executar

"""

numero_str = input('Vou dobrar o número que vc digitar: ')

try: 
    numero_float = float(numero_str)
    print('Float', numero_float)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except:
    print('Isso não é um número')