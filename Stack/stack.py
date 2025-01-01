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

    def isEmpty(self):
        return self.top is None
    def push(self, dado):
        no = No(dado)
        if(self.isEmpty()):
            self.top = no
        else:
            no.proximo = self.top
            self.top = no

    def pop(self):
        if(self.isEmpty()):
            return print("pilha vazia")
        else:    
            aux = self.top.dado
            self.top = self.top.proximo
            return aux
    
    def peek(self):
        if(self.isEmpty()):
            return print("pilha vazia")
        else:
            return print(f'Elemento no topo: {self.top.dado}')
        
    def clear(self):
        self.top = None
        print("pilha esvaziada")
        
    def display(self):
        aux = self.top
        while aux is not None:
            print(f"{aux.getDado()} -> ")
            aux = aux.getProximo()
            
def main():
    pilha = Pilha()
    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    pilha.push(4)
    pilha.push(5)
    pilha.display()
    
main()