#Args

def calcular_preco(valor):
    ir = valor * 0.23
    iss = valor * 0.05
    csll = valor * 0.0375
    pis = valor * 0.03
    return ir + iss + csll + pis

print('Função normal: ', calcular_preco(1000))

def calcular_preco(valor, *args):
    total_imposto = 0
    for imposto in args:
        total_imposto += valor * imposto
    return total_imposto

print('Função com *args: ', calcular_preco(1000, 0.23, 0.05, 0.0375, 0.05))

#Kwargs

def calcular_preco(valor, **kwargs):
    total_imposto = 0
    for imposto in kwargs.values():
        total_imposto += valor * imposto
    return total_imposto

print('Função com **kwargs: ', calcular_preco(1000, ir=0.23, iss=0.05, csll=0.0375, pis=0.05))