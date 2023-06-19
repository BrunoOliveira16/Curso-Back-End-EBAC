## 📝 Aula 03: Coroutines
### Coroutines
Coroutines são uma forma de realizar multitarefas cooperativas, suspendendo e retomando em pontos definidos pelo programador. Em Python, coroutines são semelhantes a geradores, mas com alguns métodos extras e pequenas mudanças na forma como usamos as declarações de yield. Geradores produzem dados para iteração enquanto coroutines também podem consumir dados.

#### Exemplo 01: coroutines-example.py
```
def func():
    print('Function Starts')

    #Pause
    yield

    print('End of function')


try:
    y = func()
    print(type(y))
    next(y)
    next(y)
except StopIteration as error:
    pass
```
Este é um exemplo de uma função geradora em Python. Quando a função func é chamada, ela retorna um objeto gerador (y), que é um iterador. A primeira chamada de next(y) inicia a execução da função func e executa até encontrar a declaração yield, que pausa a execução e retorna o controle para o chamador. Neste caso, a saída seria “Function Starts”.

A segunda chamada de next(y) retoma a execução da função func a partir do ponto em que foi pausada e continua até o final da função ou até encontrar outra declaração yield. Neste caso, a saída seria “End of function”.

Como não há mais declarações yield na função, uma terceira chamada de next(y) levantaria uma exceção StopIteration, indicando que não há mais valores a serem gerados. Essa exceção é capturada pelo bloco try/except e silenciada com o comando pass.

A saída deste exemplo será:
```
<class 'generator'>
Function Starts
End of function
```

<br>

#### Exemplo 02: coroutines-computations.py
```
def func():
    x = 5
    print('Function Part 1')

    yield x
    x += 7
    print('Function Part 2')

    yield x

    print('Function Part 3')


try:
    y = func()
    z = next(y)     # Function Part 1 executed
    print(z)

    z = next(y)     # Function Part 2 executed
    print(z)

    z = next(y)     # Function Part 3 executed and StopIteration exception raised
    print(z)        # This print will not be executed

except StopIteration as error:
    pass
```
Este é outro exemplo de uma função geradora em Python. Quando a função func é chamada, ela retorna um objeto gerador (y), que é um iterador. A primeira chamada de next(y) inicia a execução da função func e executa até encontrar a primeira declaração yield, que pausa a execução e retorna o valor de x (que é 5) para o chamador. Neste caso, a saída seria “Function Part 1” e “5”.

A segunda chamada de next(y) retoma a execução da função func a partir do ponto em que foi pausada e continua até encontrar a segunda declaração yield. Neste caso, o valor de x é incrementado em 7 (tornando-se 12) e a saída seria “Function Part 2” e “12”.

A terceira chamada de next(y) retoma a execução da função func a partir do ponto em que foi pausada e continua até o final da função. Neste caso, a saída seria “Function Part 3”. Como não há mais declarações yield na função, uma quarta chamada de next(y) levantaria uma exceção StopIteration, indicando que não há mais valores a serem gerados. Essa exceção é capturada pelo bloco try/except e silenciada com o comando pass.

A saída final deste código seria:
```
Function Part 1
5
Function Part 2
12
Function Part 3
```

<br>

#### Exemplo 03: coroutines-send-values.py
```
def func():
    print('Function part 1')

    x = yield
    print(x)
    print('Function part 2')

    a = yield
    print(a)
    print('Function part 3')


try:
    y = func()

    next(y)     #Function part 1 executed, to reach the first yield we used next

    y.send(6)   #Function part 2 executed and value sent 6

    y.send(12)  #Function part 3 executed and value sent 12 and StopIteration raised

except StopIteration as error:
    pass
```
Este é um exemplo de uma função geradora em Python que usa o método ``send`` para enviar valores para a função geradora. Quando a função func é chamada, ela retorna um objeto gerador (``y``), que é um iterador. A primeira chamada de ``next(y)`` inicia a execução da função func e executa até encontrar a primeira declaração ``yield``, que pausa a execução e aguarda um valor ser enviado para a função geradora. Neste caso, a saída seria “Function part 1”.

A primeira chamada de ``y.send(6)`` retoma a execução da função func a partir do ponto em que foi pausada e envia o valor 6 para a função geradora. O valor enviado é atribuído à variável x e impresso. A execução continua até encontrar a segunda declaração ``yield``, que pausa a execução e aguarda outro valor ser enviado para a função geradora. Neste caso, a saída seria “6” e “Function part 2”.

A segunda chamada de ``y.send(12)`` retoma a execução da função func a partir do ponto em que foi pausada e envia o valor 12 para a função geradora. O valor enviado é atribuído à variável a e impresso. A execução continua até o final da função. Neste caso, a saída seria “12” e “Function part 3”. Como não há mais declarações ``yield`` na função, uma terceira chamada de ``next(y)`` ou ``y.send()`` levantaria uma exceção StopIteration, indicando que não há mais valores a serem gerados. Essa exceção é capturada pelo bloco try/except e silenciada com o comando pass.

