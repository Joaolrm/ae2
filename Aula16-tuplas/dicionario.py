carro = {
    "modelo" : "Renegade"
    ,"ano" : 2021
}

print(carro)
print(carro["modelo"])
carro["cor"] = "prata"
print(carro)
del carro["cor"]
print(carro)

carro2 = {
    "modelo" : "Doblo"
    ,"ano" : 2006
    ,"cor" : "prata"
}

carro3 = {
    "modelo" : "Uno"
    ,"ano" : 2004
    ,"cor" : "prata"
}

frota = carro, carro2

print(frota)

def getSizeArray(a):
    return len(a)

x = map(getSizeArray, {"maçã", "Banana", "Laranja"})
print(list(x))