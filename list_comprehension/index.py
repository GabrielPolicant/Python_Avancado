#List Comprehension

lista_preco = [0, 200, 300, 400, 500]
nova_lista = []

for preco in lista_preco:
    preco_novo = preco * 2
    nova_lista.append(preco_novo)

lista_nova_2 = [preco * 2 for preco in nova_lista]

print('Lista normal: ', lista_preco)
print('Lista nova: ', nova_lista)
print('Lista nova 2: ', lista_nova_2)

#Misturando com if = Condições de Lógica

lista_3 = [preco for preco in lista_nova_2 if preco / 2]

print('Lista nova 3: ', lista_3)