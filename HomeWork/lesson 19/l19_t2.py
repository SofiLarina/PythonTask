"""
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация,
то есть соединение, строк. В остальных случаях введенные числа суммируются.
"""

a = input("Введите первое число: ")
b = input("Введите второе число: ")

try:
    a = int(a)
    b = int(b)
    res = a + b
except ValueError:
    res = str(a) + str(b)

print(res)