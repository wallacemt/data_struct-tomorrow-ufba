'''
-->Projeto:  Sistema de Atendimento de Clientes em um Caixa usando Fila.
|>push(elemento) - Colocar um elemento no fim da fila
|>pop() - Remover o elemento do início da fila
|>front() - Retorna o elemento no início da fila
|>show() - Mostrar a fila em ordem de chegada
'''

class No():
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        
class Fila():
    def __init__(self):
        self.inicio = None
        self.fim = None
        
    def enqueue(self, dado):
        no = No(dado)
        if(self.inicio is None):
            self.inicio = self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        
    def dequeue(self):
        if(self.inicio is None):
            return None
        dado = self.inicio.dado
        self.inicio = self.inicio.proximo
        if(self.inicio is None):
            self.fim = None
        return dado
        
    def get_front(self):
        if(self.inicio is None):
            return None
        return self.inicio.dado
    
    def displayQueue(self):
        aux = self.inicio
        while(aux is not None):
            print(aux.dado, end=" -> ")
            aux = aux.proximo
        print("None")
def main():
    fila = Fila()
    while True:
        print("1 - Adicionar cliente a fila (nome)")
        print("2 - Atender cliente")
        print("3 - Mostrar fila de clientes")
        print("4 - Mostrar cliente na frente da fila")
        print("0 - Sair do sistema")
        op = input("Opção: ")
        if(op == "1"):
            nome = input("Digite o nome do cliente: ")
            fila.enqueue(nome)
        elif(op == "2"):
            if(fila.dequeue() is None):
                print("Nenhum cliente na fila")
            else:
                print("Atendendo...")
        elif(op == "3"):
            fila.displayQueue()
        elif(op == "4"):
            if(fila.get_front() is None):
                print("Nenhum cliente na fila")
            else:
                print("Cliente na frente da fila: ", fila.get_front())
        elif(op == "0"):
            break
        else:
            print("Opção inválida. Tente novamente.")
    print("Sistema de atendimento encerrado. Até  logo!")
        
main()