class No:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.proximo = None
    
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def adiciona(self, nome, idade):
        no = No(nome, idade)
        if(self.fim is None):
            self.inicio = no
            self.fim = no
        else: 
            self.fim.proximo = no
            self.fim = no
        
    def atender(self, limite):
        atendidos = []
        for i in range(limite):
            if(self.inicio is not None):
                atendido = self.inicio  
                atendidos.append(atendido.nome)  
                self.inicio = self.inicio.proximo  
                if(self.inicio is None):  
                    self.fim = None
        return atendidos
    
    def reorganizar(self):
        if(self.inicio is None or self.inicio.proximo is None):
            return
        
        pessoas = []
        atual = self.inicio
        while atual is not None:
            pessoas.append((atual.nome, atual.idade))
            atual = atual.proximo
        
        pessoas.sort(key=lambda x: x[1], reverse=True)
        
        self.inicio = None
        self.fim = None
        for nome, idade in pessoas:
            self.adiciona(nome, idade)
    
def armazenDoPierre():
    try:
        D, X = map(int, input().split())
        fila = Fila()
        
        for i in range(D):
            N = int(input())
            for j in range(N):
                nome, idade = input().split()
                idade = int(idade)
                fila.adiciona(nome, idade)
            
            fila.reorganizar()
            
            atendidos = fila.atender(X)
            
            for atendido in atendidos:
                print(atendido)
    
    except Exception as e:
        print(e)
        
armazenDoPierre()

