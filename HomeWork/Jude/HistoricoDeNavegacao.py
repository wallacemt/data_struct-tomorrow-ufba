class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
    def getDado(self):
        return self.dado
    def getProximo(self):
        return self.proximo


class Pilha:
    def __init__(self):
        self.top = None
        
    def insert(self, dado):
        no = No(dado)
        no.proximo = self.top
        self.top = no
    
    def pop(self):
        if(self.top == None):
            return print("historico vazio")
        else:
            aux = self.top.dado
            self.top = self.top.proximo
            return aux
    
    def getTop(self):
        if(self.top is not None):
            return self.top.dado
    
    def display(self):
        aux = self.top
        while aux is not None:
            print(f"{aux.getDado()} -> ")
            aux = aux.getProximo()

    


def historicoDeNavegação(entrada):
    hist = Pilha()
    texto = entrada.split()
    while True:
        if(texto[0] == "A"):
            dado = texto
            hist.insert(dado)
        elif(op == "V"):
            if(hist.getTop() is not None):
                print(hist.getTop())
            hist.pop()

        elif(op == "E"):
            break
        else:
            "opcao invalida!"
    


historicoDeNavegação("A google")