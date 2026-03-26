peso = float(input("qual seu peso em kg?" ))
altura = float(input("qual sua altura em M?" ))
imc = peso / altura ** 2
print(imc)

if imc < 18.5: 
    categoria = "magreza"
elif imc < 25: 
    categoria = "normal"
elif imc < 30:
    categoria = "sobrepeso"
else:
    categoria = "obesidade"

print(f"imc = {imc:.2f} - {categoria}")
