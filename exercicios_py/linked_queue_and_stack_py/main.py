from fila import LinkedQueue
from pilha import LinkedStack

pilha = LinkedStack()
pilha1 = LinkedStack()
fila = LinkedQueue()


#Função que ordena os numeros inteiros da fila

#Escolhi faz o exercicio trabalhando com uma fila encadeada e com 10 num int aleatorios

#Primeiro valor vai pra primeira pilha e então começa as verificações
#Depois de tudo ordenado, na primeira pilha, ta tudo do maior ao menor
#Então a função passa pra segunda pilha, assim inverte a ordem e depois passa direto pra fila, fazendo ficar de menor a maior, mas é opcional

#Escolhi criar uma função que cria valores inteiros aleatorios, so pra acelerar todo o processo, mas é possivel adicionar os valores manualmente

def organizeQueue():
    pilha.append(fila.verifica()) 
    fila.excluir()
    while not fila.vazia():
        while pilha.getLastItem() != None and fila.verifica() != None and pilha.getLastItem() > fila.verifica():
            pilha1.append(pilha.getLastItem())
            pilha.delLastItem()
        pilha.append(fila.verifica())
        fila.excluir()
        while not pilha1.verificaVazia():
            pilha.append(pilha1.getLastItem())
            pilha1.delLastItem()
    while not pilha.verificaVazia():
        pilha1.append(pilha.getLastItem())
        pilha.delLastItem()
    while not pilha1.verificaVazia():
        fila.insert(pilha1.getLastItem())
        pilha1.delLastItem()

fila.randomQueue()
print(fila)
organizeQueue()
print(fila)