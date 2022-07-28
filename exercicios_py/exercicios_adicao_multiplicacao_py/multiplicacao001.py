def mult(valor, valor1):
    x = 0
    if (valor % 2) == 1:
        x = valor1
    while valor >= 1:
        if (valor % 2) == 0:
            valor = round((valor / 2))
        else:
            valor = round((valor / 2) - 0.5)
        valor1 = (valor1 * 2)
        if (valor % 2) == 1:
            x = x + valor1
    print(x)


mult(3, 20)
