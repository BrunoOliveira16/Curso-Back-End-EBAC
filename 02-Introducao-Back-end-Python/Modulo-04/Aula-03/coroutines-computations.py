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