"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки.
И создаем папку по указанному пути.
"""
import sys
import os

if len(sys.argv) < 3:
    print("Недостаточно аргументов")
else:
    path = sys.argv[1]
    folder_name = sys.argv[2]

    folder_path = os.path.join(path, folder_name)

    try:
        os.makedirs(folder_path)
        print(f"Папка {folder_name} успешно создана по пути {path}")
    except FileExistsError:
        print(f"Папка {folder_name} уже существует по пути {path}")
    except Exception as e:
        print(f"Произошла ошибка при создании папки: {e}")