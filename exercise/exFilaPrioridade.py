'''
-->Projeto:  Gerenciador de Processos do Sistema Operacional com Fila de Prioridade.
|>push(elemento) - Colocar um elemento na fila de prioridade (Posição depende da sua prioridade)
|>pop() - Remover o elemento do início da fila
|>front() - Retorna o elemento no início da fila
|>show() - Mostrar a fila em ordem de prioridade
'''

class No():
    def __init__(self, dado, prioridade):
        self.dado = dado
        self.prioridade = prioridade
        self.proximo = None
        
class Fila():
    def __init__(self):
        self.inicio = None
        self.fim = None
        
    def enqueue(self, dado, prioridade):
        no = No(dado, prioridade)
        if(self.inicio is None):
            self.inicio = self.fim = no
        else:
            if(no.prioridade > self.inicio.prioridade):
                no.proximo = self.inicio
                self.inicio = no
            else:
                aux = self.inicio
                while(aux.proximo is not None and aux.proximo.prioridade <= no.prioridade):
                    aux = aux.proximo
                no.proximo = aux.proximo
                aux.proximo = no
                if(aux.proximo is None):
                    self.fim = no
    def dequeue(self):
        if(self.inicio is None):
            return None
        dado = self.inicio.dado
        self.inicio = self.inicio.proximo
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
        print("\nGerenciador de Processos do Sistema Operacional")
        print("1. Adicionar processo")
        print("2. Remover processo")
        print("3. Mostrar processo no início")
        print("4. Mostrar todos os processos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dado = input("Informe o nome do processo: ")
            prioridade = int(input("Informe a prioridade do processo(1-10): "))
            fila.enqueue(dado, prioridade)
        elif opcao == "2":
            removido = fila.dequeue()
            if removido:
                print(f"Processo {removido} removido.")
            else:
                print("Fila vazia.")
        elif opcao == "3":
            frente = fila.get_front()
            if frente:
                print(f"Processo no início: {frente}")
            else:
                print("Fila vazia.")
        elif opcao == "4":
            print("Processos na fila:")
            fila.displayQueue()
        elif opcao == "5":
            print("Encerrando o gerenciador.")
            break
        else:
            print("Opção inválida. Tente novamente.")   
        
main()