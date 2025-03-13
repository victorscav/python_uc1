idade = int(input("Qual a sua idade? "))
senha = input("Digite a sua senha: ").lower()

senha_correta = "1234"

if (idade >= 18) and (senha == senha_correta):
    print("Acesso Liberado!")

else:
    print("Acesso Negado!")