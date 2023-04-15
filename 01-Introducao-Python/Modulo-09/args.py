from sys import argv

print(argv)
print(type(argv))

posicao_arg = 0
for arg in argv:
    print(posicao_arg)
    print(arg)
    print(type(arg))
    posicao_arg = posicao_arg + 1