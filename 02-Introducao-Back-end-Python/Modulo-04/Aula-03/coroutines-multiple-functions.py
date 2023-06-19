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