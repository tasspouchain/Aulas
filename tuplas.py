coordenadas = (10, 20)
dias = ("segunda", "terça", "quarta", "quinta", "sexta")

print("X:", coordenadas [0], "| Y:", coordenadas[1])
print("Primeiros 3 dias: ", dias[:3])
print("tamanho da tupla 'dias:", len(dias))
print("Tem 'segunda'?", "segunda" in dias)
print("contagem de 'terça':", dias.count("terça"))
print("índice de 'quarta':", dias.index("quarta"))



dias = ("sábado", "domingo")
print("todos os dias:", dias)
print("tem 'quinta'?", "quinta" in dias)
print("índice de 'sábado':", dias.index("sábado"))