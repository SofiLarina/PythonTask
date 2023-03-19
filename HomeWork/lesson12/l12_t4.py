"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров,
а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""
def cacluate(**args):
    average = sum(args) / len(args)
    list = []
    for i in args:
        if i > average:
            list.append(i)
    return (average, list)
print(cacluate)