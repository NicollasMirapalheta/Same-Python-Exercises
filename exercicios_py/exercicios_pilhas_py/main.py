from continua import ContinuedStack
from encadeada import LinkedStack
from random import randint

size = 10
Pilha_continua = ContinuedStack(size)
Pilha_encadeada = LinkedStack()


def verificarIgualdade():
    while (not Pilha_encadeada.getLastItem() == None or not Pilha_continua.getLastItem() == None):
        if not(Pilha_continua.getLastItem() == Pilha_encadeada.getLastItem()):
            return False
        Pilha_continua.delLastItem()
        Pilha_encadeada.delLastItem()
    return True

for i in range(size):
    Pilha_continua.append(randint(1,10))  # cria numeros inteiros aleatorios, pode ser alterado.
    Pilha_encadeada.append(randint(1,10))  # cria numeros inteiros aleatorios, pode ser alterado.

print()
print(f'As pilhas são iguais? {verificarIgualdade()}')
print()
print(f"Pilhas continua\n{Pilha_continua}")
print()
print(f'Último valor da pilha continua: {Pilha_continua.getLastItem()}')
print()
Pilha_continua.delLastItem()
print('Deletando ultimo valor da pilha continua...')
print()
print(f'Último valor da pilha continua: {Pilha_continua.getLastItem()}')
print()
Pilha_continua.delall()
print('Tudo apagado.')
print()
print(f'Último valor da pilha continua: {Pilha_continua.getLastItem()}')
print()
print(f"Pilha Encadeada\n{Pilha_encadeada}")
print()
print(f'Último valor da pilha encadeada: {Pilha_encadeada.getLastItem()}')
print()
Pilha_encadeada.delLastItem()
print('Deletando ultimo valor da lista continua...')
print()
print(f'Último valor da pilha encadeada: {Pilha_encadeada.getLastItem()}')
print()
Pilha_encadeada.delall()
print('Tudo apagado.')
print()
print(f'Último valor da pilha encadeada: {Pilha_encadeada.getLastItem()}')