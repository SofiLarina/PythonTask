"""
Напишите генератор выводящий все символы строки на печать,
но только в том случае, если они являются буквами (остальные игнорируются).
"""
def generator(string):
    for char in string:
        if char.isalpha():
            yield char

my_string = input("Введите предложение: ")
for letter in generator(my_string):
    print(letter)