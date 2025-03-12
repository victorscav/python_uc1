compra= float(input("Digite o valor da sua compra: "))

if compra > 500:
    desconto = 0.15

elif 200 <= compra <= 500:
    desconto = 0.10

elif compra < 200:
    desconto = 0.05

compra_desconto = compra * desconto

compra_final = compra - compra_desconto

print((f"o valor da compra com desconto é R${compra_final:.2f}"))
