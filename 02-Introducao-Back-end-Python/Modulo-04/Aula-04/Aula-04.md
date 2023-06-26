## 📝 Aula 04: CPU parte 1
### CPU Bound
CPU Bound é um termo usado para descrever programas que são limitados pela capacidade de processamento da CPU. Isso significa que a velocidade de execução do programa é determinada principalmente pela velocidade da CPU e não por outros fatores, como operações de entrada/saída (I/O) ou acesso à memória.

Em Python, a execução de código pode ser limitada pela CPU devido ao Global Interpreter Lock (GIL), que é um mecanismo de segurança implementado no interpretador CPython para garantir a execução segura de código em ambientes multithreaded. O GIL garante que apenas uma thread possa executar código Python por vez, o que pode limitar o desempenho de programas que são CPU Bound.

Para contornar essa limitação, é possível usar a biblioteca multiprocessing do Python para executar código em múltiplos processos simultaneamente, aproveitando ao máximo a capacidade de processamento da CPU.

<br>

### IO/Bound
IO Bound é um termo usado para descrever programas que são limitados principalmente por operações de entrada/saída (I/O), como leitura ou gravação em disco, acesso à rede, etc. Isso significa que a velocidade de execução do programa é determinada principalmente pela velocidade dessas operações e não pela capacidade de processamento da CPU.

Em Python, existem várias estratégias para otimizar programas IO Bound. Uma delas é usar técnicas de programação concorrente, como multithreading ou asyncio, para permitir que o programa continue executando outras tarefas enquanto espera pela conclusão de operações de I/O. Isso pode melhorar significativamente o desempenho de programas IO Bound ao reduzir o tempo de espera e aumentar a utilização da CPU.

<br>

### Python GIL
O Global Interpreter Lock (GIL) é um mecanismo de segurança implementado no interpretador CPython que permite que apenas uma thread execute código Python por vez. Isso significa que, mesmo em um ambiente multithreaded com mais de um núcleo de CPU, apenas uma thread pode estar em um estado de execução a qualquer momento.

O GIL foi criado para resolver problemas relacionados ao gerenciamento de memória em cenários de aplicações concorrentes. O Python usa contagem de referências para gerenciar a memória, o que significa que os objetos criados em Python têm uma variável de contagem de referências que mantém o controle do número de referências que apontam para o objeto. Quando essa contagem chega a zero, a memória ocupada pelo objeto é liberada.

Essa variável de contagem de referências precisava ser protegida contra condições de corrida onde duas threads aumentam ou diminuem seu valor simultaneamente. Se isso acontecer, pode causar vazamento de memória que nunca é liberada ou, pior ainda, liberar incorretamente a memória enquanto ainda existe uma referência ao objeto. Isso pode causar falhas ou outros bugs “estranhos” em seus programas Python.

Para evitar esses problemas, o GIL foi implementado como um único bloqueio no próprio interpretador, adicionando uma regra de que a execução de qualquer bytecode Python requer a aquisição do bloqueio do interpretador. Isso evita deadlocks (já que existe apenas um bloqueio) e não introduz muita sobrecarga de desempenho. No entanto, efetivamente torna qualquer programa Python CPU-bound single-threaded.