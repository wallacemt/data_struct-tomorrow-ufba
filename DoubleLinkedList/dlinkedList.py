class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None
    
    def getDado(self):
        return self.dado

    def setDado(self, novoDado):
        self.dado = novoDado
    
    def getProximo(self):
        return self.proximo

    def setProximo(self, novoNo):
        self.proximo = novoNo
    
    def getAnterior(self):
        return self.anterior

    def setAnterior(self, novoNo):
        self.anterior = novoNo

class ListaDuplaEncadeada:
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
        no.setAnterior(atual)
    
    def adicionaInicio(self, dado):
        novoNo = No(dado)

        novoNo.setProximo(self.head)
        
        self.head = novoNo
        
    
    def __str__(self):
        texto = ""

        actual = self.head

        while(actual is not None):
            texto += f"{actual.getDado()} - "
            actual = actual.getProximo()
        
        texto += "None"
        return texto


lista = ListaDuplaEncadeada()

lista.push(1)
lista.push(2)
lista.push(3)

print(lista)