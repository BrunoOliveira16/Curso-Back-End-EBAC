## 📝 Aula 08: Bubble Sort
Bubble Sort é um algoritmo de ordenação simples que compara elementos adjacentes em uma lista e os troca de lugar se estiverem fora de ordem. O processo é repetido várias vezes até que a lista esteja completamente ordenada.

O Bubble Sort é fácil de entender e implementar, mas não é muito eficiente para listas grandes, pois tem uma complexidade de tempo média e pior caso de O(n^2), onde n é o número de elementos na lista. Existem outros algoritmos de ordenação mais eficientes, como o Quick Sort e o Merge Sort, que podem ser usados para ordenar listas grandes mais rapidamente.

O código abaixo define uma função bubble_sort que implementa o algoritmo Bubble Sort para ordenar uma lista. A função recebe como argumento uma lista não ordenada unsorted_list e a ordena usando o algoritmo Bubble Sort. O algoritmo funciona percorrendo a lista várias vezes e comparando elementos adjacentes. Se dois elementos estiverem fora de ordem, eles são trocados de lugar. O processo é repetido até que a lista esteja completamente ordenada. A função retorna a lista ordenada.
```
def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):

        for j in range(len(unsorted_list) - 1):
            if unsorted_list[j] > unsorted_list[j+1]:

                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

    return unsorted_list
```

O segundo código define e executa um teste unitário para a função bubble_sort usando o módulo unittest. Ele importa a função bubble_sort do módulo bubble_sort e define uma classe de teste chamada TestBubbleSort que herda de unittest.TestCase. Dentro desta classe, um método de teste chamado test_bubble_sort é definido.

O método test_bubble_sort define uma lista não ordenada e uma lista esperada. Em seguida, ele chama a função bubble_sort com a lista não ordenada e verifica se o resultado retornado pela função é igual à lista esperada usando o método assertEqual do unittest.TestCase.

No final do script, há uma verificação para ver se o script está sendo executado diretamente (em vez de ser importado como um módulo). Se for o caso, os testes são executados chamando unittest.main().
```
import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        unsorted_list = [66, 11, 4, 8, 1, 70]
        expected_list = [1, 4, 8, 11, 66, 70]

        unsorted_list = bubble_sort(unsorted_list)
        print(unsorted_list)
        self. assertEqual(unsorted_list, expected_list)
    
if __name__ == '__main__':
    unittest.main()
```

### Resumo
Em resumo, o primeiro código define uma função que implementa o algoritmo Bubble Sort para ordenar uma lista, enquanto o segundo código define e executa um teste unitário para verificar se a função está funcionando corretamente.