peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso / (altura ** 2)

print(f"o imc é : {imc:.2f} ")

if imc < 18.5:
    print("Você está abaixo do peso!")

elif 18.5 <= imc <= 24.9:
    print("Você está no peso ideal!")

elif 25 <= imc <= 29.9:
    print("Voce está em sobrepeso!")

else:
    print("Você está obeso!")