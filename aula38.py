"""
Faça uma lista de compras com listas
- O usuário deve ter a possibilidade de:
- inserir, apagar e listar valores da sua lista
- Não permita que o programe quebre com erros de índices inexistentes na lista
"""
lista = []
while True:
    try:
        opcao_inicial = input('Selecione uma opção  \n[I]nserir [A]apagar [L]listar: ').upper()

        if len(opcao_inicial) > 1:
            print('Por favor digite apenas uma letra.')
            continue

        if opcao_inicial == 'I':
            novo_item = input('Digite o nome do novo item: ')
            lista.append(novo_item)

        elif opcao_inicial == 'A':
            if len(lista) >= 1:
                for i, val in enumerate(lista):
                    print(f'Indice: {i + 1}, nome: {lista[i]}')
                    indice_para_remover_item = input('Digite o índice que deseja remover: ')
                    
                    indice_para_remover_item_int = int(indice_para_remover_item)

                    if indice_para_remover_item.isnumeric:
                        indice_para_remover_item_int - 1
                        lista.pop(indice_para_remover_item_int - 1)
                        print('Item removido com sucesso!')
                    else:
                        print('Por favor digite um número valido')
                        continue
            else:
                    print('Você não possui nenhum item ainda.')
                    continue
        elif opcao_inicial == 'L':
             if len(lista) >= 1:
                for i, val in enumerate(lista):
                    print(f'Indice: {i + 1}, nome: {lista[i]}')
             else:
                    print('Você não possui nenhum item ainda.')
                    continue
        else:
            print('Por favor digite um valor válido.')

    except IndexError as e:
        print('Por favor digite somente os indices exibidos.')

    except:
        print('Ocorreu um erro.')
 
