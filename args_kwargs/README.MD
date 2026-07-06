# 📘 Resumo de Estudos — \*args e \*\*kwargs em Python

Este material reúne os principais conceitos sobre `*args` e `**kwargs`, explicando como eles funcionam, quando utilizá-los e algumas boas práticas para escrever funções mais flexíveis e organizadas.

---

# Args e Kwargs

Ao chamar uma função em Python, podemos passar argumentos de três formas:

- **Por posição** (Positional Arguments)
- **Pelo nome do parâmetro** (Keyword Arguments)
- **Misturando os dois**, desde que os argumentos posicionais venham primeiro.

## Exemplo

```python
def minha_funcao(valor):
    ...

minha_funcao(10)

minha_funcao(valor=10)
```

---

## Funções com mais de um parâmetro

```python
def minha_funcao(valor1, valor2):
    ...
```

Podemos chamar a função das seguintes maneiras:

```python
minha_funcao(10, 20)

minha_funcao(valor1=10, valor2=20)

minha_funcao(valor2=20, valor1=10)
```

> **Observação:** Quando utilizamos argumentos nomeados (_keyword arguments_), a ordem deixa de importar.

---

# \*args

O `*args` permite que uma função receba uma quantidade variável de **argumentos posicionais**.

```python
def minha_funcao(valor, *args):
    ...
```

Todos os argumentos extras enviados para a função são agrupados em uma **tupla**.

### Exemplo

```python
def soma(*args):
    print(args)

soma(10, 20, 30)
```

**Saída**

```python
(10, 20, 30)
```

---

## O nome `args` é obrigatório?

Não.

O nome `args` é apenas uma convenção da comunidade Python.

Podemos escrever:

```python
def minha_funcao(*numeros):
    ...
```

O funcionamento será exatamente o mesmo.

---

# Boas práticas com \*args

O ideal é que todos os elementos enviados para `*args` representem o mesmo tipo de informação.

### ✔ Bom exemplo

```python
def calcular_preco(valor_produto, *impostos):
    ...
```

Neste caso, todos os valores extras representam impostos.

---

### ❌ Mau exemplo

```python
calcular_preco(100, "Gabriel", True, 0.15)
```

Cada argumento representa uma informação diferente, tornando o código confuso e difícil de manter.

---

# \*\*kwargs

O `**kwargs` permite que uma função receba uma quantidade variável de **argumentos nomeados** (_keyword arguments_).

```python
def minha_funcao(**kwargs):
    ...
```

O Python reúne todos esses argumentos em um **dicionário**, onde:

- a **chave** é o nome informado;
- o **valor** é o valor passado.

---

## Exemplo

```python
def minha_funcao(**kwargs):
    print(kwargs)

minha_funcao(nome="Gabriel", idade=25)
```

**Saída**

```python
{
    "nome": "Gabriel",
    "idade": 25
}
```

---

## O nome `kwargs` é obrigatório?

Também não.

Assim como `args`, trata-se apenas de uma convenção.

```python
def minha_funcao(**dados):
    ...
```

Funciona exatamente da mesma forma.

---

# \*args e \*\*kwargs são opcionais

Não somos obrigados a passar valores para `*args` ou `**kwargs`.

Exemplo:

```python
def exemplo(*args, **kwargs):
    print(args)
    print(kwargs)

exemplo()
```

**Resultado**

```python
()
{}
```

Ou seja:

- `args` será uma **tupla vazia**.
- `kwargs` será um **dicionário vazio**.

---

# Ordem correta dos parâmetros

Existe uma ordem recomendada para declarar parâmetros em uma função Python.

```python
def funcao(parametros_normais, *args, **kwargs):
    ...
```

A ordem é:

1. Parâmetros comuns;
2. `*args`;
3. `**kwargs`.

### Exemplo

```python
def cadastro(nome, idade, *telefones, **dados):
    ...
```

---

# Resumo Final

| Recurso           | Recebe                            | Tipo armazenado     |
| ----------------- | --------------------------------- | ------------------- |
| Parâmetros comuns | Valores fixos                     | Variável normal     |
| `*args`           | Argumentos posicionais ilimitados | Tupla (`tuple`)     |
| `**kwargs`        | Argumentos nomeados ilimitados    | Dicionário (`dict`) |

---

# Exemplo completo

```python
def cadastro(nome, idade, *telefones, **dados):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Telefones: {telefones}")
    print(f"Dados extras: {dados}")

cadastro(
    "Gabriel",
    25,
    "18 99999-1111",
    "18 98888-2222",
    cidade="Assis",
    profissao="Analista de Dados"
)
```

**Saída**

```python
Nome: Gabriel
Idade: 25
Telefones: ('18 99999-1111', '18 98888-2222')
Dados extras: {
    'cidade': 'Assis',
    'profissao': 'Analista de Dados'
}
```

---

# Principais pontos para lembrar

- `*args` recebe **quantos argumentos posicionais forem necessários**.
- `**kwargs` recebe **quantos argumentos nomeados forem necessários**.
- `args` é armazenado como uma **tupla**.
- `kwargs` é armazenado como um **dicionário**.
- Os nomes `args` e `kwargs` são apenas convenções.
- Não é obrigatório passar valores para `*args` ou `**kwargs`.
- A ordem correta na declaração é:
  1. Parâmetros comuns
  2. `*args`
  3. `**kwargs`

- Prefira que todos os elementos de `*args` representem o mesmo tipo de informação para manter o código legível e organizado.
