"""
Напишите генератор выводящий все числа делящиеся на 11 в диапазоне от 0 до 100
"""
def divisible(start, end):
    for n in range(start, end+1):
        if n % 11 == 0:
            yield n

for n in divisible(0, 100):
    print(n)