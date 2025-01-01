'''
-->Projeto: Histórico de Ações de um Editor de Texto com Lista Simplesmente Encadeada.
|> push(elemento) - Colocar um nó com o dado ao final da lista
|> pop() - Remover o nó passado (Dica: Faça uma função auxiliar __remover(nó, pai))
|> insert(dado, posicao) - Colocar o nó com o dado no posição indicada passado
|> show() - Mostrar todos os elementos da lista
'''

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        
class ListaEncadeada:
    def __init__(self):
        self.head = None
        
    def push(self, dado):
        no = No(dado)
        
        if(self.head is None):
            self.head = no
        else:
            aux = self.head
            while(aux.proximo is not None):
                aux = aux.proximo
            aux.proximo = no
        
        return 
    
    def remover(self, dado):
        aux = self.head
        pai = None
        if(aux is not None and aux.dado == dado):
            self.head = aux.proximo
            aux = None
            return

        while(aux is not None and aux.dado != dado):
            pai = aux
            aux = aux.proximo
        
        if(aux is not None):
            pai.proximo = aux.proximo
            aux = None
            print(f'Ação ({dado}) removida com sucesso!')
        else:
            print(f'Ação ({dado}) não encontrado no historico.')

    def insert(self, dado, posicao):
        no = No(dado)
        if(posicao == 0):
            no.proximo = self.head
            self.head = no
        else:
            aux = self.head
            for i in range(posicao - 1):
                aux = aux.proximo
            no.proximo = aux.proximo
            aux.proximo = no
        return
    
    def show(self):
        aux = self.head
        while(aux is not None):
            print(aux.dado, end=" -> ")
            aux = aux.proximo
        print()
    
    
def main():
    historico = ListaEncadeada()
    while True:
        print(" 1 - Adicionar ação ao historico ex(inserir texto, excluir texto, etc.):")
        print(" 2 - Remover ação do historico")
        print(" 3 - Adicionar ação em uma posicao especifica")
        print(" 4 - Mostrar historico de acões")
        print(" 0 - Sair")
        op = int(input("Escolha uma opcao: "))
        print("")
        if op == 1:
            dado = input("Digite a ação: ")
            historico.push(dado)
            print("")
        elif op == 2:
            dado = input("Digite a ação: ")
            historico.remover(dado)
            print("")
        elif op == 3:
            dado = input("Digite a ação: ")
            posicao = int(input("Digite a posição: "))
            historico.insert(dado, posicao)
            print("")
        elif op == 4:
            print("Historico:")
            historico.show()
            print("")
        elif op == 0:
            break
        else:
            print("Opção invalida")
            print("")
            
main();
