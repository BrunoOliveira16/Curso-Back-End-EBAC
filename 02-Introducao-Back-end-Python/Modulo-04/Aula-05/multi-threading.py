import time
import threading

def calc_square(numbers):
    print('Calculate square numbers: ')
    for i in numbers:
        #time-delay
        time.sleep(2)
        print('square: {} '.format(str(i * i)))

def calc_cube(numbers):
    print('Calculate cube numbers: ')
    for i in numbers:
        time.sleep(2)
        print('cube: {} '.format(str(i * i * i)))

if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))
    # creating two threads here t1 & t2
    t1.start()
    t2.start()
    # starting threads here parallel by using start function.
    t1.join()
    # this join() will wait until the cal_square() function is finished
    t2.join()
    # this join() will wait until the cal_cube() function is finished
    print('Main Thread Here!!')
    print('Successes!')