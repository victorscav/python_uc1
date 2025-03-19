soma = 0

while True:
    numero = float(input("Digite um número ou digite um número negativo para sair: "))
    soma += numero

    if numero < 0:
        break


print(f"A soma dos números positivos digitados é: {soma}")
