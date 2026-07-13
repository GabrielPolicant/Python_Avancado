#Projeto com todos os itens estudados aqui

def multiplica_valores(*args):
    return [num * 2 for num in args]

def conta_palavras(frase):
    return {palavra: frase.count(palavra) for palavra in frase.split()}

resultado = multiplica_valores(1,2,3,4,5,6)
frase = 'Gabriel é um ótimo professor e Gabriel é muito paciente'
print(conta_palavras(frase))
print(resultado)