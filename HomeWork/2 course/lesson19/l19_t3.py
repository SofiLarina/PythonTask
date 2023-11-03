"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


def read(file_path, q):
    with open(file_path, "r") as f:
        for name in f:
            name = name.strip()
            path = f"{name}.txt"
            q.put(path)

def create(file_path):
    with open(file_path, "w") as f:
        f.write("Hello!")

if __name__ == "__main__":
    q = Queue()

    with ThreadPoolExecutor() as executor:
        executor.submit(read, "Names.txt", q)

    with ThreadPoolExecutor() as executor:
        while not q.empty():
            file_path = q.get()
            executor.submit(create, file_path)

    print("Код был выполнен")