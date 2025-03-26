from collections import deque

def reverter_fila(entrada):
    fila = deque(entrada)
    pilha = []
    while fila:
        pilha.append(fila.popleft())
    while pilha:
        fila.append(pilha.pop())
    return list(fila)

entrada = [1, 2, 3]
saida = reverter_fila(entrada)
print(saida)  