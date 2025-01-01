class No:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.direita = None
        self.esquerda = None
    def __str__(self):
        return f"{self.key} | {self.data}"

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
    
    def busca(self, key):
        atual = self.raiz
        parent = None
        while(atual is not None and key != atual.key):
            parent = atual
            if(key < atual.key):
                atual = atual.esquerda
            else:
                atual = atual.direita
        
        return(atual, parent)
    
    def inserir(self, key, data):
        no, pai = self.busca(key)
        if(no is not None):
            no.data = data
            return

        if pai is None:
            self.raiz = No(key, data)
        elif key < pai.key:
            pai.esquerda = No(key, data)
        else:
            pai.direita = No(key, data)

    def remover(self, key):
        no, pai = self.busca(key)
        if no is not None:
            self._remover(no, pai)

    def _remover(self, no, pai):
        if no.esquerda is not None and no.direita is not None:
            self._promoverSucessor(no)
            return

        if no.esquerda is not None:
            if pai is None:
                self.raiz = no.esquerda
            elif no is pai.esquerda:
                pai.esquerda = no.esquerda
            elif no is pai.direita:
                pai.direita = no.esquerda
        elif no.direita is not None:
            if pai is None:
                self.raiz = no.direita
            elif no is pai.esquerda:
                pai.esquerda = no.direita
            elif no is pai.direita:
                pai.direita = no.direita
        else:
            if pai is None:
                self.raiz = None
            elif no is pai.esquerda:
                pai.esquerda = None
            else:
                pai.direita = None

    def _promoverSucessor(self, no):
        pai = no
        sucessor = no.direita

        while sucessor.esquerda is not None:
            sucessor = sucessor.esquerda

        no.key = sucessor.key
        no.data = sucessor.data
        self._remover(sucessor, pai)

arvore = ArvoreBinariaBusca()
arvore.inserir(50, 10)
arvore.inserir(60, 15)

no, pai = arvore.busca(60)

print(no, pai)
