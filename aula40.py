"""
Split e join com list e str

split - divide uma string
join - une uma string
"""

frase = 'Olha só que, legal'
lista_frases_cruas = frase.split()

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

frases_unidas = '-'.join('abc')

print(lista_frases)
print(frases_unidas)