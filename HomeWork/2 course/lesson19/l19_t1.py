"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""

from queue import Queue
from threading import Thread

q = Queue()

def add():
    while True:
        surname = input("Введите фамилию студента(off - для завершения): ")
        if surname == 'off':
            break
        q.put(surname)

def remove():
    while True:
        if not q.empty():
            surname = q.get()
            print(f"Студент {surname} отчислен")
        else:
            break

q.put("Нартов")
q.put("Крдян")

t1 = Thread(target=add)
t2 = Thread(target=remove)

t1.start()
t2.start()

t1.join()
t2.join()