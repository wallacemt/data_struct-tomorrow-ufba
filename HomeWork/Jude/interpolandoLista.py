class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None;
    
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
        self.size = 0
    
    def append(self, dado):
        no = No(dado)

        if(self.head == None):
            self.head = no
            self.size += 1
        else:
            aux = self.head
            while(aux.getProximo() != None):
                aux = aux.getProximo()
            
            aux.setProximo(no)
            self.size += 1

    def display(self):
        aux = self.head
        while(aux != None):
            print("{} -> ".format(aux.getDado()), end="")
            aux = aux.getProximo()
            
        print("None")
        
    def newList(self):
        self.head = None
        return self
    
    def freeList(self):
        self.head = None
        return
    
    def insert(self, pos, dado):
        no = No(dado)
        if pos <= 0:  
            no.setProximo(self.head)
            self.head = no
        elif pos >= self.size:  
            self.append(dado)
        else:  
            aux = self.head
            for i in range(pos - 1):
                aux = aux.getProximo()
            no.setProximo(aux.getProximo())
            aux.setProximo(no)
        self.size += 1 




def interpolaLista(A, B):
    pos = 0  
    atual = A.head 
    
    while atual is not None:
        dado = atual.getDado()  
        pos += dado  
        
        
        B.insert(pos, dado)
        atual = atual.getProximo()  
    aux = B.head
    while aux is not None:
        print(aux.getDado(), end=" ")
        aux = aux.getProximo()
    print("")



A = ListaEncadeada()
B = ListaEncadeada()

A.append(10)
A.append(1)

B.append(0)
B.append(1)
B.append(2)
B.append(3)
B.append(4)
B.append(5)
B.append(6)
B.append(7)
B.append(8)
B.append(9)

interpolaLista(A, B)

