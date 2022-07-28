class Table:
    def __init__(self):
        self.chave = [None]*11
        self.valor = [None]*11
        self.size = 0

    def __repr__(self):
        text = ""
        if (self.size > 0):

            for i in range(1,self.size+1):
                text = text + str(self.chave[i]) + ": " + str(self.valor[i] + "\n")
            return text 
            
        return "0"
    
    def __len__(self):
        return self.size

    #Busca Linear
    def buscaLinear(self,chave):
        if(self.size > 0):
            for i in range(1,self.size + 1):
                if(self.chave[i] == chave):
                    return i
        return 0

    #Busca Linear Recursiva
    def buscaLinear_R(self,chave,i=0):
        if(self.chave[i] == chave):
                    return i
        if i == self.size:
            return 'Item not found'
        else:
            return self.buscaLinear_R(chave,i+1)

    #Busca Binaria
    def buscaBinaria(self,chave):
        inicio = 1
        fim = self.size
        if self.size >= 1:
            meio = (inicio + fim ) //2
            if chave < self.chave[meio]:
                while chave < self.chave[meio]:
                    fim = meio
                    meio = (inicio + fim ) //2
                    fim = meio
                   
                    if (self.chave[meio + 1]) == self.chave[self.size] and self.chave[meio] != chave:
                        meio += 1
                        break
                    if (self.chave[meio] == 1 and self.chave[self.size] == chave):
                        meio += 1
                        break
            elif chave > self.chave[meio]:
                inicio = meio
                while chave > self.chave[meio]:
                    meio = (inicio + fim ) //2
                    inicio = meio
                    if (self.chave[meio + 1]) == self.chave[self.size] and self.chave[meio] != chave:
                        meio += 1
                        break
            return meio
             
        else:
            return 0

    #busca Binaria Recursiva
    def buscaBinaria_R(self,inicio,fim,chave):
        if inicio <= fim:
            meio = (inicio + fim)//2
            if chave > self.chave[meio]:
                return self.buscaBinaria_R(meio+1,fim,chave)
            elif chave < self.chave[meio]:
                return self.buscaBinaria_R(inicio,meio-1,chave)
            else:
                return meio
        return 0

    #Escolhe qual busca deseja fazer(Binaria ou Linear)
    def buscar(self,chave,opt):
        if(opt == 'Linario'):
            return self.buscaBinaria(chave)
        elif(opt == 'Linear'):
            return self.buscaLinear(chave)
        else:
            return 'Invalid option!'

    #Escolhe qual busca recursiva deseja fazer(Binaria ou Linear)
    def buscar_R(self,chave,opt):
        if(opt == 'Binario'):
            return self.buscaBinaria_R(1,self.size,chave)
        elif(opt == 'Linear'):
            return self.buscaLinear_R(chave)
        else:
            return 'Invalid option!'
    #Adiciona na tabela
    def inserir(self,chave, valor):
        op = 'binario'
        posicao = self.buscar(chave,op)
        if(posicao > 0):
            self.valor[posicao] = valor
        elif(self.size < 10):
            if (self.size == 0):
                self.size +=1
                self.chave[self.size] = chave
                self.valor[self.size] = valor
            elif(chave > self.chave[self.size]):
                self.size +=1
                self.chave[self.size] = chave
                self.valor[self.size] = valor
            else:
                for i in range(1,self.size+1):
                    if (chave < self.chave[i]):
                        self.chave[i+1] = self.chave[i]
                        self.valor[i+1] = self.valor[i]
                        self.chave[i] = chave
                        self.valor[i] = valor
                self.size +=1
    #Exclui um valor da tabela
    def excluir(self,chave):
        opt = input("Digite qual tipo buscar você deseja utilizar:")
        posicao = self.buscar(chave,opt)     
        if(posicao > 0):
            for i in range(posicao,self.size+1):
                self.chave[i] = self.chave[i+1]
                self.valor[i] = self.valor[i+1]
            self.size -=1
    #Destroi a tabela
    def destruir(self):
        self.size = 0
