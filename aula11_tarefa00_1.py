pessoa = {"nome": "Papagaio", "idade": 49, "cidade": "Petrópolis"}
print (f"Dados da pessoa: {pessoa}")

pessoa["idade"]=48
print(f"Dados atualizados: {pessoa}")

pessoa["email"]="luis.rodrigo.net@gmail.com"
print(f"Dados atualizados: {pessoa}")

pessoa["sexo"]="m"
print(f"Dados atualizados: {pessoa}")

del pessoa["nome"]
del pessoa["email"]
print(f"Dados atualizados: {pessoa}")