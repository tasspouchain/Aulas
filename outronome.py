frutas = ["morango","mirtilo", "framboesa"]
numeros = [0, 1 , 2]
print("Nós temos: ")
print(frutas[0],",",frutas[1],"e",frutas[2])

print("minha fruta favorita é a", frutas[2],"!")

frutas[1] = "bluberry"
print("e pode-se dizer que mirtilo se chama:", frutas[1])

frutas.insert(3, "banana")
print("aliás, ficaria mais completa assim:", frutas)

frutas.remove("bluberry")
print("ou menos complicado, vamos ter apenas:", frutas)