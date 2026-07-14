#Lambda

def calcular_imposto(preco):
    return preco * 0.3

print(calcular_imposto(1000))

imposto_preco = lambda x: x * 0.3
print(imposto_preco(1000))

precos = [100, 200, 300, 400]
impostos = list(map(lambda x: x * 0.3, precos))
print(impostos)