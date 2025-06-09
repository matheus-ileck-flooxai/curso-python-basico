"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    Append = Adiciona um item ao final
    insert = Adiciona um item no índice escolhido
    pop = Remove do final ou do índice escolhido
    del = apaga um índice
    clear = limpa a lista
    extend = estende a lista
    + = concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (crud)
"""

lista = [10,20,30,40]

lista.append('Matheus')
nome = lista.pop()
lista.append(1234)
del lista[-1]
lista.insert(100,5)

print(lista[4])