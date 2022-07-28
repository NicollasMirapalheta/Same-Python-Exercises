cont = 0
cont1 = 0
dict = {"Nome": ["Numero"]} #Dicionario
lista = [] #lista vazia
while cont == 0: #Estrutura de repetição
    n1 = str(input('Digite o nome do contato:')) #Variaveis
    n2 = str(input('Digite o numero do contato:'))#Variaveis
    lista.append(n2) #Adiciona a variavel n2 na lista
    while cont1 == 0:#Estrutura de repetição
        stop1 = input('Deseja continuar adicionando numeros?[S/N] ').upper() #Verifica se deseja continuar
        if stop1 == "N":
            cont1 = 1
        else:
            n2 = str(input('Digite o numero do contato:'))
            lista.append(n2) #Adiciona mais um item na lista
    dict[n1] = lista #Adiciona a lista ao dicionario e cria a chave baseado no n1 e o conteudo nos elementos da lista
    lista = [] #Esvazia a lista para fazer um novo contato
    stop = str(input('Deseja continuar adicionando contatos?[S/N] ').upper()) #Verificação para ver
                                                                             # se deseja adicionar mais um contato
    cont1 = 0
    if stop == "N":
        cont = 1

print('''
+++++++++++++++++++++++++++++++
Relatorio da agenda de contatos
+++++++++++++++++++++++++++++++

{}


'''.format(dict)) #Relatorio com os nomes adicionados e os numeros de seus respectivos contatos