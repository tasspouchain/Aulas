nota1 = float(input("digite uma nota: "))
nota2 = float(input("digite uma nota: "))
nota3 = float(input("digite uma nota: "))
notas = [nota1, nota2, nota3]
print(notas)

soma_tudo = sum(notas)
media = (soma_tudo / 3)
print(media)

notas.remove(min(notas))
print(notas)
nota1 = float(input("digite outra nota: "))
notas.append(nota1)
print(notas)

notas.sort()
print(notas)

soma_dnv = sum(notas)
nova_media = (soma_dnv / 3)
print(nova_media)