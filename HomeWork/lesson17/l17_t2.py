"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open("file1.txt", "w") as f:
    f.write(", но у меня не получается")
with open("file2.txt", "w") as f:
    with open("file.txt", "r") as f1:
        f.write(f1.read())
    with open("file1.txt", "r") as f2:
        f.write(f2.read())
with open("file2.txt", "r") as f:
    print(f.read())