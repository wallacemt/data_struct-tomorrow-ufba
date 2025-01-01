'''
-->Projeto: Sistema de Notas de Estudantes usando Vetor.
|> push(elemento) - Colocar um elemento no final do vetor
|> pop() - Remover o último elemento do vetor
|> insert(elemento, indice) - Colocar o elemento no índice passado
|> show() - Mostrar todos os elementos do vetor
'''

class Vetor:
    def __init__(self, max):
        self.vetor = [None] * max
        self.size = 0
        self.max = max
        
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.max
    
    def push(self,data):
        if(self.isFull()):
            print("A tabela esta cheia!")
            return
        self.vetor[self.size] = data
        
        self.size += 1;
    
    def pop(self):
        if(self.isEmpty()):
            print("Error: Vetor vazio")
            return None
        
        removed = self.vetor[self.size - 1]
        self.vetor[self.size - 1] = None
        self.size -= 1
        print("Elemento removido!")
        return removed 
    
    def insertAt(self, data, index):
        if(self.isFull()):
            print("A tabela esta cheia!")
            return
        for i in range(self.size - 1, index - 1, -1):
            self.vetor[i + 1] = self.vetor[i]
        self.vetor[index] = data
        self.size += 1
        
    def show(self):
        for i in range(self.size):
            print(self.vetor[i], end = "->")
        print()
        

def main():
    vetor = Vetor(10)
    while True:
        print(" 1 - Adicionar nota")
        print(" 2 - Remover nota")
        print(" 3 - Adicionar nota em uma posicao")
        print(" 4 - Mostrar notas")
        print(" 0 - Sair")
        op = int(input("Escolha uma opção: "))
        print("")
        if op == 1:
            nota = float(input("Digite a nota: "))
            vetor.push(nota)
        elif op == 2:
            vetor.pop()
        elif op == 3:
            pos = int(input("Digite a posicao: "))
            nota = float(input("Digite a nota: "))
            vetor.insertAt(nota, pos)
        elif op == 4:
            print("Notas:")
            vetor.show()
            print("")
        elif op == 0:
            break
        else:
            print("Opção invalida")
main()
