class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def obter_filhos(raiz, valor):
    if not raiz:
        return []
    fila = [raiz]
    while fila:
        no = fila.pop(0)
        if no.valor == valor:
            filhos = []
            if no.esquerda:
                filhos.append(no.esquerda.valor)
            if no.direita:
                filhos.append(no.direita.valor)
            return filhos
        if no.esquerda:
            fila.append(no.esquerda)
        if no.direita:
            fila.append(no.direita)
    return []

raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)


saida = obter_filhos(raiz, 10)
print(saida)  