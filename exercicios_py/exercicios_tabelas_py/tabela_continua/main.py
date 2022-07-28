from tabela import TabelaContinua

tabela = TabelaContinua(5)
tabela.append("banana", "Olá")
tabela.append("abacate", "Olá")
tabela.append("carro", "Olá")
tabela.append("13", "Olá")
tabela.append("00", "Olá")
print(tabela)
print()

tabela.remover("13")
print(tabela)
print()

print(tabela.find("banana"))
print()

tabela.destroy()
print(tabela)