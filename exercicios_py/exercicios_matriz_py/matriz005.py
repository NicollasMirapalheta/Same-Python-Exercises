arq = open('dados.txt', 'r')  # abre o arquivo
text = []  # declaro um vetor
matriz = []  # declaro um segundo vetor
texto = arq.readlines()  # quebra as linhas do arquivo em vetores
print("")

for i in range(len(texto)):  # esse for percorre a posições dp vetor texto
    matriz.append(texto[i].strip('\n').split(';'))  # aqui eu quebro nos espasos das palavras

print("")

for i in range(len(texto)):  # mostra quedrando em linhas
    print(matriz[i])

arq.close()  # comando para fechar o arquivo
# Nomes
nome1 = matriz[0][0]
nome2 = matriz[1][0]
nome3 = matriz[2][0]
# Codigo de registro
cod1 = matriz[0][1]
cod2 = matriz[1][1]
cod3 = matriz[2][1]
# Compras client1
compra_0_1 = float(matriz[0][2])
compra_0_2 = float(matriz[0][3])
compra_0_3 = float(matriz[0][4])
# Compras client2
compra_1_1 = float(matriz[1][2])
compra_1_2 = float(matriz[1][3])
compra_1_3 = float(matriz[1][4])
# Compras client3
compra_2_1 = float(matriz[2][2])
compra_2_2 = float(matriz[2][3])
compra_2_3 = float(matriz[2][4])

# Valores totais de compras de cada cliente
total1 = compra_0_1 + compra_0_2 + compra_0_3
total2 = compra_1_1 + compra_1_2 + compra_1_3
total3 = compra_2_1 + compra_2_2 + compra_2_3
print('''
++++++CLIENTE 1++++++

Nome: {}

N° de registro: {}

1° compra valor: R${:.2f}
2° compra valor: R${:.2f}
3° compra valor: R${:.2f}

Valor total gasto: R${:.2f}
'''.format(nome1, cod1, compra_0_1, compra_0_2, compra_0_3, total1))

if total1 >= 1000: #Verificação se é vip ou não
    print(" /\/\/\/\/\//\/=====VIP=====\/\/\/\/\//\/\ ")

print('''
++++++CLIENTE 2++++++

Nome: {}

N° de registro: {}

1° compra valor: R${:.2f}
2° compra valor: R${:.2f}
3° compra valor: R${:.2f}

Valor total gasto: R${:.2f}
'''.format(nome2, cod2, compra_1_1, compra_1_2, compra_1_3, total2))

if total2 >= 1000:
    print(" /\/\/\/\/\//\/=====VIP=====\/\/\/\/\//\/\ ")#Verificação se é vip ou não

print('''
++++++CLIENTE 3++++++

Nome: {}

N° de registro: {}

1° compra valor: R${:.2f}
2° compra valor: R${:.2f}
3° compra valor: R${:.2f}

Valor total gasto: R${:.2f}
'''.format(nome3, cod3, compra_2_1, compra_2_2, compra_2_3, total3))

if total3 >= 1000:
    print(" /\/\/\/\/\//\/=====VIP=====\/\/\/\/\//\/\ ")#Verificação se é vip ou não
