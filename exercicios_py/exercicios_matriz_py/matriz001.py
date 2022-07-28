matriz1 = [[1, 4, 5], [3, 5, 7], [9, 1, 6]]
'''
[1, 4, 5]
[3, 5, 7]
[9, 1, 6]
'''
matriz2 = matriz1
n1 = matriz1[0][0]
n2 = matriz1[1][1]
n3 = matriz1[2][2]
num01 = int(input('Digite o numero pelo qual deseja multiplicar a diagonal principal: '))

mult1 = n1 * num01
mult2 = n2 * num01
mult3 = n3 * num01
continuar = str(input("Deseja continuar e mostrar a matriz anterior e a nova??[S/N] ")).upper()

if continuar == "S":
    matriz2 = matriz1[:]
    matriz2[0][0] = mult1
    matriz2[1][1] = mult2
    matriz2[2][2] = mult3
    print("""
    MATRIZ ANTIGA
    {}
    
    MATRIZ NOVA
    {}
    
    """.format(matriz1, matriz2))
else:
    print('Obrigado por comparecer!')
