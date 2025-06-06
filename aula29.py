"""Calculadora com while"""



try:
    while True:
        
        primeiro_numero_str = input('Digite o primeiro número: ')
        segundo_numero_str = input('Digite o segundo número: ')
        operador = input('Digite o operador da conta (+ - * /):  ')
        operadores_permitidos = '+-/*'

        primeiro_numero_int = int(primeiro_numero_str)
        segundo_numero_int = int(segundo_numero_str)

        if operador not in operadores_permitidos:
            print('Operador Inválido.')
            continue
        
        if len(operador) > 1:
            print('Por favor digite apenas um operador.')
            continue

        if operador == '+':
            print(f'{primeiro_numero_int} + {segundo_numero_int} = {primeiro_numero_int + segundo_numero_int} ')
        
        elif operador == '-':
            print(f'{primeiro_numero_int} - {segundo_numero_int} = {primeiro_numero_int - segundo_numero_int} ')

        elif operador == '*':
            print(f'{primeiro_numero_int} * {segundo_numero_int} = {primeiro_numero_int * segundo_numero_int} ')

        elif operador == '/':
            print(f'{primeiro_numero_int} / {segundo_numero_int} = {primeiro_numero_int // segundo_numero_int} ')






        sair = input('Deseja continuar [S] [N]? ').upper()
       
        if sair == 'S':
            continue
        elif sair == 'N':
            print('Encerrando...')
            break

except:
    print('Você não digitou um valor valido.')