"""
Напишите скрипт который в качестве параметра из командной
строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""
import sys

if len(sys.argv) < 2:
    print("Недостаточно аргументов. Укажите имя файла.")
else:
    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            commands = file.readlines()

        for command in commands:
            exec(command)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при выполнении команд: {e}")