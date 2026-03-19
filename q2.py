a = int(input("digite um numero: "))
b = int(input("digite um numero: "))
c = int(input("digite um numero: "))
d = int(input("digite um numero: "))
lista = [a, b, c, d]
print(lista)

numero_alvo = int(input("digite mais um numero: "))
print(numero_alvo)

lista.remove(numero_alvo)
print(len(lista))