entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')


senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')



print('123' in senha_permitida)
print('123' not in senha_permitida)

    
