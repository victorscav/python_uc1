nome = input("Qual seu nome?")
idade = float(input("Qual a sua idade? "))
pais = input("Está acompanhada dos pais? <s/n>:")

lista_banidos= "victor" "carlos" "fernando" "josé"

if nome in lista_banidos:
    print("Voce está banido de entrar da festa!")

else:
    if (idade>=18) or pais == "s":
        print("Acesso liberado!")
    else:
        print("Acesso negado")
