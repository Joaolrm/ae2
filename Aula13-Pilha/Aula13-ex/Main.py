from Livro import Livro
from PilhaDeLivros import PilhaDeLivros

p1 = PilhaDeLivros()
l1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Roling", 300)
l2 = Livro("Harry Potter e a Cámara Secreta", "J. K. Roling", 350)
l3 = Livro("Harry Potter e o Prisioneiro de Azkaban", "J. K. Roling", 350)

p1.add(l1)
p1.add(l2)
p1.add(l3)
p1.remover()
p1.remover()
p1.remover()
