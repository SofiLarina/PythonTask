"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""
import csv
with open("Task1.csv") as f:
    reader = list(csv.reader(f, delimiter = ";"))
    for line in reader:
        print({(line[0], line[1]): {line[2]: line[3]}})