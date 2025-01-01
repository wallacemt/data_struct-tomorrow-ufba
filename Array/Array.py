
class Vetor:
    def __init__(self, max):
        self.vetor = [None] * max
        self.size = 0
        self.max = max

    def push(self, data):
        if self.size == self.max:
            return
        
        self.vetor[self.size] = data

        self.size += 1

    def delete(self, index):
        if self.size == 0:
            return
        
        if index >= self.max:
            return
        
        if index == self.size - 1:
            self.size -= 1
            return

        for i in range(index + 1, self.size):
            self.vetor[i - 1] = self.vetor[i]
        self.size -= 1

    def __str__(self):
        text = "["
        for i in range(self.size):
            text += (f"{self.vetor[i]}, ")
        print("]")
        
vetor = Vetor(10)

vetor.push(1)
vetor.push(2)
vetor.push(3)

print(vetor.vetor)


vetor.delete(1)

print(vetor.vetor)