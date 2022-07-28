arq = open('dados_matriz003.txt', 'r')  # abre o arquivo
text = []  # declaro um vetor
matriz = []  # declaro um segundo vetor
texto = arq.readlines()  # quebra as linhas do arquivo em vetores
print("vetor texto -> ", texto)  # aqui eu mostro
print("")

for i in range(len(texto)):  # esse for percorre a posições dp vetor texto
    matriz.append(texto[i].split(';')) # aqui eu quebro nos espasos das palavras
print("vetor matriz -> ", matriz)  # mostra o vertor com um conjunto de vetores
print("")

for i in range(len(texto)):  # mostra quedrando em linhas
    print(matriz[i])
arq.close()  # comando para fechar o arquivo
