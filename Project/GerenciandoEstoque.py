class No:
    def __init__(self, nome, preco, categoria, quantidade):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.quantidade = quantidade
        self.esquerda = None
        self.direita = None
        
class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
    
    def _busca(self, nome):
        atual = self.raiz
        pai = None
        while(atual is not None and nome != atual.nome):
            pai = atual
            if(nome < atual.nome):
                atual = atual.esquerda
            else:
                atual = atual.direita
    
        return(atual, pai)
    
    def busca(self, nome):
        atual = self.raiz
        
        while(atual is not None and nome != atual.nome):
            if(nome < atual.nome):
                atual = atual.esquerda
            else:
                atual = atual.direita
        if(atual is None):
            print(f"Produto '{nome}' não encontrado na árvore!")
            return None
        else:
            print(f"Produto '{nome}' encontrado na árvore!")
            print(f"{'Nome':<20}{'Preço R$':<10}{'Categoria':<15}{'Quantidade':<10}")
            print("-" * 55)
            print(f"{atual.nome:<20}{f'R${atual.preco:<10.2f}'}{atual.categoria:<15}{atual.quantidade:<10}")
            return
        
    def inserir(self, nome, preco, categoria, quantidade):
            nome = nome.lower()
            novo = No(nome, preco, categoria, quantidade)
            atual, pai = self._busca(nome)
            
            if(atual is not None):
                print(f"Produto '{nome}' já cadastrado na árvore!")
                return
            
            if(pai is None):
                self.raiz = novo
            elif nome < pai.nome:
                pai.esquerda = novo
            else:
                pai.direita = novo
            
    def remover(self, nome):
            nome = nome.lower()
            no, pai = self._busca(nome)
            if(no is None):
                print(f"Produto '{nome}' nao encontrado na arvore!")
                return
            self._remover(no, pai)
            print(f"Produto '{nome}' removido com sucesso!")
        
    def _remover(self, no, pai):
            if(no.esquerda is None and no.direita is None):
                if(pai is None):
                    self.raiz = None
                elif(pai.esquerda == no):
                    pai.esquerda = None   
                else:
                    pai.direita = None
            elif(no.esquerda is None):
                if(pai is None):
                    self.raiz = no.direita
                elif(pai.esquerda == no):
                    self.raiz = no.direita
                else:
                    pai.direita = no.direita
            elif(no.direita is None):
                if(pai is None):
                    self.raiz = no.esquerda
                elif(pai.esquerda == no):
                    pai.esquerda = no.esquerda
                else:
                    pai.direita = no.esquerda
            else:
                sucessor = self._minimo(no.direita)
                no.nome = sucessor.nome
                no.preco = sucessor.preco
                no.categoria = sucessor.categoria
                no.quantidade = sucessor.quantidade
                self._remover(sucessor, no)
                
    def _minimo(self, no):
            atual = no
            while(atual.esquerda is not None):
                atual = atual.esquerda
            return atual
        
        
    def calcularTotal(self, no):
            if(no is None):
                return 0
            valor_atual = no.preco * no.quantidade
            return valor_atual + self.calcularTotal(no.esquerda) + self.calcularTotal(no.direita)
            
    def exibir(self):
        if self.raiz is None:
            print("\033[31mO estoque está vazio.\033[0m")
            return
        print(f"\033[32m{'Nome':<20}{'Preço R$':<10}{'Categoria':<15}{'Quantidade':<10} \033[0m")
        print("\033[31m-\033[0m" * 55)
        self._exibir(self.raiz)
        
    def _exibir(self, no):
        if no is not None:
            self._exibir(no.esquerda)
            print(f"\033[34m{no.nome:<20}{f'R${no.preco:<10.2f}'}{no.categoria:<15}{no.quantidade:<10}\033[0m")
            self._exibir(no.direita)
            
    def dropDatabase(self):
        self.raiz = None
        print("Arvore apagado com sucesso!")
        
        
estoque = ArvoreBinariaBusca()
estoque.inserir("RTX 3080", 1650, 'Hardware', 13)
estoque.inserir("Xbox-S", 2300, 'Periférico', 12)
estoque.inserir("monitor", 1200, 'Gamer', 21)
estoque.inserir("headset", 130, 'Periférico', 10)
estoque.inserir("Pc gamer", 6400, 'Periférico', 5)
estoque.inserir("Ps5", 2500, 'Gamer', 30)
estoque.exibir()
print(f"Valor total em estoque:{estoque.calcularTotal(estoque.raiz)}")

print("-" *20)
estoque.remover('Ps5')
estoque.exibir()

#exemplo exalirdraw >> https://excalidraw.com/#json=SsIjsQ7RFks5XSQC5cWgZ,F4fkMINkU8R-J79wFgI5vQ