A saída final deste código seria:

```
Function part 1
6
Function part 2
12
Function part 3
```

<br>

#### Exemplo 04: coroutines-multiple-functions.py
```
def func1():
    print('Function 1 part 1')

    yield
    print('Function 1 part 2')

    yield
    print('Function 1 part 3')

    yield
    print('Function 1 part 4')

    yield
    print('Function 1 part 5')


def func2():
    print('Function 2 part 1')

    yield
    print('Function 2 part 2')

    yield
    print('Function 2 part 3')

    yield
    print('Function 2 part 4')

    yield
    print('Function 2 part 5')


try:
    a = func1()
    b = func2()

    next(a)     # Will execute Function 1 part 1
    next(b)     # Will execute Function 2 part 1
    next(a)     # Will execute Function 1 part 2
    next(a)     # Will execute Function 1 part 3
    next(b)     # Will execute Function 1 part 2
    next(b)     # Will execute Function 1 part 3
    next(b)     # Will execute Function 1 part 4
    next(a)     # Will execute Function 1 part 4
    next(a)     # Will execute Function 1 part 5 and raise StopIteration exception

except StopIteration as error:
    pass
```
Este é um exemplo de duas funções geradoras em Python sendo executadas de forma intercalada. Quando as funções func1 e func2 são chamadas, elas retornam objetos geradores (a e b, respectivamente), que são iteradores.

A primeira chamada de next(a) inicia a execução da função func1 e executa até encontrar a primeira declaração yield, que pausa a execução. Neste caso, a saída seria “Function 1 part 1”.

A primeira chamada de next(b) inicia a execução da função func2 e executa até encontrar a primeira declaração yield, que pausa a execução. Neste caso, a saída seria “Function 2 part 1”.

A segunda chamada de next(a) retoma a execução da função func1 a partir do ponto em que foi pausada e continua até encontrar a segunda declaração yield, que pausa a execução novamente. Neste caso, a saída seria “Function 1 part 2”.

A terceira chamada de next(a) retoma a execução da função func1 a partir do ponto em que foi pausada e continua até encontrar a terceira declaração yield, que pausa a execução novamente. Neste caso, a saída seria “Function 1 part 3”.

A segunda chamada de next(b) retoma a execução da função func2 a partir do ponto em que foi pausada e continua até encontrar a segunda declaração yield, que pausa a execução novamente. Neste caso, a saída seria “Function 2 part 2”.

As chamadas subsequentes de next(a) e next(b) continuam alternando entre as duas funções geradoras até que uma delas chegue ao final e levante uma exceção StopIteration, indicando que não há mais valores a serem gerados. Essa exceção é capturada pelo bloco try/except e silenciada com o comando pass.

A saída final deste código seria:
```
Function 1 part 1
Function 2 part 1
Function 1 part 2
Function 1 part 3
Function 2 part 2
Function 2 part 3
Function 2 part 4
Function 1 part 4
Function 1 part 5
```

<br>

### Saiba Mais
#### Gerador
Um gerador é um tipo especial de iterador em Python que permite iterar sobre uma sequência de valores sem armazenar todos os valores na memória ao mesmo tempo. Geradores são criados usando funções geradoras, que são funções que usam a palavra-chave ``yield`` em vez de return para retornar valores.

Quando uma função geradora é chamada, ela retorna um objeto gerador, que pode ser iterado usando o método ``next()`` ou em um loop ``for``. A cada chamada de ``next()``, a função geradora é executada até encontrar uma declaração ``yield``, que retorna o valor e pausa a execução da função. A próxima chamada de ``next()`` retoma a execução da função a partir do ponto em que foi pausada e continua até encontrar outra declaração ``yield`` ou até o final da função.

Geradores são úteis quando se trabalha com grandes conjuntos de dados ou quando se deseja gerar valores sob demanda sem armazená-los todos na memória ao mesmo tempo.

<br>

#### Quais são as diferenças entre geradores e coroutines?
Geradores e coroutines são conceitos relacionados em Python, mas têm algumas diferenças importantes. Geradores são funções que usam a palavra-chave yield para retornar valores um de cada vez, sem armazenar todos os valores na memória ao mesmo tempo. Eles são úteis quando se trabalha com grandes conjuntos de dados ou quando se deseja gerar valores sob demanda.

Coroutines, por outro lado, são uma forma de realizar multitarefas cooperativas, suspendendo e retomando em pontos definidos pelo programador. Em Python, coroutines são semelhantes a geradores, mas com alguns métodos extras e pequenas mudanças na forma como usamos as declarações de yield. Geradores produzem dados para iteração enquanto coroutines também podem consumir dados.

Uma das principais diferenças entre geradores e coroutines é que geradores são usados principalmente para produzir valores, enquanto coroutines podem ser usadas tanto para produzir quanto para consumir valores. Além disso, coroutines podem ser usadas para realizar multitarefas cooperativas de maneira mais flexível do que geradores.