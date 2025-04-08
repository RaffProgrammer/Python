peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    condicao = "Abaixo do peso"
elif 18.6 <= imc <= 24.9:
    condicao = "Peso ideal (parabéns)"
elif 25.0 <= imc <= 29.9:
    condicao = "Levemente acima do peso"
elif 30.0 <= imc <= 34.9:
    condicao = "Obesidade grau I"
elif 35.0 <= imc <= 39.9:
    condicao = "Obesidade severa"
else:
    condicao = "Obesidade mórbida"

print("Seu IMC é:", round(imc, 2))
print("Condição:", condicao)
