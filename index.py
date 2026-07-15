"""
1. Filtrar números pares

Crie uma lista com os números de 1 a 20 e, utilizando list comprehension, gere uma nova lista contendo apenas os números pares.
"""

numeros = list(range(21))
numeros_pares = [num for num in numeros if num % 2 == 0]
print('Ex01: ', numeros_pares)

"""
2. Criar um dicionário de números e quadrados

Dada a lista:

numeros = [1, 2, 3, 4, 5]

Utilize dict comprehension para criar um dicionário onde:

A chave seja o número.
O valor seja o quadrado do número.
"""

numeros = list(range(1,6))
numeros_quadrados = {num: num ** 2 for num in numeros}
print("Numeros quadrados: ", numeros_quadrados)

"""
3. Filtrar funcionários por salário

Dada a lista:

funcionarios = [
    ("Gabriel", 3500),
    ("Ana", 5200),
    ("Lucas", 2800),
    ("Maria", 4700)
]

Utilize list comprehension para criar uma lista contendo apenas os funcionários que ganham mais de R$ 4.000.
"""

funcionarios = [
    ("Gabriel", 3500),
    ("Ana", 5200),
    ("Lucas", 2800),
    ("Maria", 4700)
]

maiores_salarios = [pessoa for pessoa in funcionarios if pessoa[1] > 4000]
print("Salarios maiores do que R$4000: ", maiores_salarios)

"""
4. Contar a quantidade de cada palavra

Dada a lista:

palavras = ["python", "java", "python", "csharp", "java", "python"]

Crie um dicionário que contenha cada palavra e a quantidade de vezes que ela aparece.
"""

palavras = ["python", "java", "python", "csharp", "java", "python"]
contados_palavras = {palavra: palavras.count(palavra) for palavra in palavras}
print('Contador de palavras: ', contados_palavras)

"""
5. Filtrar e transformar dados

Dada a lista:

produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 100},
    {"nome": "Teclado", "preco": 250},
    {"nome": "Monitor", "preco": 1200}
]

Crie uma nova lista contendo apenas os produtos com preço maior que R$ 500, mas contendo apenas o nome dos produtos.
"""

produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 100},
    {"nome": "Teclado", "preco": 250},
    {"nome": "Monitor", "preco": 1200}
]

produtos_maiores = [produto['nome'] for produto in produtos if produto['preco'] > 500]

print('Produtos com precos maiores do que 500 reais: ', produtos_maiores)