class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def pre_ordem(raiz):
    if raiz:
        print(raiz.valor, end=' ')
        pre_ordem(raiz.esquerda)
        pre_ordem(raiz.direita)

raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)
raiz.esquerda.esquerda = No(2)
raiz.esquerda.direita = No(7)


pre_ordem(raiz)  