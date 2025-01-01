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
    
    def remover(self):
        if self.is_empty():
            return None
        aux = self.top.dado
        self.top = self.top.proximo
        return aux
    
    def getTop(self):
        if self.top is not None:
            return self.top.dado
    def is_empty(self):
        return self.top is None
        

def verificar_balanceamento(sequencia):
    pilha = Pilha()
    pares = {')': '(', '}': '{', ']': '[', '>': '<'}
    
    for simbolo in sequencia:
        if simbolo in "({[<":
            pilha.insert(simbolo)
        elif(simbolo in ")}]>"):
            topo = pilha.remover()
            if topo != pares[simbolo]:
                return "N"
    return "Y" if pilha.is_empty() else "N"
def main():
    N = int(input())
    
    for i in range(N):
        entrada = input().split() 
        sequencia = ''.join(entrada)  
        resultado = verificar_balanceamento(sequencia)
        print(resultado)
        
main()