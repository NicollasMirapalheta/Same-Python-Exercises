matriz = []
#Parametros
qlinhas = int(input('Quantas linhas(L) gostaria que sua matriz tenha?'))
qcolunas = int(input('Quantas colunas(C) gostaria que sua matriz tenha?'))

for i in range(qlinhas):
    # Cria linha vazia
    linha = []
    for j in range(qcolunas):
        # Adiciona numeros na linha
        elem = int(input('Digite os numeros para cada espaço ['+str(i)+','+str(j)+']:'))
        linha.append(elem)
# Adiciona a linha na matriz
    matriz.append(linha)

print("Matriz informada:")

for i in range(len(matriz)):
    for j in range(len(matriz[i])): #Mostra a matriz separada em colunas e linhas
        print(matriz[i][j], end=" ")
    print()

# Encontrar o menor elemento
linha1 = 0
col1 = 0
linha2 = 0
col2 = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] < matriz[linha1][col1]:
            linha1 = i
            col1 = j
# Encontrar o maior elemento
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > matriz[linha2][col2]:
            linha2 = i
            col2 = j

print(f"Menor elemento: {matriz[linha1][col1]}")
print(f"Linha: {linha1}")
print(f"coluna: {col1}")
print('-'*40)
print(f"maior elemento: {matriz[linha2][col2]}")
print(f"Linha: {linha2}")
print(f"coluna: {col2}")
