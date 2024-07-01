carros = "Uno", "Doblo", "Toro", "Jeep", "Hilux"
print(carros)
print(carros[1:4])
print(carros[1:-2])
print(carros[2:])


print(sorted(carros))
carrosOrdenados = sorted(carros)
carrosOrdenados[0] = "Fusca"
print(carrosOrdenados)

def calcular(x, y):
    return x+y, x-y, x*y, x/y

resultado = calcular(10, 11)
print(resultado)
print(resultado[1])

pessoa = {
    "nome": "Maria"
    ,"Idade": 25
}

print(pessoa)