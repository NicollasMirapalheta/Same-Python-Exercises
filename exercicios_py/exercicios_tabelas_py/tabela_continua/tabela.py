class TabelaContinua:
    def __init__(self, tamanho_max):
        self.__chave = [None] * (tamanho_max)
        self.__valor = [None] * (tamanho_max)
        self.__tamanho_max = tamanho_max - 1
        self.__pos_atual = -1
    
    def __len__(self):
        return self.__pos_atual + 1

    def __str__(self):
        chaves = [chave for chave in self.__chave]
        valores = [valor for valor in self.__valor]
        mensagem = f'Chaves: {str(chaves)}\nValores: {str(valores)}'
        return mensagem
    
    def getKey(self, index):
        try:
            return self.__chave[index]
        except Exception as e:
            raise e
    
    def getValue(self, chave):
        index = self.find(chave)
        if not(index == -1):
            return self.__valor[index]

    def __setitem__(self, chave, elemento):
        index = self.find(chave)
        if not(index == -1):
            self.__valor[index] = elemento
        

    def __full(self):
        return self.__pos_atual >= self.__tamanho_max
    
    def __empty(self):
        return self.__pos_atual == -1

    def append(self, chave, valor):
        if(self.__full()):
            raise OverflowError("Não tem mais espaço para adicionar um novo elemento!")
            
        if(chave in self.__chave):
            raise ValueError("A chave já está cadastrada!")
        
        self.__pos_atual += 1

        if(self.__pos_atual == 0):
            self.__chave[self.__pos_atual] = chave
            self.__valor[self.__pos_atual] = valor
        else:
            pos = 0
            AUXtamanho = self.__pos_atual
            while True:
                if(chave < self.__chave[pos]):
                    while AUXtamanho > pos:
                        self.__chave[AUXtamanho] = self.__chave[AUXtamanho - 1]
                        self.__valor[AUXtamanho] = self.__valor[AUXtamanho - 1]
                        AUXtamanho -= 1
                    self.__chave[pos] = chave
                    self.__valor[pos] = valor
                    break
                pos += 1
                if(self.__chave[pos] == None):
                    self.__chave[pos] = chave
                    self.__valor[pos] = valor
                    break



    def find(self, chave):
        comeco = 0
        final = self.__pos_atual + 1
        index = -1

        while comeco < final:
            meio = (comeco + final) // 2
            if(self.__chave[meio] == chave):
                index = meio
                break
            else:
                if(chave < self.__chave[meio]):
                    final = meio
                else:
                    comeco = meio
            if(meio == 0):
                break
        
        return index

    def remover(self, chave):
        if not(self.__empty()):
            index = self.find(chave)
            if(index == -1):
                raise ValueError("Chave não encontrada!")
            while index < self.__pos_atual:
                self.__chave[index] = self.__chave[index + 1]
                self.__valor[index] = self.__valor[index + 1]
                index += 1
            self.__chave[self.__pos_atual] = None
            self.__valor[self.__pos_atual] = None
            self.__pos_atual -= 1

    def destroy(self):
        for i in range(self.__pos_atual + 1):
            self.__chave[i] = None
            self.__valor[i] = None
            self.__pos_atual -= 1