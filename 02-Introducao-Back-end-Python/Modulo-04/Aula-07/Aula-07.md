## 📝 Aula 07: Binary Search
A pesquisa binária (binary search) é um algoritmo de busca eficiente para encontrar um elemento em uma lista ordenada. Ele funciona dividindo repetidamente a lista pela metade até encontrar o elemento desejado ou determinar que ele não está presente na lista.

Aqui está um exemplo de implementação da função ``binary_search`` em Python:
```
def binary_search(array, x, low, high):

    #Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binary_search(array, x, 0, len(array)-1)

if result != -1:
    print('Element is present at index ' + str(result))
else:
    print('Element not found')
```
Este código define e usa uma função ``binary_search`` para encontrar um elemento em uma lista ordenada. A função ``binary_search`` recebe como argumentos um ``array`` ordenado, um valor ``x`` a ser procurado, e os índices ``low`` e ``high`` que definem o intervalo de busca. A função retorna o índice do elemento ``x`` no ``array`` se ele estiver presente, ou -1 caso contrário.

O código começa definindo a função ``binary_search``, que implementa o algoritmo de pesquisa binária. Dentro da função, há um loop ``while`` que é executado enquanto os ponteiros ``low`` e ``high`` não se encontrarem. Dentro do loop, o índice médio (``mid``) do intervalo de busca é calculado e o elemento nesse índice é comparado com o valor ``x``. Se o elemento for igual a ``x``, o índice é retornado. Caso contrário, o intervalo de busca é atualizado para a metade esquerda ou direita do intervalo atual, dependendo se o elemento é menor ou maior que ``x``. Se o elemento não for encontrado, a função retorna -1.

Depois de definir a função ``binary_search``, o código define um ``array`` ordenado e um valor ``x`` a ser procurado. Em seguida, ele chama a função ``binary_search`` com esses valores e os índices apropriados para o intervalo de busca. O resultado retornado pela função é armazenado na variável result.

Finalmente, o código verifica se o resultado é diferente de -1 (o que indica que o elemento foi encontrado) e imprime uma mensagem indicando o índice do elemento no ``array``. Caso contrário, ele imprime uma mensagem indicando que o elemento não foi encontrado.

Ao executar este código, ele deve imprimir a mensagem “Element is present at index 1”, indicando que o elemento 4 está presente no índice 1 do ``array``.

<br>

### Módulo unittest
unittest é um módulo de teste de unidade embutido no Python que permite escrever e executar testes automatizados para o seu código. Ele fornece uma estrutura para definir casos de teste, agrupá-los em conjuntos de testes e executá-los para verificar se o código está funcionando corretamente.

O código abaixo define e executa um teste para a função binary_search usando o módulo unittest:
```
import unittest
from binary_search import binary_search

class TestBubleSort(unittest.TestCase):
    def test_binary_search(self):
        array = [3, 4, 5, 6, 7, 8, 9]
        find = 4

        result = binary_search(array, find, 0, len(array)-1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored']) # Passando o argumento argv para ignorar os argumentos da linha de comando em ambientes interativos
```

Este código define e executa um teste para a função ``binary_search`` usando o módulo unittest do Python. Primeiro, o módulo ``unittest`` e a função ``binary_search`` são importados. Em seguida, uma classe de teste chamada ``TestBubleSort`` é definida, que herda de ``unittest.TestCase``. Dentro desta classe, um método de teste chamado ``test_binary_search`` é definido.

O método ``test_binary_search`` define um array de entrada e um valor a ser procurado. Em seguida, ele chama a função ``binary_search`` com esses valores e verifica se o resultado retornado pela função é igual ao valor esperado (1) usando o método ``assertEqual`` do ``unittest.TestCase``.

No final do script, há uma verificação para ver se o script está sendo executado diretamente (em vez de ser importado como um módulo). Se for o caso, os testes são executados chamando ``unittest.main()`` com o argumento ``argv=['first-arg-is-ignored']`` para ignorar os argumentos da linha de comando em ambientes interativos.

Em resumo, este código define e executa um teste para a função ``binary_search``, verificando se ela retorna o valor correto para um caso de teste específico.