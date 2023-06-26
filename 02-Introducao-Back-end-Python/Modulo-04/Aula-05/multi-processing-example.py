import multiprocessing

# Creating a global variable
results = []

def calc_square(numbers):
    global results
    for i in numbers:
        print('square: ', str(i * i))
        results.append(i * i)
        print('Within a result: ' + str(results))

if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    # creating one Process here p1
    p1.start()
    # starting Processes here parallel by using start function.
    p1.join()
    # this join() will wait until the cal_square() function is finished
    print('result: ' + str(results))
    # this print didn't work here we have to print it within the process
    print('Successes!')