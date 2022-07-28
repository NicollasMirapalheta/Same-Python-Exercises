def soma(lista):
    if not lista:
        return 0  
    else:
        return (lista[0] + soma(lista[1:]))


lista = input("").split()
lista_n = [int(x) for x in lista if x.isdigit()]
print(soma(lista_n))