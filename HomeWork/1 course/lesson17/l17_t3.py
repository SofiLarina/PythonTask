"""
Напишите программу, которая будет считывать содержимое файла,
добавлять к считанным строкам порядковый номер и сохранять их в таком
виде в новом файле. Имя исходного файла необходимо запросить у пользователя,
так же, как и имя целевого файла. Каждая строка в созданном
файле должна начинаться с ее номера, двоеточия и пробела, после чего
должен идти текст строки из исходного файла.
"""
file3 = input("Введите имя файла: ")

with open(file3,"r") as fr:
    with open(f"new_{file3}","w") as fw:
        count = 1
        for i in fr:
            fw.write(f"{count}: {i}")
            count += 1