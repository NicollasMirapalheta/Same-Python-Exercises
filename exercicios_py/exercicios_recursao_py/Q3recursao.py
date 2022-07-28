def fibonacci(numerador):                            
    if numerador <=1:                                 
        return numerador                                                                 
    return fibonacci(numerador - 1) + fibonacci(numerador - 2)     

numerador = int(input(""))
print(fibonacci(numerador))