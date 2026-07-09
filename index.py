#Projeto com todos os itens estudados aqui

def multiplica_valores(*args):
    return [num * 2 for num in args]

resultado = multiplica_valores(1,2,3,4,5,6)
print(resultado)