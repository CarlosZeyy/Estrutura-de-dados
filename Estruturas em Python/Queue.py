filaCliente = []

filaCliente.append('Cliente 1')
print(filaCliente)

filaCliente.append('Cliente 2')
print(filaCliente)

filaCliente.pop(0)
print(filaCliente)

from collections import deque

# Criando a fila
filaCliente = deque()

# Adicionando (enqueue)
filaCliente.append('Cliente 1')
filaCliente.append('Cliente 2')
print(filaCliente)

# Removendo o primeiro (dequeue) - note que o comando é popleft()
filaCliente.popleft() 
print(filaCliente)