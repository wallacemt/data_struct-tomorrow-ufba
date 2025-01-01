class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
    
    def getDado(self):
        return self.dado

    def setDado(self, novoDado):
        self.dado = novoDado
    
    def getProximo(self):
        return self.proximo

    def setProximo(self, novoNo):
        self.proximo = novoNo

class ListaEncadeada:
    def __init__(self):
        self.head = None
    
    def push(self, dado):
        no = No(dado)

        if self.head is None:
            self.head = no
            return

        atual = self.head

        while(atual.getProximo() is not None):
            atual = atual.getProximo()
        
        atual.setProximo(no)
    
    def __str__(self):
        texto = ""

        actual = self.head

        while(actual is not None):
            texto += f"{actual.getDado()} -> "
            actual = actual.getProximo()
        
        texto += "None"
        return texto


lista = ListaEncadeada()

lista.push(1)
lista.push(2)
lista.push(3)

print(lista)