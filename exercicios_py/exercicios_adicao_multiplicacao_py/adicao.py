from datetime import datetime


def plus(valor, valor1):
    start_time = datetime.now()

    valor = str(valor)
    valor1 = str(valor1)
    cont = 0
    cont1 = 0
    lista = [[], [], []]
    if len(valor) != len(valor1):
        if len(valor) > len(valor1):
            vazios = len(valor) - len(valor1)
            for i in range(vazios):
                lista[1].append(0)
        else:
            vazios = len(valor1) - len(valor)
            for i in range(vazios):
                lista[0].append(0)

    for i in range(len(valor)):
        lista[0].append(int(valor[cont]))
        cont = cont + 1
    for i in range(len(valor1)):
        lista[1].append(int(valor1[cont1]))
        cont1 = cont1 + 1
    print("""
              {}
            + {}
            ---------------------------------------------------------
    """.format(lista[0], lista[1]))
    cont = 1
    cont1 = 1
    verificador = True
    resto = 0
    while verificador is True:
        lista[2].append(lista[0][len(lista[0]) - cont] + lista[1][len(lista[1]) - cont1] + resto)
        print("""
              {}
            + {}
            ---------------------------------------------------------
              {}
            """.format(lista[0], lista[1], lista[2]))
        resto = 0
        if lista[2][cont-1] >= 10 and cont <= len(lista[2]):
            lista[2][cont-1] = lista[2][cont-1] - 10
            resto = 1
        cont = cont + 1
        cont1 = cont1 + 1
        if cont > len(lista[1]):
            verificador = False
    cont = 0
    listamemoria = lista[2]
    lista[2] = []
    while cont < len(listamemoria):
        lista[2].append(listamemoria[(len(listamemoria) - 1) - cont])
        cont = cont + 1
    print("""
             {}
           + {}
           ---------------------------------------------------------
             {}
           """.format(lista[0], lista[1], lista[2]))
    cont = 1
    resposta = str(lista[2][0])
    for i in range(len(lista[2]) - 1):
        resposta = resposta + str(lista[2][cont])
        cont = cont + 1
    print('Resposta: {}'.format(resposta))
    end_time = datetime.now()
    print(f'Tempo de execução: {(end_time - start_time)}')


plus(27284761162726447616, 63562426624264356242)
