class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
    
    def verificaVazia(self):
        return self.top == None

    def append(self, dado):
        new = Node(dado)
        if not(self.verificaVazia()):
            new.next = self.top
        self.top = new

    def getLastItem(self):
        if not(self.verificaVazia()):
            return self.top.data

    def delLastItem(self):
        if not(self.verificaVazia()):
            self.top = self.top.next       
  
    def delall(self):
        while not(self.verificaVazia()):
            self.delLastItem()
    
    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
        
    def __str__(self):
        return self.__repr__()

    def mostrarLista(self):
        return self.__repr__()

