a = float(input(f"Qual o valor de a? : "))
b = float(input(f"Qual o valor de b? : "))
c = float (input(f"Qual o valor de c? : "))

delta = b**2 - 4*a*c

x1= (-b + delta**1/2) / 2*a
x2= (-b - delta**1/2) / 2*a

print(f"O valor de x1 é :{x1}")
print(f"O Valor de x2 é :{x2}")