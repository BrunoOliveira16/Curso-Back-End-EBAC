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