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