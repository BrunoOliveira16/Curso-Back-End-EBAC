## 📝 Aula 06: TDD
### Introdução a TDD
O TDD (Test-Driven Development ou Desenvolvimento Orientado a Testes) é uma metodologia de desenvolvimento de software que enfatiza a escrita de testes antes do código de produção. Ele é parte do processo de desenvolvimento ágil, utilizado em metodologias como o XP (Programação Extrema) e sendo uma das técnicas que auxiliam na melhoria de qualidade do processo de desenvolvimento.

O processo de TDD é iterativo e segue os seguintes passos:

- Escreva um teste para uma nova funcionalidade.
- Execute o teste e verifique se ele falha (o que é esperado, já que a funcionalidade ainda não foi implementada).
- Escreva o código de produção mínimo necessário para fazer o teste passar.
- Execute o teste novamente e verifique se ele passa.
- Refatore o código de produção para melhorar sua qualidade, mantendo os testes passando.

Esses passos são repetidos para cada nova funcionalidade ou mudança no código. O objetivo do TDD é garantir que o código esteja correto e bem projetado, pois cada mudança é validada por testes automatizados. Além disso, os testes servem como documentação viva do comportamento esperado do código.

O TDD pode levar a um código mais limpo, modular e fácil de manter, pois incentiva a refatoração constante e a escrita de testes abrangentes. No entanto, ele requer disciplina e prática para ser aplicado corretamente, e pode aumentar o tempo inicial de desenvolvimento devido à necessidade de escrever testes antes do código de produção.

<br>

### Níveis de testes

Além do TDD, existem vários níveis de testes que podem ser aplicados durante o processo de desenvolvimento de software. Os principais níveis são:

- ``Teste unitário:`` testa individualmente as menores unidades do código, como funções ou métodos.
- ``Teste de integração:`` testa como diferentes partes do sistema funcionam juntas.
- ``Teste de sistema:`` testa o sistema como um todo, incluindo sua interface com outros sistemas.
- ``Teste de aceitação:`` testa se o sistema atende aos requisitos do usuário e se está pronto para ser lançado.

Cada nível de teste tem um objetivo diferente e pode ajudar a garantir a qualidade do software em diferentes estágios do processo de desenvolvimento. A combinação desses níveis de teste com a prática do TDD pode levar a um software mais robusto e confiável.

<br>

### Quais são as vantagens e desvantagens do TDD
O TDD (Test-Driven Development ou Desenvolvimento Orientado a Testes) é uma metodologia de desenvolvimento de software que tem várias vantagens, mas também algumas desvantagens. Aqui estão algumas das principais vantagens e desvantagens do TDD:

#### Vantagens:

- ``Melhoria da qualidade do código:`` Como os testes são escritos antes do código de produção, o TDD incentiva a refatoração constante e a escrita de testes abrangentes, o que pode levar a um código mais limpo, modular e fácil de manter.
- ``Redução de bugs:`` Como cada mudança no código é validada por testes automatizados, o TDD pode ajudar a reduzir o número de bugs no código e tornar mais fácil identificar e corrigir problemas.
- ``Documentação viva:`` Os testes servem como documentação viva do comportamento esperado do código, tornando mais fácil para outros desenvolvedores entenderem como o código funciona e como ele deve ser usado.
- ``Facilita mudanças:`` Como o código é constantemente testado e refatorado, é mais fácil fazer mudanças sem introduzir novos bugs ou quebrar funcionalidades existentes.

#### Desvantagens:

- ``Aumento do tempo inicial de desenvolvimento:`` Como os testes são escritos antes do código de produção, o TDD pode aumentar o tempo inicial de desenvolvimento. No entanto, esse tempo pode ser compensado pela redução de bugs e pela facilidade de manutenção do código a longo prazo.
- ``Necessidade de disciplina e prática:`` O TDD requer disciplina para escrever testes antes do código de produção e para refatorar constantemente o código. Além disso, é preciso prática para escrever testes eficazes e para aplicar corretamente a metodologia.
- ``Pode levar a testes excessivos:`` Como o TDD enfatiza a escrita de testes, é possível escrever testes excessivos ou desnecessários, o que pode aumentar o tempo de desenvolvimento sem trazer benefícios significativos.

Em resumo, o TDD tem várias vantagens, como a melhoria da qualidade do código, a redução de bugs e a documentação viva. No entanto, ele também tem algumas desvantagens, como o aumento do tempo inicial de desenvolvimento e a necessidade de disciplina e prática. É importante avaliar essas vantagens e desvantagens ao decidir se o TDD é adequado para um projeto específico.

<br>

### Exemplo
Código para efetuar teste nas funções ``addition_operation`` e ``subtraction_operation``
```
import unittest
from math_operations import addition_operation
from math_operations import subtraction_operation

class TestMathOperations(unittest.TestCase):
    def test_addition_operation(self):
        match_addition_result = addition_operation(num_1=5, num_2=10)
        self.assertEqual(match_addition_result, 15)
    
    def test_subtraction_operation(self):
        match_subtraction_result = subtraction_operation(num_1=10, num_2=10)
        self.assertEqual(match_subtraction_result, 0)


if __name__ == '__main__':
    unittest.main()
```

<br>

Funções a serem testadas de ``math_operations``:
```
def addition_operation(num_1, num_2):
    addition = num_1 + num_2
    return addition

def subtraction_operation(num_1, num_2):
    subtraction = num_1 - num_2
    return subtraction
```

O primeiro código define duas funções, ``addition_operation`` e ``subtraction_operation``, que realizam operações matemáticas básicas de adição e subtração, respectivamente. Cada função recebe dois argumentos, ``num_1`` e ``num_2``, e retorna o resultado da operação.

O segundo código define e executa testes unitários para as funções ``addition_operation`` e ``subtraction_operation`` usando o módulo ``unittest``. Ele importa as funções do módulo ``math_operations`` e define uma classe de teste chamada ``TestMathOperations`` que herda de ``unittest.TestCase``. Dentro desta classe, dois métodos de teste são definidos, ``test_addition_operation`` e ``test_subtraction_operation``, que testam as funções ``addition_operation`` e ``subtraction_operation``, respectivamente. Cada método de teste chama a função apropriada com valores de entrada específicos e verifica se o resultado retornado é igual ao valor esperado usando o método ``assertEqual`` do ``unittest.TestCase``.

No final do script, há uma verificação para ver se o script está sendo executado diretamente. Os testes são executados chamando ``unittest.main()``.