lista = []
cont = 0
cont1 = 1
cont2 = 0
tam_list = 0
lista_vazia = []
reset = 1

init = int(input('''
Digite [1] para iniciar e criar uma lista de produtos vazia.
Digite [2] para iniciar e criar uma lista de produtos da sua escolha.

DIGITE A ALTERNATIVA: '''))  # Pede dados

while reset == 1:  # Estrutura de repetição
    if init == 1:  # Estrutura de condição onde eu crio uma lista com um numero x de listas vazias dentro
        for n in range(10):
            lista.append(lista_vazia)
    elif init == 2:
        while cont == 0:  # Adicionar produtos a lista
            x = str(input('Digite o produto a ser adicionado: '))
            lista.append(x)
            stop = str(input('Deseja adicionar mais?[S/N]').upper())
            if stop == "N":
                cont = 1
    init = 10
    print('''
!!!!!DIGITE!!!!!
[1]ADICIONAR UM PRODUTO NA LISTA
[2]REMOVER UM PRODUTO DA LISTA
[3]BUSCAR POSIÇÃO DO PRODUTO
[4]LIMPAR LISTA
[5]MOSTRAR LISTA
    ''')  # Determinar ações
    choice1 = int(input('OPÇÃO? '))
    if choice1 == 1:
        valor = str(input('Digite o nome do produto: '))
        choice2 = str(input('Deseja escolher a posição?[S/N]').upper())
        tam_list = len(lista)  # Le a quantidade de posições que tem na lista
        if choice2 == "S":
            choice3 = int(input('Deseja executar essa ação em qual posição da lista?'))
            if choice3 > tam_list:  # Quando o a posição for maior que o tamanho da lista, ele vai gerar listas
                # vazias para preencher esses espaços
                for n in range(choice3 - tam_list):
                    lista.append(lista_vazia)
            choice3 -= 1
            lista[choice3] = valor  # Adicionar o valor na posição (choice3) da lista
        else:
            while cont2 <= (len(lista)):
                if '' not in lista[cont2]:
                    lista[cont2] = valor
                    cont2 = (len(lista) + 2)
                else:
                    cont2 += 1
            if cont2 == (len(lista) + 1):
                lista.append(valor)  # Caso não escolha a posição, automaticamente vai adicionar no fim da lista
            cont2 = 0
    if choice1 == 2:  # Remove o produto da lista, para não afetar as posições posteriores, substitui por uma []
        choice2 = int(input('Deseja remover o produto de qual posição? ').upper())
        choice2 -= 1
        lista[choice2] = []
    if choice1 == 3:
        produto = str(input("Digite o nome do produto: "))
        while cont1 != 0:  # Verifica se tem o produto na lista, verificando posição por posição
            if produto in lista[cont1 - 1]:
                print('O produto {} está localizado na posição {} da lista.'.format(produto, cont1))
                cont1 = 0
            elif produto not in lista:  # Se não estiver na lista, aparece esse print e essa ação termina aqui
                print('O produto buscado não está na lista.')
                cont1 = 0
            else:
                cont1 += 1
        cont1 = 1
    if choice1 == 4:  # limpa a lista
        lista = lista_vazia
    if choice1 == 5:
        print(lista)  # Mostra a lista
    reset = int(input('Digite [1] para voltar pro inicio e [2] para finalizar:'))
