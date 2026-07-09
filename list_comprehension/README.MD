# 📚 List Comprehension em Python

## O que é List Comprehension?

**List Comprehension** é uma forma mais elegante e enxuta de criar listas em Python.

Ao invés de utilizar um `for` tradicional juntamente com o método `append()`, podemos criar toda a lista em apenas uma linha de código, deixando o código mais limpo e fácil de entender.

---

## Sintaxe

```python
nova_lista = [expressao for item in iteravel]
```

Onde:

- **expressao** → Valor que será adicionado na nova lista.
- **item** → Cada elemento percorrido.
- **iteravel** → Lista, tupla, string ou qualquer objeto iterável.

Exemplo:

```python
numeros = [1, 2, 3, 4, 5]

dobro = [numero * 2 for numero in numeros]

print(dobro)
```

**Saída**

```python
[2, 4, 6, 8, 10]
```

---

# Comparando com um `for`

### Forma tradicional

```python
lista_preco = [0, 200, 300, 400, 500]
nova_lista = []

for preco in lista_preco:
    preco_novo = preco * 2
    nova_lista.append(preco_novo)

print(nova_lista)
```

### Utilizando List Comprehension

```python
lista_preco = [0, 200, 300, 400, 500]

nova_lista = [preco * 2 for preco in lista_preco]

print(nova_lista)
```

As duas produzem exatamente o mesmo resultado.

---

# Utilizando condições (if)

Também podemos adicionar uma condição para que apenas alguns elementos sejam adicionados à nova lista.

A sintaxe fica assim:

```python
nova_lista = [expressao for item in iteravel if condicao]
```

### Exemplo

Queremos pegar apenas os números pares:

```python
lista = [1, 800, 1200, 1600, 2000]

pares = [numero for numero in lista if numero % 2 == 0]

print(pares)
```

**Resultado**

```python
[800, 1200, 1600, 2000]
```

Neste caso:

- `%` representa o operador de módulo (resto da divisão).
- Quando o resto da divisão por `2` é igual a `0`, significa que o número é par.

---

# Código completo

```python
# List Comprehension

lista_preco = [0, 200, 300, 400, 500]

nova_lista = [preco * 2 for preco in lista_preco]

print("Lista original:", lista_preco)
print("Lista nova:", nova_lista)


# List Comprehension com condição

lista_nova_2 = [1, 800, 1200, 1600, 2000]

lista_3 = [preco for preco in lista_nova_2 if preco % 2 == 0]

print("Lista nova 3:", lista_3)
```

---

# Vantagens

- Código mais limpo.
- Menor quantidade de linhas.
- Fácil leitura quando usada corretamente.
- Muito utilizada em projetos profissionais.
- Geralmente possui desempenho igual ou melhor que o uso de `for` com `append()`.

---

# Resumo

A **List Comprehension** é uma maneira rápida e elegante de criar listas em Python.

Seu formato básico é:

```python
[expressao for item in iteravel]
```

E quando desejamos aplicar alguma regra de filtragem, basta acrescentar um `if`:

```python
[expressao for item in iteravel if condicao]
```

É um recurso bastante utilizado no dia a dia de quem programa em Python e ajuda a deixar o código mais organizado, legível e Pythonico.
