"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: Append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (crud)
"""

lista = [10,20,30,40]

lista.append(50)
lista.append(60)
lista.append(70)

ultimo_valor = lista.pop()

print(lista, 'Removido, ', ultimo_valor)