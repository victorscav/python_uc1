"""
Aula 09 - Atividade 01
"""
vet_dados = [50,74,105,220,220,2024]

"""
CRIAR E IMPRIMIR UMA LISTA (2 MANEIRAS)
"""
def criar_imprimir_lista():
    vetor=[15,2,94,30,8,76,2025]
    print (f"\n\tO conteúdo do vetor é: {vetor}\n")

def criar_imprimir_lista_v2(vetor):
    print (f"\n\tO conteúdo do vetor é: {vetor}\n")

"""
ITERAR E IMPRIMIR CADA ELEMENTO DO VETOR
"""
def iterando_lista(vet_dados):
    for elemento in vet_dados:
        print(f"\n\tO elemento do vetor é: {elemento}\n")

"""
SOMA DOS ELEMENTOS DE UM VETOR
"""
def soma_vetor(vet_dados):
    soma = sum(vet_dados)
    print(f"\n\tA soma dos elementos é: {soma} ")

"""
ENCONTRAR O MENOR E O MAIOR VALOR DE UM VETOR
"""
def maior_e_menor(vet_dados):
    maior = max(vet_dados)
    menor = min(vet_dados)
    print(f"\n\tO maior valor é: {maior}")
    print(f"\n\tO menor valor é: {menor}")

"""
INVERTER A ORDEM DOS ELEMENTOS DE UM VETOR
"""
def inverter_vetor(vet_dados):
    vetor_invertido = vet_dados[::-1]
    print(f"\n\tO valor do vetor invertido é: {vetor_invertido}")

"""
MULTIPLICAR CADA ELEMENTO POR 2
"""
def multiplicar_por_2(vet_dados):
    multiplicador = 2
    vetor_mult = [elemento * multiplicador for elemento in vet_dados]
    print(f"\n\tO valor do vetor multiplicado é: {vetor_mult}")

"""
QUANTAS VEZES O VALOR 74 APARECE EM UM VETOR
"""
def valor_aparece(vet_dados):
    ocorrencias = vet_dados.count(74)
    print(f"\n\tO valor 74 aparece {ocorrencias} vezes.")

"""
ORDENAR UM VETOR EM ORDEM CRESCENTE
"""
def ordernar_crescente(vet_dados):
    vetor_ordenado = sorted(vet_dados)
    print(f"\n\tVetor ordenado: {vetor_ordenado}")

"""
REMOVER ELEMENTOS DUPLICADOS DE UM VETOR
"""
def remover_duplicado(vet_dados):
    vetor_sem_duplicatas = list(dict.fromkeys(vet_dados))
    print(f"\n\tO valor sem duplicatas é: {vetor_sem_duplicatas}")

"""
SEPARAR OS ELEMENTOS PARES E IMPARES EM DUAS LISTAS
"""
def separar_par_e_impar(vet_dados):
    pares = [num for num in vet_dados if num % 2 == 0]
    impar = [num for num in vet_dados if num % 2 != 0]
    print(f"\n\tOs números pares do vetor são: {pares}")
    print(f"\n\tOs números ímpares do vetor são: {impar}")

"""
CALCULAR A MÉDIA E EXIBIR OS ELEMENTOS ACIMA DA MÉDIA
"""
def calcular_media(vet_dados):
    media = sum(vet_dados) / len(vet_dados)
    acima_media = [num for num in vet_dados if num > media]
    print(f"\n\tA média dos vetores é: {media}")
    print(f"\n\tOs vetores acima da média são: {acima_media}")



           
if __name__ == "__main__":

    #CRIAR E IMPRIMIR UMA LISTA:
    criar_imprimir_lista()
    criar_imprimir_lista_v2(vet_dados)
    
    #ITERANDO LISTA:
    iterando_lista(vet_dados)

    #SOMA DOS VETORES:
    soma_vetor(vet_dados)

    #MAIOR E MENOR VALOR EM UM VETOR:
    maior_e_menor(vet_dados)

    #INVERTER A ORDEM DO VETOR:
    inverter_vetor(vet_dados)

    #MULTIPLICAR O VETOR POR 2:
    multiplicar_por_2(vet_dados)

    #QUANTAS VEZES O VALOR 74 APARECE:
    valor_aparece(vet_dados)

    #ORDENAR O VETOR EM ORDEM CRESCENTE:
    ordernar_crescente(vet_dados)

    #REMOVER ELEMENTOS DUPLICADOS DO VETOR:
    remover_duplicado(vet_dados)

    #SEPARAR PAR E ÍMPAR:
    separar_par_e_impar(vet_dados)

    #CALCULAR A MÉDIA E EXIBIR ELEMENTOS ACIMA DA MÉDIA:
    calcular_media(vet_dados)


