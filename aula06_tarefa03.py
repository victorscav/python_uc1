matriz = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for elemento in linha:
        print(elemento,end="  ")
    print()

    for i in range(10):
        if i == 5:
            break
        if i % 2 ==0:
            continue
        print(i)