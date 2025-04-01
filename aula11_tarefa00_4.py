aluno_1 ={"nome": "Victor", "notas":[8.3, 9.4, 7.5]}
aluno_2 ={"nome": "Felipe", "notas":[9.3, 7.7, 8.2]}
aluno_3 ={"nome": "Fernando", "notas":[7.6, 8.7, 9.2]}

print (f"Dados do aluno 1: {aluno_1}")

print (f"As notas do aluno {aluno_1["nome"]} são {aluno_1["notas"]}")

media = sum (aluno_1["notas"]) / len (aluno_1["notas"])
print(f"O aluno {aluno_1["nome"]} obteve média igual a: {media}")

aluno_1["media"]=media
print(f"Dados do aluno {aluno_1["nome"]} atualizados: {aluno_1}")

