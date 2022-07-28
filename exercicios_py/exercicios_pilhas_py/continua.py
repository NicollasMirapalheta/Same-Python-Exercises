class ContinuedStack:
    def __init__(self, size = 10):
        self.__comeco = 0
        self.__final = size
        self.__top  = -1
        self.__valores = [None] * self.__final

    def delall(self):
        for i in range(self.__final):
            self.__valores[i] = None
        self.__top = -1

    def verificaVazia(self):
        return self.__top >= self.__comeco

    def getLastItem(self):
        if(self.verificaVazia):
            return self.__valores[self.__top]
        return None

    def delLastItem(self):
        if(self.verificaVazia):
            self.__valores[self.__top] = None
            self.__top -= 1

    def append(self, valor):
        if (self.__top <= self.__final):
            self.__top += 1
            self.__valores[self.__top] = valor

    def __repr__(self):
        r = ""
        cont1 = 9
        for i in range(self.__final):
            r = r + str(self.__valores[cont1]) + "\n"
            cont1 = cont1 - 1
        return r
        
    def __str__(self):
        return self.__repr__()