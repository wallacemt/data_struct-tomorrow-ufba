class No: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.prox_nome = None
        self.prox_idade = None
    
class Multilista:
    def __init__(self):
        self.inicio_nome = None
        self.inicio_idade = None

    def inserir(self, nome, idade):
        if not self._existe(nome, idade):
            no = No(nome, idade)
            self._inserir_ordenado_nome(no)
            self._inserir_ordenado_idade(no)
    
    def _existe(self, nome, idade):
        atual = self.inicio_nome
        while atual:
            if atual.nome == nome and atual.idade == idade:
                return True
            atual = atual.prox_nome
        return False
    
    def _inserir_ordenado_nome(self, no):
        if self.inicio_nome is None or no.nome < self.inicio_nome.nome:
            no.prox_nome = self.inicio_nome
            self.inicio_nome = no
        else:
            atual = self.inicio_nome
            while atual.prox_nome and atual.prox_nome.nome < no.nome:
                atual = atual.prox_nome
            no.prox_nome = atual.prox_nome
            atual.prox_nome = no
            
    def _inserir_ordenado_idade(self, no):
        if self.inicio_idade is None or no.idade < self.inicio_idade.idade:
            no.prox_idade = self.inicio_idade
            self.inicio_idade = no
        else:
            atual = self.inicio_idade
            while atual.prox_idade and atual.prox_idade.idade < no.idade:
                atual = atual.prox_idade
            no.prox_idade = atual.prox_idade
            atual.prox_idade = no
            
    def exibir(self):
        atual_nome = self.inicio_nome
        atual_idade = self.inicio_idade
        while atual_nome and atual_idade:
            print(f'{atual_nome.nome} {atual_nome.idade} | {atual_idade.nome} {atual_idade.idade}')
            atual_nome = atual_nome.prox_nome
            atual_idade = atual_idade.prox_idade
            
def main():
    N = int(input())
    lista = Multilista()
    
    for i in range(N):
        entrada = input().split()
        nome = entrada[0]
        idade = int(entrada[1])
        lista.inserir(nome, idade)
    lista.exibir()

main()

