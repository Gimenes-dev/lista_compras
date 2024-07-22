lista = []

while True:
    print('(A)dicinar | (R)emover | (L)istar')
    comando = input('Digite oque deseja: ')

    if comando.lower() == 'a':
        item = input('Digite o nome do Item: ')
        if item != '':
            lista.append(item)
            print('item adicionado a sua lista.')
        else:
            print('Você não digitou nome do item!')
    elif comando.lower() == 'r':
        indice = input('Qual indice do Item que deseja Remover: ')
        if int(indice) < len(lista):
            lista.pop(int(indice))
            print('Item removido com Sucesso.')
    elif comando.lower() == 'l':
        if len(lista) > 0:
            print(list(enumerate(lista)))
        else:
            print('Nenhum item encontrado!')
    else:
        print('opção incorreta.')
        continue