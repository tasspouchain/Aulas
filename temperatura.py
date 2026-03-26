temperatura = float(input("Quantos graus ºC faz em Palhoça agora? "))

if temperatura < 0:
    categoria = "melhor voltar p ceará"
elif temperatura < 10:
    categoria = "frio dms"
elif temperatura < 24:
    categoria = "clima ameno"
elif temperatura < 30:
    categoria = "quente pa dedeu"
else:
    categoria = "inferno na terra"

print(f"temperatura = {temperatura} - {categoria}")

