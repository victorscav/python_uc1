lado1= float(input("Informe o valor do primeiro lado: "))
lado2= float(input("Informe o valor do segundo lado: "))
lado3= float(input("Informe o valor do terceiro lado: "))

if (lado1 == lado2 == lado3):
    print("Esse é um triângulo equilátero!")

elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
    print("Esse é um triângulo isósceles!")

else:
    print("Esse é um triângulo escaleno!")