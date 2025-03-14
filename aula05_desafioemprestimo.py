nome_sujo= (input("Possui nome sujo? <s/n>: ")).lower()
renda= float(input("Qual a sua renda mensal? "))
idade= float(input("Qual a sua idade? "))

if (idade >= 21) and (renda >= 2000) and (nome_sujo == "n"):
    print("Você pode pedir um empréstimo!")


else:
    print("Voce não pode pedir um empréstimo!")