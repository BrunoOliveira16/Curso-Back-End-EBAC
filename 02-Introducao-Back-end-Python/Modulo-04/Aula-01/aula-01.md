## 📝 Aula 01: Introdução a programação assincrona e multi processos 
A programação assíncrona é uma alternativa à programação síncrona. Na programação síncrona, as tarefas são executadas exatamente uma após a outra. No modelo assíncrono, tem-se a capacidade de atender a múltiplas requisições simultaneamente de forma concorrente ou em paralelo. A programação assíncrona é diferente do paralelismo, onde você não vai rodar dois processos ao mesmo tempo. Você vai rodar 1 processo e a medida que ele estiver rodando pode acontecer de ele travar ou ficar em espera por algum motivo. Quando isso acontece se inicia um segundo processo assíncrono.

Python possui integrada ao seu core a biblioteca asyncio, que permite a construção de código assíncrono não bloqueante3. Essa estrutura de programação assíncrona é relativamente recente no Python, sendo lançada somente após a versão 3.4 do Python.

<br>

### Multi processos
Multiprocessamento é o uso de duas ou mais unidades centrais de processamento (CPUs) dentro de um único sistema de computador. O termo também se refere à capacidade de um sistema suportar mais de um processador ou a capacidade de alocar tarefas entre eles.

Em Python, o módulo de multiprocessamento inclui uma API muito simples e intuitiva para dividir o trabalho entre vários processos. Você pode usar a classe ``Process`` para criar um processo e a classe ``Pool`` para definir um pool de processamento. O módulo de multiprocessamento também fornece uma classe ``Manager`` que controla um processo do servidor e permite que outros processos manipulem objetos Python usando proxies.

Este é um exemplo simples de como usar o módulo de multiprocessamento em Python para criar dois processos que executam funções diferentes:
```
import multiprocessing

def print_cube(num):
    print("Cube: {}".format(num * num * num))

def print_square(num):
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Done!")
```
Este código cria dois processos usando a classe ``Process``. O primeiro processo tem como alvo a função ``print_square`` e o segundo processo tem como alvo a função ``print_cube``. Ambos os processos são iniciados com o método ``start()`` e depois esperamos que ambos terminem com o método ``join()`` antes de imprimir “Done!”.