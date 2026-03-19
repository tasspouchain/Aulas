pessoa = {"nome": "Tassia", "idade": 26}
print("nome da pessoa:", pessoa["nome"])
pessoa["cidade natal"] = "Fortaleza"
pessoa["idade"] = 26
print("pessoa atualizada", pessoa)


removido = pessoa.pop("idade")
print("valor removido (idade):", removido)

print("quantidade de chaves em 'pessoa':", len(pessoa))
print(list(pessoa.values()))
print(list(pessoa.items()))


prof = {"nome": "Caroline", "cidade": "Palhoça", "curso": "programação"}
print("nome da prof:", prof["nome"],"\n", "prof de que?:", prof["curso"])
