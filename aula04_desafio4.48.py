lado01 = float(input("Digite o primeiro número: "))
lado02 = float(input("Digite o segundo número: "))
lado03 = float(input("Digite o terceiro número: "))

if lado01 + lado02 > lado03 and lado01 + lado03 > lado02 and lado02 + lado03 > lado01:
    print("Esses números podem formar um triângulo!")

else:
    print("Esses números não podem formar um triângulo!")
