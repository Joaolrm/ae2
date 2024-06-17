from No import No

class Fila:

    def __init__(self) -> None:
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, valor):
        nodo = No(self, valor)
        if self.inicio == None:
            self.inicio = nodo
            
        else:
            self.fim.proximo = nodo
        self.fim = nodo
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print("------Lista Encadeada--------------------------")
        if self.inicio == None:
            print( "Lista Vazia" )
        else:
            print( self.tamanho,  " elementos na Lista" )
            aux = self.inicio
            while aux:
                texto += aux.dado + " - "
                aux = aux.proximo
            print(texto)
    
    def remover(self):
        if self.inicio:
            if self.inicio.prox == None:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.inicio.proximo

