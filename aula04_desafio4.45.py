usuario = (input("Digite o nome de usuário: "))
senha = (input("Digite a sua senha: "))

if usuario == "admin": 
    if senha =="1234": 
        print("Acesso permitido.")

else:
    print("Acesso negado.")
