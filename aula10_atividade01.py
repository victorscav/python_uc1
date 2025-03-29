""" 
Aula 10 - Atividade 01
"""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_4_4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

"""
MOSTRAR ELEMENTO
"""

def mostrar_elemento():
    print("Elemento (0,0)", matriz[0][0])
    print("Elemento (2,1)", matriz[2][1])

"""
ARRUMAR A MATRIZ
"""

def arrumar_matriz():
    for linha in matriz:
        print(f"|", end=" ")
        for elemento in linha:
            print(elemento, end= ' | ')
        print()

"""
MONTAR A MATRIZ
"""

def montar_matriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor = int(input(f"Digite o valor para [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    for linha in matriz:
        print(linha)

"""
SOMATORIO (2 MANEIRAS)
"""

def somatorio_v1():
    soma = 0
    for i in range(4):
        for j in range(4):
            soma=soma + matriz_4_4[i][j]
    print(f"Soma dos elementos é: {soma}")

def somatorio_v2():
    soma = 0
    for i in range(4):
        soma=soma + sum(matriz_4_4[i])
    print(f"Soma dos elementos é: {soma}")

def somatorio_v3():
    soma=0
    for linha in matriz_4_4:
        soma=soma+sum(linha)
    print(f"A soma dos elementos é {soma}")

"""
MAIOR VALOR (2 MANEIRAS)
"""

def maior_valor():
    for i in range(4):
        maior=matriz_4_4[i][0]
        for j in range(4):
            if matriz_4_4[i][j] > maior:
                maior = matriz_4_4[i][j]
        print(f"O maior valor da linha {i} é: {maior}")

def maior_valorv2():
    for i in range(4):
        maior=max(matriz_4_4[i])
        print(f"O maior valor da linha {i} é: {maior}")

"""
QUANTOS NUMEROS PARES E IMPARES TEM E QUAIS SÃO ELES
"""

def pares_e_impares():
    vet_pares=[]
    vet_impares=[]
    pares = 0
    impares = 0
    for i in range(4):
        for j in range(4):
            if matriz_4_4[i][j] % 2 == 0:
                pares = pares + 1
                vet_pares.append(matriz_4_4[i][j])
            elif matriz_4_4[i][j] % 2 == 1:
                impares = impares + 1
                vet_impares.append(matriz_4_4[i][j])
    print(f"A quantidade de numeros pares é: {pares}")
    print(f"A quantidade de números impares é: {impares}")
    print(f"Os números pares são: {vet_pares}")
    print(f"Os números ímpares são: {vet_impares}")

""" 
MULTIPLICAÇÃO DE LINHAS POR UM NUMERO
"""

def multi_linhas():
    num = int(input("Digite o número para a multiplicação: "))
    linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))
    for j in range (4):
        matriz_4_4[linha_escolhida][j] *= num
    for linha in matriz_4_4:
        print(linha)


if __name__ == "__main__":

    mostrar_elemento()
    arrumar_matriz()
    somatorio_v1()
    somatorio_v2()
    somatorio_v3()
    montar_matriz()
    maior_valor()
    maior_valorv2()
    pares_e_impares()
    multi_linhas()