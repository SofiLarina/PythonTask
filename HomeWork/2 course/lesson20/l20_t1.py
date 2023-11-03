"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""
import multiprocessing

def sum_even(start, end):
    total = 0
    for num in range(start, end+1):
        if num % 2 == 0:
            total += num
    return total

def sum_odd(start, end):
    total = 0
    for num in range(start, end+1):
        if num % 2 != 0:
            total += num
    return total

if __name__ == "__main__":
    start = 1
    end = 1000000

    p1 = multiprocessing.Process(target=sum_even, args=(start, end))
    p2 = multiprocessing.Process(target=sum_odd, args=(start, end))

    p1.start()
    p2.start()

    p1.join()
    p2.join()