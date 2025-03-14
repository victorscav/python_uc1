nome=(input("Qual o seu nome? "))
senha=(input("Qual a sua senha? "))

if len(nome) < 3:
    print("Erro: O usuário tem deve ter pelo menos 3 letras.")

elif len(senha) < 6:
    print("Erro: A senha deve ter pelo menos 6 letras.")

elif senha == ("123456") or senha == ("senha"):
    print("Erro: Essa senha é muito fraca!")

else:
    print("Cadastro realizado com sucesso!")