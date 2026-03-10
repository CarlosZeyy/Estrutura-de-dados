m = []
v1 = []
v2 = []
v3 = []

for i in range(3):
    valor = int(input("Digite um valor para o vetor 1: "))
    v1.append(valor)
m.append(v1)

for i in range(3):
    valor2 = int(input("Digite um valor para o vetor 2: "))
    v2.append(valor2)
m.append(v2)    

for i in range(3):
    valor3 = int(input("Digite um valor para o vetor 3: "))
    v3.append(valor3)
m.append(v3)

for linha in m:
    print(linha)

print(m[1][0])