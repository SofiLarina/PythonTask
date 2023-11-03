"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""
import os
from threading import Thread
from queue import Queue

q = Queue()

def read(path, q):
    with open(path, "r") as f:
        names = f.readlines()
        for name in names:
            name = name.strip()
            file_path = os.path.join("/lesson19", name + ".txt")
            q.put(file_path)

def create():
    while not q.empty():
        file_path = q.get()
        with open(file_path, "w") as f:
            f.write("Hello!")

th1 = Thread(target=read, args=("Names.txt", q))
th2 = Thread(target=create)
th1.start()
th2.start()
th1.join()
th2.join()