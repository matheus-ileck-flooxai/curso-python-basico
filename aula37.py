"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice,nome in enumerate(lista):
    indice, nome = item
    print(indice, nome)
 

# for tupla_enumerada in enumerate(lista):
#     print('For da tupla: ')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')