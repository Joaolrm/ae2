from Livro import Livro

class PilhaDeLivros:

    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def add(self, livro):
        if self.topo != None:
            livro.proximo = self.topo    
        self.topo = livro
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print("------Pilha de livros--------------------------")
        if self.topo == None:
            print( "Pilha Vazia" )
        else:
            print( self.tamanho,  " elementos na Pilha" )
            aux = self.topo
            while aux:
                print(aux)
                aux = aux.proximo
                
    
    def remover(self):
        if self.topo != None:
            self.topo = self.topo.proximo
            self.tamanho -= 1
        self.imprimir()
