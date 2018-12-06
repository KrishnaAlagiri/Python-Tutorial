"""
   Multiprocessing Assignment
===================================
Write a python program multiprocessing_assignment.py which calculates the
square of all numbers 1..10 using a separate Process to calculate each number.
Use a shared memory Array to store the results.
(Remember to lock the shared array before manipulating it.)

"""
import os
from multiprocessing import Process, Lock
lock = Lock()

def square(number):
    lock.acquire()
    try:
        result = number * number
    finally:
        lock.release()
    proc = os.getpid()
    print('{0} squared to {1} by process id: {2}'.format(number, result, proc))

if __name__ == '__main__':
    procs = []
    for number in range(1,10):
        proc = Process(target=square, args=(number,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
