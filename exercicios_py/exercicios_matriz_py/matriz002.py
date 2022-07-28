# Preencher a matriz por leitura

turma = []
for i in range(3):
    # cria linha vazia
    linha = []
    for j in range(3):
        # adiciona as notas na linha
        elem = int(input('Digite a nota [' + str(i) + ',' + str(j) + ']:')) # Recebe 1 valor inteiro por vez
        linha.append(elem)
    # adiciona a linha na matriz turma
    turma.append(linha)
print(turma) # Mostra a matriz na linha
