class Tabela:
    def __init__(self, tamanhoMax):
        self.chave = [None] * (tamanhoMax + 1)
        self.valor = [None] * (tamanhoMax + 1)
        self.li = 1
        self.ls = tamanhoMax
        self.ini = self.li - 1
        self.fim = self.li + 1
    
    def __repr__(self):
        string = ""
        if (not self.vazia()):
            for i in range(self.ini, self.fim + 1):
                string = string + str(self.chave[i]) + ": " + str(self.valor[i]) + "\n"
        return string + "\n"

    def vazia(self):
        return self.ini < self.li or self.fim > self.ls
    
    def cheia(self):
        return (self.ini == self.li and self.fim == self.ls)
    
    def tamanho(self):
        if not self.vazia():
            return self.fim - self.ini + 1
        else:
            return 0
    
    def buscar(self, chave):
        if (not self.vazia()):
            for i in range(self.ini, self.fim + 1):
                if (self.chave[i] == chave):
                    return i
        return 0

    def inserir(self, chave, valor):
        posicao = self.buscar(chave)
        if (posicao > 0):
            self.valor[posicao] = valor
        elif (not self.cheia()):
            if (self.vazia()):
                self.ini = self.li
                self.fim = self.li
            else:
                self.fim += 1
            self.chave[self.fim] = chave
            self.valor[self.fim] = valor

    def inserirOrd(self, chave,valor):
        posicao = self.buscar(chave)
        if (posicao > 0):
            self.valor[posicao] = valor
            return
        if (self.vazia()):
            if (self.vazia()):
                self.ini = self.li
                self.fim = self.li
                self.chave[self.fim] = chave
                self.valor[self.fim] = valor
            return
        if (not self.vazia()):
            for i in range(self.ini, self.fim + 1):
                if (str(self.chave[i]) > str(chave)):
                    chack = i
                    for i in range(i,self.fim + 1):
                        self.chave[i + 1] = self.chave[i]
                        self.valor[i + 1] = self.valor[i]
            self.fim += 1
            self.chave[chack] = chave
            self.valor[chack] = valor 

    def buscarBinaria(self, chave):
        if (not self.vazia()):
            if self.chave[1] == chave:
                return 1
            i = int(self.fim / 2)
            i1 = 0
            while str(self.chave[i]) != str(chave):
                if self.chave[i] != chave:
                    i1 = i
                    i = int(i + (i / 2))
                else:
                    i1 = i
                    i = int(i - (i / 2))
            return
            
        return 0

    def consultar(self, chave):
        posicao = self.buscar(chave)
        if (posicao > 0):
            return self.valor[posicao]
    
    def excluir(self, chave):
        posicao = self.buscar(chave)
        if (posicao > 0):
            for i in range(posicao,self.fim):
                self.chave[i] = self.chave[i + 1]
                self.valor[i] = self.valor[i + 1]
            self.fim -= 1

    def destruir(self):
        self.ini = self.li - 1
        self.fim = self.ls + 1