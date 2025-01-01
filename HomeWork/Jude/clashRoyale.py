class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def enqueue(self, dado):
        novo_no = No(dado)
        if self.is_empty():
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def dequeue(self):
        if self.is_empty():
            return None
        dado = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return dado
    
    def get_front(self):
        if self.is_empty():
            return None
        return self.inicio.dado
    
    def is_empty(self):
        return self.inicio is None

def clash_royale():
    N = int(input())
    fila_monstros = Fila()
    entrada = input().strip()
    numero = ""
    
    for char in entrada:
        if char != " ":
            numero += char
        else:
            fila_monstros.enqueue(int(numero))
            numero = ""
    if numero:
        fila_monstros.enqueue(int(numero))
    
    L = int(input())
    fila_adversarios = Fila()
    
    entrada = input().strip()
    numero = ""
    for char in entrada:
        if char != " ":
            numero += char
        else:
            fila_adversarios.enqueue(int(numero))
            numero = ""
    if numero:
        fila_adversarios.enqueue(int(numero))
    
    mortos = 0

    while not fila_adversarios.is_empty() and not fila_monstros.is_empty():
        poder_adversario = fila_adversarios.dequeue()
        poder_monstro = fila_monstros.get_front()
        
        if(poder_monstro is not None):   
            if poder_monstro >= poder_adversario:
                fila_monstros.enqueue(fila_monstros.dequeue())
            else:
                fila_monstros.dequeue()
                mortos += 1
        else:
            break
    
    print(mortos)

clash_royale()

