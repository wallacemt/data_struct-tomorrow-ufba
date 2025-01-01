class No:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
    
class Queue:
    def __init__(self):
        self.begin = None
        self.end = None
        
    def enqueue(self,data):
        newNo = No(data)
        if(self.end is None):
            self.begin = newNo
            self.end = newNo
        else:   
            self.end.next = newNo      
            self.end = newNo
            
        
    def dequeue(self):
        if(self.begin is None):
            print("A fila está vazia!")
            return None
        data = self.begin.data
        self.begin = self.begin.next
        if(self.begin is None):
            self.end = None

        return data
            
    def displayBegin(self):
        if(self.begin is None):
            print("A fila esta vazia")
            return None
        return(self.begin.data)
    
    def displayEnd(self):
        if(self.end is None):
            print("A fila está vazia")
            return None
        return str(self.end.data)
    
        
    def displayQueue(self):
        if self.begin is None:
            print("A fila está vazia")
            return

        aux = self.begin
        while(aux is not None):
            print(str(aux.data), end=" -> ")
            aux = aux.next
        print("None")        
            
            
# CRIA FILA
fila = Queue()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)

# VER O INICIO DA FILA
print(fila.displayBegin())

# VER O FINAL DA FILA
print(fila.displayEnd())

# VER A FILA ENCADEADA
fila.displayQueue()
        
