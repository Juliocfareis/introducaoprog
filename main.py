1. # Cria um vetor vazio com capacidade para 20 números
numeros = [0] * 20

for i in range(20):
    numeros[i] = int(input("Digite um número: "))

for i in range(19, -1, -1):
    print(numeros[i])

2. # Cria um vetor vazio com capacidade para 10 números
vetor = [0] * 10

for i in range(10):
    vetor[i] = int(input("Digite um número: "))

repetidos = []
for i in range(10):
    if vetor.count(vetor[i]) > 1 and vetor[i] not in repetidos:
        repetidos.append(vetor[i])
        print("O número", vetor[i], "se repete nas posições:", end=" ")
        for j in range(10):
            if vetor[j] == vetor[i]:
                print(j, end=" ")
        print()

if not repetidos:
    print("Não há números repetidos no vetor.")
