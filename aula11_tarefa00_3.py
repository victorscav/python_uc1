frase = "o rato roeu a roupa do rei de roma"
palavras = frase.split()
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)