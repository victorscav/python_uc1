nota01= float(input("Qual a nota da primeira prova?: "))
nota02= float(input("Qual a nota da segunda prova?: "))
trabalho_extra= input("Você fez um trabalho extra? <s/n>: ").lower()

media= (nota01 + nota02) / 2

if media >= 7 or trabalho_extra == "s":
    print("Aluno aprovado!")

else:
    print("Aluno reprovado!")