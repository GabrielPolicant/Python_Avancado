# Lambda Functions em Python

## O que são funções Lambda?

As **funções lambda** são funções **anônimas**, ou seja, funções que não precisam ser definidas utilizando `def`.

Elas são ideais para operações simples e rápidas, principalmente quando a função será utilizada apenas uma vez.

Enquanto uma função comum é criada com `def`, uma lambda é escrita em apenas uma linha.

---

## Sintaxe

```python
lambda parametros: expressao
```

A expressão é executada e seu resultado é retornado automaticamente.

**Exemplo:**

```python
dobro = lambda x: x * 2

print(dobro(10))
# Saída: 20
```

Observe que não utilizamos `return`. O retorno é feito automaticamente pela expressão.

---

# Comparando com uma função comum

### Utilizando `def`

```python
def calcular_imposto(preco):
    return preco * 0.3

print(calcular_imposto(1000))
```

### Utilizando `lambda`

```python
calcular_imposto = lambda preco: preco * 0.3

print(calcular_imposto(1000))
```

Ambas produzem exatamente o mesmo resultado.

---

# Entendendo a sintaxe

```python
lambda x: x * 0.3
```

Pode ser lida da seguinte forma:

- `lambda` → indica que estamos criando uma função anônima.
- `x` → parâmetro recebido pela função.
- `:` → separa os parâmetros da expressão.
- `x * 0.3` → expressão que será executada e retornada.

É muito comum utilizar nomes curtos como `x`, `n` ou `item`, mas nada impede utilizar nomes mais descritivos.

```python
lambda preco: preco * 0.3
```

Também é perfeitamente válido.

---

# Quando utilizar Lambda?

As funções lambda são mais úteis quando precisamos passar uma função como argumento para outra função.

Os casos mais comuns são:

- `map()`
- `filter()`
- `sorted()`
- `max()`
- `min()`

Nessas situações, criar uma função completa com `def` muitas vezes seria desnecessário.

---

# Exemplo com `map()`

O `map()` aplica uma função para cada elemento de um iterável.

Sem lambda:

```python
def calcular_imposto(preco):
    return preco * 0.3

precos = [100, 200, 300, 400]

impostos = list(map(calcular_imposto, precos))

print(impostos)
```

Com lambda:

```python
precos = [100, 200, 300, 400]

impostos = list(map(lambda x: x * 0.3, precos))

print(impostos)
```

Saída:

```python
[30.0, 60.0, 90.0, 120.0]
```

---

# Outro exemplo

Ordenando pessoas pela idade.

```python
pessoas = [
    {"nome": "Gabriel", "idade": 22},
    {"nome": "Lucas", "idade": 18},
    {"nome": "Ana", "idade": 25}
]

ordenado = sorted(pessoas, key=lambda pessoa: pessoa["idade"])

print(ordenado)
```

Nesse caso, a lambda informa ao `sorted()` que a ordenação deve ser feita pela idade.

---

# Vantagens

- Código mais curto.
- Ótima para funções simples.
- Muito utilizada com `map()`, `filter()` e `sorted()`.
- Evita criar funções que serão usadas apenas uma vez.

---

# Desvantagens

- Só pode conter **uma única expressão**.
- Não é indicada para regras de negócio complexas.
- Pode prejudicar a legibilidade quando fica muito extensa.

Sempre que a lógica começar a crescer, prefira utilizar uma função tradicional com `def`.

---

# Resumo

- `lambda` cria funções anônimas.
- Não utiliza `return`, pois o retorno é automático.
- Deve conter apenas uma expressão.
- É ideal para funções pequenas e temporárias.
- Seu uso é muito comum com `map()`, `filter()`, `sorted()`, `max()` e `min()`.
- Se a lógica ficar complexa, prefira utilizar `def`.
