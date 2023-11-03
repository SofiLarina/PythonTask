"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""

from threading import Thread
from queue import Queue

def divisor(num, queue):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    queue.put(result)

def divisors(nums):
    queue = Queue()
    threads = []
    for num in nums:
        t = Thread(target=divisor, args=(num, queue))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    results = []
    while not queue.empty():
        results.append(queue.get())

    return results

if __name__ == '__main__':
    nums = [10, 20, 30, 40, 50]
    threads = []
    queue = Queue()

    for num in nums:
        t = threading.Thread(target=divisor, args=(num, queue))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    results = []
    while not queue.empty():
        results.append(queue.get())

    print(results)