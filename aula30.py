frase = 'O python é uma linguagem de programação multiparadigma.'\
        'Python foi criado por Guido van Rossum'

contador = 0
maior_letra = 0
letra_apareceu_mais_vezes = ''

while contador < len(frase):

    letra_atual = frase[contador]

    if letra_atual == ' ':
        contador += 1

        continue

    conta_letras = frase.count(letra_atual)

    if maior_letra < conta_letras:
        maior_letra = conta_letras
        letra_apareceu_mais_vezes = letra_atual
    
    contador += 1

print(f'A letra que mais apareceu é "{letra_apareceu_mais_vezes}" que apareceu {maior_letra}x')