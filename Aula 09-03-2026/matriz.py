m = []

for i in range(3):
    vetor = []
    for j in range(3):
        valor = int(input(f'Digite um valor para o vetor {i + 1}, posição {j + 1}: '))
        vetor.append(valor)
    m.append(vetor)

for linha in m:
    print(linha)

print(m[1][0])