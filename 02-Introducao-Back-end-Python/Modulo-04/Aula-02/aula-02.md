## 📝 Aula 02: Yields Generators
### Iterator
Um iterator é um objeto que contém um número contável de valores. Um iterator é um objeto que pode ser iterado, o que significa que você pode percorrer todos os valores. Tecnicamente, em Python, um iterator é um objeto que implementa o protocolo de iterator, que consiste nos métodos ``__iter__()`` e ``__next__()``.

Você também pode criar métodos de iterador, que são métodos que produzem um iterator para os elementos dessa classe. Um iterator é um objeto que percorre contêineres, particularmente listas. Os iteradores podem ser usados para executar uma ação em cada item em uma coleção ou para enumerar uma coleção personalizada.

Aqui está um exemplo simples de como criar e usar um iterator em Python:
```
my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
```

Este código cria uma lista chamada ``my_list`` e depois cria um iterator para a lista usando a função ``iter()``. Em seguida, usamos a função ``next()`` para obter cada valor do iterator.

<br>

### Generators
Generators são uma implementação Pythonic de criar iteradores, sem precisar implementar explicitamente uma classe com os métodos ``__iter__()`` e ``__next__()``. Além disso, você não precisa acompanhar o estado interno do objeto.

A palavra-chave ``yield`` é usada para controlar o fluxo de uma função geradora. A declaração vai além para lidar com o estado da função geradora, pausando-a até que seja chamada novamente, usando a função ``next()``.

Aqui está um exemplo simples de como criar uma função geradora em Python usando a palavra-chave ``yield``:
```
def my_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

gen = my_generator(5)

for i in gen:
    print(i)
```

Este código define uma função geradora chamada ``my_generator`` que recebe um argumento n. Dentro da função, usamos um loop ``while`` para gerar valores de 0 a ``n-1``. A palavra-chave ``yield`` é usada para produzir cada valor.

Quando chamamos a função ``my_generator``, ela retorna um objeto gerador que podemos iterar usando um loop ``for``. Cada iteração do loop chama a função geradora e produz o próximo valor.

<br>

Utilizamos um exemplo na aula no arquivo ``generator-example.py``:
```
# Simples função generator
def my_gen():
    n = 1
    print('Primeiro print, n e igual a {}'.format(n))
    # As generators functions contêm declarações de rendimentos
    yield n

    n += 1
    print('Segundo print, n e igual a {}'.format(n))
    yield n

    n += 1
    print('Terceiro e ultimo print, n e igual a {}'.format(n))
    yield n

test = my_gen()

for i in test:
    print(i)
```

A função my_gen é uma função geradora que produz três valores: 1, 2 e 3. Aqui está uma explicação detalhada de como a função funciona:
1. Quando a função é chamada pela primeira vez, ela define uma variável local n com o valor 1.

2. Em seguida, a função imprime uma mensagem informando que ``n`` é igual a 1.

3. A função então usa a palavra-chave ``yield`` para produzir o valor de ``n``, que é 1.

4. Quando a função é chamada novamente, ela retoma a execução logo após a primeira declaração ``yield``. A variável ``n`` é incrementada em 1, então agora tem o valor 2.

5. A função imprime outra mensagem informando que ``n`` é igual a 2.

6. A função usa a palavra-chave ``yield`` novamente para produzir o valor de ``n``, que é 2.

7. Quando a função é chamada pela terceira vez, ela retoma a execução logo após a segunda declaração ``yield``. A variável ``n`` é incrementada novamente em 1, então agora tem o valor 3.

8. A função imprime uma última mensagem informando que ``n`` é igual a 3.

9. A função usa a palavra-chave ``yield`` pela última vez para produzir o valor de ``n``, que é 3.

Depois disso, se a função for chamada novamente, ela não terá mais valores para produzir e lançará um erro ``StopIteration``.