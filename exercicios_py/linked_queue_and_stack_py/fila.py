from random import randint
# linked queue or Fila linkada

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.ini = None
        self.end = None
    
    def vazia(self):
        return self.ini == None

    def insert(self, elem):
        new = Node(elem)
        if self.vazia():
            self.ini = new
        else:
            self.end.next = new
        self.end = new
    
    def excluir(self):
        if (not self.vazia()):
            self.ini = self.ini.next

    def verifica(self):
        if (not self.vazia()):
            return self.ini.data

    def destruir(self):
        while (not self.vazia()):
            self.excluir()
    
    def __repr__(self):
        r = "["
        pointer = self.ini
        while(pointer):
            r = r + (" --> " + str(pointer.data))
            pointer = pointer.next
        r = r + "]"
        return r
    
    def randomQueue(self):
        for i in range(0,9):
            self.insert(randint(0,10))