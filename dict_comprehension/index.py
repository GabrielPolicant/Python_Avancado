lista_num = [1,2,3,4,5,6]

dict_num = {num: num * 2 for num in lista_num}
print(dict_num)

dict_num = {num: num * 2 for num in lista_num if num % 2 == 0}
print(dict_num)

precos = {
    "Notebook": 3500,
    "Mouse": 80,
    "Teclado": 200
}

novos_precos = {produto: preco * 0.9 for produto, preco in precos.items()}
print(novos_precos)