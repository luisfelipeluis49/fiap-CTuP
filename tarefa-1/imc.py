# This file will be written in portuguese
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))

imc = peso / (altura * altura)

print(f"Seu IMC é de {imc:.1f}")
