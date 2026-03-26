aluna = input("nome da aluna: ")
nota_aluna = float(input("nota: "))

if nota_aluna < 5:
    categoria = "reprovada"
elif nota_aluna < 7:
    categoria = "recuperação"
elif nota_aluna < 9:
    categoria = "aprovada"
else:
    categoria = "aprovada com excelência"

print(f"nota_aluna = {nota_aluna} - {categoria}")