"""
Из файла Task1.csv выведите данные в формате:
Имя - Звание
"""
import csv

with open('Task1.csv') as f:
    reader = list(csv.reader(f, delimiter = ";"))
    for i in reader:
        print(i[0], "-", i [3])