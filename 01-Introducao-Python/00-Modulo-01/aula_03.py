# -*- coding: utf-8 -*-
"""module_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QY0zf-yBrHEtqRnw-4FqRPk4RjeK0uWt

**Módulo 1 - Váriaveis & Tipos de Dados**
- Aula 3: Números

**3.1. Motivação**

Você precisa calcular o **ticket médio** diário **tkt** do seu restaurante. A métrica é calculada pela soma do valor das vendas **svv** de um mesmo dia dividido pela quantidade de vendas **sqv** , também de um mesmo dia.

*$tkt = svv / sqv$*

Esta é a sua planilha:

![image.png](data:image/png;base64,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)

Como podemos fazer este cálculo usando o Python?

**3.2. Definição**

Armazenam valores numéricos:
- 10, 37, 500 (inteiros);
- 0.333, 10.1 (decimais);
- 1 + 2j (complexos).

São dos tipos:
- int (inteiros);
- float (decimais);
- complex (complexos).
"""

print(type(37))
print(type(10.15))
print(type(1 + 2j))

"""**3.3. Operações**

As operações dos tipos numéricos são as quatro operações matemáticas fundamentais:
- +(soma);
- -(subtração);
- *(multiplicação);
- /(divisão).

Além de operações mais avançadas:
- //(divisão inteira)
- **(potência ou exponenciação);
- %(resto de divisão).

**Exemplo:** Carrinho de compra de um e-commerce.

"""

qtd_items_carrinho_compra = 0

qtd_items_carrinho_compra = qtd_items_carrinho_compra + 1
print(qtd_items_carrinho_compra)

qtd_items_carrinho_compra = qtd_items_carrinho_compra + 1
print(qtd_items_carrinho_compra)

qtd_items_carrinho_compra = 0

qtd_items_carrinho_compra += 1
print(qtd_items_carrinho_compra)

qtd_items_carrinho_compra += 1
print(qtd_items_carrinho_compra)

"""**Exemplo:** Total a pagar de um produto"""

preco = 47
quantidade = 0.250

total_a_pagar = quantidade * preco
print(total_a_pagar)

a = 3
b = 2

c = a / b
print(c)
print(type(c))

d = a // b
print(d)
print(type(d))

"""**3.4. Conversão**

Podemos converter os tipos numéricos entre si utilizando o método nativo *int*, *float* e *complex*:
"""

print(int(3.9))

print(float(10))

print(complex(1))

"""**3.5. Revisitando a motivação**

![image.png](data:image/png;base64,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)

Ticket médio diário do dia 19/01.
"""

svv_19 = 153.98
sqv_19 = 3

tkt_19 = svv_19 / sqv_19
print(tkt_19)

"""Ticket médio diário do dia 20/01."""

svv_20 = 337.01
sqv_20 = 7

tkt_20 = svv_20 / sqv_20
print(tkt_20)

"""Ticket médio diário do dia 23/01."""

svv_23 = 295.33
sqv_23 = 5

tkt_23 = svv_23 / sqv_23
print(tkt_23)

"""Ticket Médio"""

tkt = (tkt_19 + tkt_20 + tkt_23) / 3
print(tkt)
