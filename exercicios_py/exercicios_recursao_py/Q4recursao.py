def soma_dez(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + soma_dez(n // 10)

n = int(input(""))
print(soma_dez(n))