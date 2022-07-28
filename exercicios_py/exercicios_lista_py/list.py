class Node:
    #Cria o Nó
    def __init__(self,date):
        self.date = date
        self.next = None
class Lista:
    def __init__(self):
      self.head = None
      self._size = 0

    def __len__(self):
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range.")
        return pointer

    #Pega um elem da lista
    def __getitem__(self,index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.date
        raise IndexError("the index out of range.")

    #Mostrar a lista
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.date) + "--> "
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

    #Mostrar a posição do elemento
    def posicao(self,elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.date == elem:
                return i + 1
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} not in list".format(elem))

    #Mostra a posição do elemento de forma recursiva
    def posicao(self,elem,i,pointer=0):
        if i == 0:
            pointer = self.head
        if pointer.date == elem:
            return i + 1
        else:
            pointer = pointer.next
            return self.indexR(elem,i+1,pointer)

    #Inserir um elemento em uma posição
    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1
    
    #Remover um elem de uma posição da lista
    def remove(self, index):
        if self.head == None:
            raise ValueError("the list is empty.")
        elif index == 0:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            i = 1
            while(pointer):
                if i == index:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
                i = i + 1
        raise ValueError("the index {} not exist in the list.".format(index+1))
    #Destroi a lista
    def destruir(self):
        self.head = None