from collections import deque

def simulacao_fila():
    fila = deque()
    fila.append(1)
    fila.append(2)
    return fila.popleft()


saida = simulacao_fila()
print(saida) 