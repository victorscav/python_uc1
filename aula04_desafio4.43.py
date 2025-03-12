a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
numero01 = int(a)
numero02 = int(b)

if numero01 > numero02:
    print(f"o maior numero é {numero01}!")

elif numero02 > numero01:
    print(f"O maior numero é {numero02}!")

else:
    print("Os números são iguais!")