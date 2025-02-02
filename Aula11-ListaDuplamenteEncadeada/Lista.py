from No import No
class Lista:
	def __init__(self):
		self.inicio = None
		self.fim = None

	def add(self, valor):
		nodo = No(valor)
		if self.inicio == None:
			self.inicio = nodo
			self.fim = nodo
		else:
			if nodo.dado < self.inicio.dado:
				nodo.proximo = self.inicio
				self.inicio.anterior = nodo
				self.inicio = nodo
			else:
				ant = self.inicio
				aux = self.inicio.proximo
				while aux:
					if nodo.dado < aux.dado:
						nodo.proximo = ant.proximo # nodo.proximo = aux
						ant.proximo = nodo
						aux.anterior = nodo
						nodo.anterior = ant
						break
					else:
						ant = aux
						aux = aux.proximo
				if aux == None and nodo.dado >= ant.dado:
					ant.proximo = nodo
		self.tamanho += 1
		self.imprimir()

	def imprimirReverso(self):
		print("------Lista Encadeada--------------------------")
		if self.inicio == None:
			print( "Lista Vazia" )
		else:
			print( self.tamanho,  " elementos na Lista" )
			aux = self.fim
			while aux:
				print( aux.dado )
				aux = aux.anterior

	def imprimir(self):
		print("------Lista Encadeada--------------------------")
		if self.inicio == None:
			print( "Lista Vazia" )
		else:
			print( self.tamanho,  " elementos na Lista" )
			aux = self.inicio
			while aux:
				print( aux.dado )
				aux = aux.proximo

	def remover(self, valor):
		tamInicial = self.tamanho
		if self.inicio != None:

			#Lista contendo só um elemente e este é igual ao valor
			if self.inicio.proximo == None and self.inicio.dado == valor:
				self.inicio = None
				self.fim = None
				self.tamanho = 0

			#Lista contendo vários elementos e o valor é igual ao primeiro
			elif self.inicio.dado == valor:
				self.inicio.proximo.anterior = None
				self.inicio = self.inicio.proximo
				self.tamanho -= 1

			# Lista com vários elementos e o valor não está no primeiro
			else:
				ant = self.inicio
				aux = self.inicio.proximo
				while aux:
					if aux.dado == valor:
						ant.proximo = aux.proximo
						self.tamanho -= 1
						break
					else:
						ant = aux
						aux = aux.proximo
		if tamInicial == self.tamanho:
			print( "Valor não encontrado")
		self.imprimir()

				