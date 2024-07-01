precos = [4, 10, 15]
def aumentarPreco(x):
    return x * 1.1

novosPrecos = map(aumentarPreco, precos)
print(list(novosPrecos))

valores = ((10, 20), [30, 40])
def somar(x):
    return x[0] + x[1]

print(f"Somas:{list(map(somar, valores))}")


def somarValores(valores):
    soma = 0
    for v in valores:
        soma += v

    return soma
v1 = [1, 2, 3]
v2 = [4, 5, 6, 7]
print(f"Soma dos valores {list(map(somarValores, [v1, v2]))}")


def multiplicarValores(x, y):
    return x * y


numeros = (2, 3, 4), (5, 6, 7)
print(f"Multiplicações: {list(map(multiplicarValores, numeros[0], numeros[1]))}")