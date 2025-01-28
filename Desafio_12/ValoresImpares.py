vetor= []

for i in range(1,11):
    vetor.append(int(input("Digite um valor: ")))


for i in vetor:
    if i % 2 != 0:
        print(f"Valores Impares: {i} - na posição {vetor.index(i)} " )



