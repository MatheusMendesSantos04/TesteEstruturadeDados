def inverter_string(s):
    pilha = []
    for char in s:
        pilha.append(char)
    inverso = []
    while pilha:
        inverso.append(pilha.pop())
    return ''.join(inverso)

entrada = "Hello"
saida = inverter_string(entrada)
print(saida) 