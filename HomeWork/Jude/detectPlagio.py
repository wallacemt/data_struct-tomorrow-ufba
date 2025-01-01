class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
    
    def getDado(self):
        return self.dado

    def setDado(self, dado):
        self.dado = dado

    def getProximo(self):
        return self.proximo

    def setProximo(self, proximo):
        self.proximo = proximo


class ListaEncadeada:
    def __init__(self):
        self.head = None
        
    def append(self, dado):
        no = No(dado)

        if self.head is None:
            self.head = no
        else:
            aux = self.head
            while aux.getProximo() is not None:
                aux = aux.getProximo()
            aux.setProximo(no)
    
    def display(self):
        aux = self.head
        while aux is not None:
            print(aux.getDado(), end=" ")
            aux = aux.getProximo()
        print()
    
    def getHead(self):
        return self.head
    

def detectarPlagio(seq1, seq2):
    inicio = seq2.getHead()
    pos_inicial = 0

    while inicio is not None:
        aux1 = seq1.getHead()
        aux2 = inicio
        pos = pos_inicial

        while aux1 is not None and aux2 is not None and aux1.getDado() == aux2.getDado():
            aux1 = aux1.getProximo()
            aux2 = aux2.getProximo()
            pos += 1
        
        if aux1 is None:
            print(f"Plagio encontrado na posição {pos_inicial}!")
            return
        
        inicio = inicio.getProximo()
        pos_inicial += 1
    
    print("Nenhum plagio detectado!")


pass1 = ListaEncadeada()
pass2 = ListaEncadeada()

t1 = str(input())
t2 = str(input())

x1 = t1.strip()
x2 = t2.strip()

for l in x1:
   pass1.append(l)
    
for l in x2:
    print(l)
    pass2.append(l)

detectarPlagio(pass1, pass2)
