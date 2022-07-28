from datetime import datetime


def mult(valor, valor1):
    start_time = datetime.now()
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
    end_time = datetime.now()
    print(f'Tempo de execução: {end_time - start_time}')


mult(4834, 2356) 
