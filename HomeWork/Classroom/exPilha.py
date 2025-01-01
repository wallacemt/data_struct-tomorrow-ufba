'''
-->Projeto: Verificador de Parênteses em Expressões Matemáticas com pilha.
|>push(elemento) - Colocar um elemento no topo da pilha
|>pop() - Remover o elemento do topo da pilha
|>peek() - Retorna o elemento no topo da pilha
|> clear() - Esvaziar a pilha
'''

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
    

def verificarParentees():
    pilha = Pilha()
    expressao = input("Digite a expressão: ")
    for i in expressao:
        if i == '(':
            pilha.push(i)
        elif i == ')':
            pilha.pop()
    if pilha.isEmpty():
        print("Expressão correta")
    else:
        print("Expressão incorreta")

def main():
    pilha = Pilha()
    while True:
        print(" 1 - Adicionar elemento na pilha")
        print(" 2 - Remover elemento da pilha")
        print(" 3 - Verificar elemento do topo da pilha")
        print(" 4 - Exibir Pilha")
        print(" 5 - Esvaziar pilha")
        print(" 6 - Verificar parenteses de expressão matemática") 
        print(" 0 - Sair")
        escolha = int(input(">>> "))
        if escolha == 1:
            dado = input("  Digite o elemento: ")
            pilha.push(dado)
            print("")
        elif escolha == 2:
            pilha.pop()
            print("")
        elif escolha == 3:
            pilha.peek()
            print("")
        elif escolha == 4:
            pilha.display()
            print("")
        elif escolha == 5:
            pilha.clear()
            print("")
        elif escolha == 6:
            verificarParentees()
            print("")
        elif escolha == 0:
            break
        else:
            print("Opção inválida")
            print("")

main()