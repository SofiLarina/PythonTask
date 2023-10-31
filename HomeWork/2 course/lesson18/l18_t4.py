"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
import os
import random
import time
from threading import Thread

def create_files(files_dir):
    for i in range(5):
        file_path = os.path.join(files_dir, f"file{i}.txt")
        with open(file_path, 'w') as file:
            file.write(f"ids:{random.randint(1, 100)}\n")

def replace_ids(file_path):
    with open(file_path, 'r+') as file:
        content = file.read()
        content = content.replace("ids", "id")
        file.seek(0)
        file.write(content)
        file.truncate()

def main(files_dir):
    start_time = time.time()

    create_files(files_dir)

    files = os.listdir(files_dir)
    threads = []
    for file_name in files:
        file_path = os.path.join(files_dir, file_name)
        thread = Thread(target=replace_ids, args=(file_path,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print("Время выполнения программы:", execution_time)

if __name__ == "__main__":
    files_dir = r"C:\Users\София\PythonTask\PythonTasks\HomeWork\2 course\lesson18\files"
    main(files_dir)